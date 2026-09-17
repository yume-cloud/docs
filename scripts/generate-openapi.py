#!/usr/bin/env python
"""Export the backend's OpenAPI schema into `openapi/`, one file per section.

The backend already splits its API into sections: `swagger_groups` in
`rental_tenant_back/urls.py` maps a section key to the URL patterns it serves,
and `rental_tenant_back/api_docs.py` gives each key a name, description and icon.
This script walks the same map, so `openapi/<key>.json` is the same
document the backend serves at `/v1/docs/openapi/<key>.json` — plus a title,
a description and a `servers` list, which the live endpoint fills in per request.

Run it with the backend's virtualenv, from the docs repo:

    ../rental_tenant_back/.venv/bin/python scripts/generate-openapi.py

Then review the diff: an endpoint that disappears here disappeared from the API.
"""

import json
import os
import pathlib
import sys


DOCS_ROOT = pathlib.Path(__file__).resolve().parent.parent
BACKEND = pathlib.Path(os.environ.get("YUME_BACKEND", DOCS_ROOT.parent / "rental_tenant_back"))
OUT_DIR = DOCS_ROOT / "openapi"

SERVERS = [
    {"url": "https://api.yume.cloud", "description": "Production"},
    {"url": "https://api.stage.yume.cloud", "description": "Stage"},
]


def main() -> int:
    if not (BACKEND / "manage.py").exists():
        sys.exit(f"backend not found at {BACKEND} — set YUME_BACKEND to its path")

    sys.path.insert(0, str(BACKEND))
    os.chdir(BACKEND)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rental_tenant_back.settings")
    os.environ.setdefault("SECRET_KEY", "openapi-export-dummy-key")
    os.environ.setdefault("DEBUG", "0")

    import django

    django.setup()

    from django.db import connection
    from django_tenants.utils import get_tenant_model

    connection.tenant = get_tenant_model()(id=1, schema_name="public")

    from drf_spectacular.generators import SchemaGenerator

    from rental_tenant_back.api_docs import SECTIONS
    from rental_tenant_back.urls import swagger_groups

    missing = [key for key in swagger_groups if key not in SECTIONS]
    if missing:
        sys.exit(f"no SECTIONS metadata for {', '.join(missing)} — add it in api_docs.py")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = set()
    total = 0

    for key, patterns in swagger_groups.items():
        section = SECTIONS[key]
        schema = SchemaGenerator(patterns=patterns).get_schema(request=None, public=True)
        schema["info"]["title"] = f"Yume API — {section['name']}"
        schema["info"]["description"] = section["description"]
        schema["servers"] = SERVERS

        target = OUT_DIR / f"{key}.json"
        target.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written.add(target.name)

        operations = sum(
            1
            for methods in schema.get("paths", {}).values()
            for method in methods
            if method in ("get", "post", "put", "patch", "delete")
        )
        total += operations
        print(f"{key:<14} {len(schema.get('paths', {})):>4} paths {operations:>4} operations  {section['name']}")

    stale = sorted(p.name for p in OUT_DIR.glob("*.json") if p.name not in written)
    if stale:
        print(f"\nstale, no longer in swagger_groups: {', '.join(stale)}")

    print(f"\n{total} operations in {len(written)} sections -> {OUT_DIR.relative_to(DOCS_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
