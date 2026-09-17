# CRM logic — рабочий глоссарий переименований

Источник для (1) переписывания страниц `ru/logic/*` на простые названия и (2) плана переименования в коде.
Статус по моделям: ✅ утверждено · ⏳ в работе.

Формат: `текущее_поле` → «Простое название» → `новый_код_идентификатор`

---

## 1. Аренда (`OrderRequest`) ✅

**Идентификация**
- `id_dense` → «Порядковый номер» → `sequential_number`
- `unique_id` → «Внешний код (устар.)» → `external_code` (deprecated)
- `plus_id` → «Номер заказа Yume Plus» → `plus_order_id`
- `client` → «Клиент» → `client`
- `status` → «Статус» → `status`

**Сроки**
- `rent_start` → «Плановое начало» → `planned_start`
- `rent_end` → «Плановое окончание» → `planned_end`
- `rent_fact_start` → «Фактическая выдача» → `actual_start`
- `rent_fact_end` → «Фактический возврат» → `actual_end`
- `autorenewal` → «Автопродление» → `auto_renewal`
- `autowithdraw` → «Автосписание» → `auto_withdraw`
- `duriation` → «Длительность» → `duration`
- `initial_duriation` → «Исходная длительность» → `initial_duration`
- `counting_duration` → «Оплачиваемая длительность» → `billable_duration`

**Деньги**
- `price` → «Сумма без скидок» → `amount_gross`
- `price_discount` → «Итоговая сумма к оплате» → `total_payable`
- `price_inventory` → «Сумма за инвентарь» → `inventory_amount`
- `price_inventory_discount` → «Инвентарь со скидкой» → `inventory_amount_net`
- `price_service` → «Сумма за услуги» → `service_amount`
- `price_service_discount` → «Услуги со скидкой» → `service_amount_net`
- `price_delivery` → «Стоимость доставки» → `delivery_amount`
- `price_referral` → «Реферальное вознаграждение» → `referral_amount`

**Налог**
- `tax_percent` → «Ставка налога, %» → `tax_percent`
- `tax_included` → «Налог включён в цену» → `tax_included`
- `price_tax` → «Сумма налога» → `tax_amount`

**Скидка**
- `discount` → «Скидка (промокод)» → `discount`
- `discount_amount` → «Размер скидки» → `discount_amount`
- `discount_inventory_amount` → «Скидка на инвентарь» → `discount_inventory_amount`
- `discount_service_amount` → «Скидка на услуги» → `discount_service_amount`
- `discount_combine` → «Суммировать скидки» → `combine_discounts`
- `additional_discount` → «Дополнительная скидка» → `additional_discount`

**Оплата и штрафы**
- `payment_status` → «Статус оплаты» → `payment_status`
- `paid_amount` → «Оплачено» → `paid_amount`
- `time_exceed` → «Просрочено» → `is_overdue`
- `penalty_amount` → «Сумма штрафов» → `penalty_amount`
- `penalty_auto` → «Автоматический штраф» → `auto_penalty_amount`
- `penalty_custom` → «Ручной штраф» → `manual_penalty_amount`
- `penalty_duriation` → «Период просрочки» → `overdue_duration`
- `penalty_step_duriation` → «Шаг начисления штрафа» → `penalty_step`
- `penalty_disabled` → «Штрафы отключены» → `penalty_disabled`

**Связи и служебные**
- `user_created` → «Кем создана» → `created_by`
- `rental_point` → «Точка выдачи» → `issue_point`
- `rental_point_return` → «Точка возврата» → `return_point`
- `bag` → «Корзина» → `bag`
- `default_tarif_period` → «Период тарифа по умолчанию» → `default_tariff_period`
- `extra` → «Доп. данные» → `extra`
- `active` → «Активна» → `is_active`
- `deleted` → «Удалена» → `is_deleted`

**Вознаграждение персонала (`OrderRequestReward`)**
- `creation` → «% за создание» → `creation_percent`
- `reservation` → «% за бронирование» → `reservation_percent`
- `collection` → «% за сборку» → `collection_percent`
- `issue` → «% за выдачу» → `issue_percent`
- `receivement` → «% за приём» → `receivement_percent`

---

## 2. Единица инвентаря (`Inventory`) ✅

Название модели в тексте: **«Единица инвентаря»**.

- `name` → «Название» → `name`
- `unique_id` → «Артикул» → `article`
- `device_unique_id` → «ID устройства» → `device_id`
- `type` → «Тип (аренда/продажа)» → `type`
- `buy_price` → «Закупочная цена» → `purchase_price`
- `buy_date` → «Дата закупки» → `purchase_date`
- `sell_price` → «Цена продажи» → `sale_price`
- `sell_date` → «Дата продажи» → `sold_at`
- `lifetime` → «Срок службы, мес.» → `lifetime_months`
- `stock_price` → «Рыночная стоимость» → `market_value`
- `comment` → «Комментарий» → `comment`
- `category` → «Категория» → `category`
- `group` → «Группа» → `group`
- `rental_point` → «Точка проката» → `rental_point`
- `state` → «Состояние» → `state`
- `sublease_user` → «Владелец субаренды» → `sublease_owner`
- `sublease_percent` → «Процент субаренды» → `sublease_percent`
- `image` → «Фото» → `image`
- `prev_earning` → «Заработок до подключения в систему» (из прежней системы учёта) → `earning_before_onboarding`
- `extra` → «Доп. данные» → `extra`
- `deleted` → «Удалён» → `is_deleted`
- `deleted_at` → «Дата удаления» → `deleted_at`

Статус не хранится — вычисляется (`INREND`/`RESERVED`/`OVERDUE`/`WRITTEN_OFF`/`DISABLED`/`WAREHOUSE`/`REPAIR`/`BROKEN`/`SOLD`/`FREE`). Перечисления статусов — в отдельном раунде «Статусы и справочники».

---

## 2b. Транспорт (`InventoryCar`) ✅

Расширение единицы инвентаря для транспорта (связь 1:1). Название в тексте: **«Транспорт»**.

- `type` → «Тип транспорта» → `type`
- `inventory` → «Единица инвентаря» → `inventory`
- `number` → «Госномер» → `plate_number`
- `tech_passport` → «Техпаспорт» → `tech_passport`
- `serial` → «Серийный номер» → `serial`
- `vin` → «VIN» → `vin`
- `brand` → «Марка» → `brand`
- `model` → «Модель» → `model`
- `extra` → «Доп. данные» → `extra`

Тип транспорта (`InventoryCarType`): `CAR`→«Машина», `SCOOTER`→«Электросамокат», `MOTORCYCLE`→«Мотоцикл/Мопед».

---

## 3. Товар (`InventoryGroup`) ✅

Название модели в тексте: **«Товар»** (пул одинаковых единиц; в каталоге — карточка товара).

- `name` → «Название» → `name`
- `unique_id` → «Артикул» → `article`
- `barcode` → «Штрихкод» → `barcode`
- `filters` → «Характеристики» → `filters`
- `slug` → «Slug (URL)» → `slug`
- `comment` → «Комментарий» → `comment`
- `type` → «Тип (аренда/продажа)» → `type`
- `category` → «Категория» → `category`
- `discount` → «Скидка (промокод)» → `discount`
- `rental_point` → «Точка проката» → `rental_point`
- `lifetime` → «Срок службы, мес.» → `lifetime_months`
- `image` → «Фото» → `image`
- `extra` → «Доп. данные» → `extra`
- `published` → «Опубликован» → `is_published`
- `unit_type` → «Единица измерения» → `unit_type`
- `unit_price` → «Цена за единицу» → `unit_price`
- `unit_count` → «Кол-во единиц» → `unit_count`
- `unit_sum` → «Сумма по единицам» → `unit_total`
- `deleted` → «Удалён» → `is_deleted`
- `deleted_at` → «Дата удаления» → `deleted_at`

**НЕ документировать (легаси / кандидаты на удаление в коде):** `points`, `price`, `bonus`, `amount`.

---

## 4. Комплект ✅

### 4a. Комплект (`InventorySet`) — «Комплект»
- `name` → «Название» → `name`
- `unique_id` → «Артикул» → `article`
- `image` → «Фото» → `image`
- `category` → «Категория» → `category`
- `discount` → «Скидка (промокод)» → `discount`
- `time_period` → «Период тарификации» → `time_period`
- `extra` → «Доп. данные» → `extra`
- `comment` → «Комментарий» → `comment`
- `slug` → «Slug (URL)» → `slug`
- `published` → «Опубликован» → `is_published`
- `static` → «Фиксированная стоимость комплекта» (сохраняется ли полная стоимость при сдаче) → `has_fixed_price`
- `deleted` → «Удалён» → `is_deleted`
- `deleted_at` → «Дата удаления» → `deleted_at`
- **НЕ документировать (легаси):** `bonus`, `amount`, `price`, `pricing`

### 4b. Позиция комплекта (`InventorySetItem`) — «Позиция комплекта»
- `set` → «Комплект» → `set`
- `group` → «Товар» → `group`
- `count` → «Количество» → `count`
- `required` → «Обязательная» → `is_required`
- `tarif_price` → «Цена тарифа» → `tarif_price`
- `filter` → «Условие подбора» → `filter`
- **НЕ документировать (легаси):** `alternative`

### 4c. Цена комплекта (`InventorySetPrice`) — «Цена комплекта»
- `set` → «Комплект» → `set`
- `name` → «Название» → `name`
- `period` → «Период» → `period`
- `price` → «Цена за период» → `price`
- `published` → «Опубликован» → `is_published`
- `order` → «Порядок» → `sort_order`

---

## 5. Тарифы ✅

Глобально: `tarif → tariff` — опционально в плане по коду (по умолчанию не трогаем). В тексте всегда «тариф».

### 5a. Интервал времени (`TimePeriod`) — «Интервал времени» / «Период тарификации»
- `name` → «Название» → `name`
- `time` → «Длительность» → `duration`
- `weekdays` → «Дни недели» → `weekdays`
- `start` → «Начало (время)» → `start_time`
- `end` → «Конец (время)» → `end_time`
- `deleted` → «Удалён» → `is_deleted`

### 5b. Тариф инвентаря (`InventoryTarif`) — «Тариф инвентаря»
- `inventory` → «Единица инвентаря» → `inventory`
- `inventory_group` → «Товар» → `inventory_group`
- `inventory_set` → «Позиция комплекта» → `set_item`
- `inventory_set_price` → «Цена комплекта» → `set_price`
- `time_period` → «Период тарификации» → `time_period`
- `weekdays` → «Дни недели» → `weekdays`
- `start` → «Начало (время)» → `start_time`
- `end` → «Конец (время)» → `end_time`
- `published` → «Опубликован» → `is_published`
- `order` → «Порядок» → `sort_order`
- `name` → «Название» → `name`
- `price` → «Цена за период» → `price`

### 5c. Тариф услуги (`ServiceTarif`) — «Тариф услуги»
- `service` → «Услуга» → `service`
- `name` → «Название» → `name`
- `price` → «Цена» → `price`
- `duriation` → «Период тарификации» → `time_period`
- `one_time_payment` → «Разовый платёж» → `is_one_time`
- `published` → «Опубликован» → `is_published`
- **НЕ документировать:** `price_company`

---

## 6. Скидки ✅

### 6a. Скидка / промокод (`Discount`) — «Скидка (промокод)»
- `name` → «Название» → `name`
- `discount` → «Величина скидки» → `value`
- `discount_type` → «Способ расчёта» (процент/фикс. сумма) → `calculation_type`
- `type` → «Тип скидки» (процентная скидка / промокод с суммой) → `type`
- `start_at` → «Действует с» → `start_at`
- `end_at` → «Действует до» → `end_at`
- `promocode` → «Промокод» → `promocode`
- `usage_limit` → «Лимит использований» → `usage_limit`
- `created_by` → «Автор» → `created_by`
- `extra` → «Доп. данные» → `extra`
- `active` → «Активна» → `is_active`
- `deleted` → «Удалена» → `is_deleted`

### 6b. Применённая скидка (`OrderRequestDiscount`) — «Применённая скидка»
- `request` → «Аренда» → `request`
- `request_inventory` → «Строка инвентаря» → `request_inventory`
- `request_service` → «Строка услуги» → `request_service`
- `type` → «Тип (из справочника/ручная)» → `type`
- `discount` → «Скидка (промокод)» → `discount`
- `discount_amount` → «Размер скидки» → `discount_amount`
- `start_at` → «Действует с» → `start_at`
- `end_at` → «Действует до» → `end_at`
- `scheduled` → «По расписанию» → `is_scheduled`
- `scheduled_amount` → «Сумма по расписанию» → `scheduled_amount`
- `destination` → «Куда применяется» (заказ/инвентарь/услуга/доставка) → `destination`
- `created_by` → «Кем добавлена» → `created_by`
- `reason` → «Причина» → `reason`

---

## 7. Депозиты, штрафы, транзакции ✅

### 7a. Залог (`OrderRequestDeposit`) — «Залог»
- `request`→«Аренда» · `created_by`→«Кем принят» · `type`→«Тип залога» · `payment_type`→«Вид оплаты» · `status`→«Статус» · `amount`→«Сумма» · `deposit`→«Описание залога» (`description`) · `returned_at`→«Дата возврата»

### 7b. Штраф (`OrderRequestPenalty`) — «Штраф»
- `type`→«Тип (авто/ручной)» · `client`→«Клиент» · `request`→«Аренда» · `request_inventory`→«Строка инвентаря» · `amount`→«Сумма» · `amount_paid`→«Оплачено» · `created_by`→«Кем создан» · `reason`→«Причина» · `penalty`→«Дорожный штраф (ЕРАП, гос. система)» (`road_penalty`)
- **НЕ документировать:** `custom` (означает лишь «нередактируемый»)

### 7c. Вид оплаты (`PaymentType`) — «Вид оплаты»
- `name`→«Название» · `order`→«Порядок» (`sort_order`) · `deleted`→«Удалён» (`is_deleted`) · `deleted_at`→«Дата удаления»

### 7d. Счёт/касса (`PaymentAccount`) — «Счёт (касса)»
- `name`→«Название» · `default`→«По умолчанию» (`is_default`) · `initial`→«Начальный остаток» (`initial_balance`) · `balance`→«Текущий баланс» · `types`→«Виды оплаты» (`payment_types`) · `order`→«Порядок» (`sort_order`)

### 7e. Категория операции (`PaymentCategory`) — «Категория операции»
- `name`→«Название» · `parent`→«Родительская категория» · `type`→«Тип (приход/расход)» · `enabled`→«Активна» (`is_enabled`) · `order`→«Порядок» (`sort_order`)

### 7f. Операция/оплата (`Transaction`, `crm_payment`) — «Операция (оплата)»
- `method`→«Приход/расход» (`direction`) · `type`→«Вид оплаты» · `account`→«Счёт» · `category`→«Категория» · `request`/`sale`/`workshop`/`maintenance`→«Аренда/Продажа/Мастерская/ТО» · `deposit`/`penalty`→«Залог/Штраф» · `amount`→«Сумма» · `bonus`→«Бонусная операция» · `exchange`→«Обмен» · `tags`→«Метки» · `status`→«Статус» · `created_by`→«Кем создана» · `comment`/`extra`→«Комментарий/Доп. данные»

### 7g–j. Вспомогательные
- `TransactionSource`→«Распределение оплаты»: `transaction`→«Операция», `request_inventory/service/delivery/penalty/deposit`→«Строка инвентаря/услуги/доставки/штраф/залог», `amount`→«Сумма».
- `TransactionStatement`→«Статья прихода/расхода»: `type`→«Приход/расход», `inventory`→«Единица инвентаря», `counterparty`→«Контрагент», `maintenance_resource`→«Ресурс ТО», `date`→«Дата».
- `TransactionRefund`→«Возврат оплаты»: `reason`→«Причина».
- `TransactionKaspi`→«Kaspi-оплата»: `phone`→«Телефон», `payment_id`→«ID платежа Kaspi», `status`→«Статус», `receipt_url`→«Ссылка на чек».

---

## 8. Прибыль и окупаемость ✅

### 8a. Прибыль по дням (`Profit`, `crm_profit`) — «Прибыль (по дням)»
FK «к чему относится строка»: `service`→«Услуга», `inventory`→«Единица инвентаря», `inventory_group`→«Товар», `inventory_set`→«Комплект», `inventory_set_group`→«Ключ комплекта в аренде» (`set_group`), `category`→«Категория», `inventory_tarif`/`service_tarif`→«Тариф инвентаря/услуги», `request`+`request_inventory`/`request_service`/`request_delivery`/`request_penalty`→«Аренда/Строка инвентаря/Строка услуги/Доставка/Штраф», `sale`/`sale_inventory`→«Продажа/Позиция продажи», `workshop`/`workshop_resource`/`workshop_service`→«Задача мастерской/Ресурс/Услуга мастерской», `maintenance`→«ТО».

Значения/даты:
- `projected` → «Ожидаемый заработок (без скидок)» → `projected`
- `prediction` → «Плановый заработок (со скидкой)» → `prediction`
- `profit` → «Фактическая прибыль» → `profit`
- `start_at` → «Начало периода» · `end_at` → «Конец периода»
- `day` → «Номер дня» (`day_index`) · `days` → «Всего дней» (`total_days`) · `date` → «Дата»

### 8b. Окупаемость (`Payback`, `crm_payback`) — «Окупаемость»
- `inventory` → «Единица инвентаря» → `inventory`
- `date` → «Дата окупаемости» → `date` (⚠️ сейчас не заполняется — баг)
- `duration` → «Срок окупаемости» → `duration` (⚠️ сейчас не заполняется — баг)
- `efficiency` → «Окупаемость, %» → `efficiency`
- `prediction` → «Плановый заработок» → `prediction`
- `profit` → «Фактический заработок» → `profit`

---

## 9. Клиенты, бонусы, рефералы ✅

### 9a. Клиент (`Client`) — «Клиент»
- `name`→«Имя / название» · `type`→«Тип клиента» · `legal_type`→«Форма юрлица» · `gender`→«Пол» · `phone`/`email`→«Телефон/Email» · `avatar`→«Аватар» · `comment`→«Комментарий» · `ticks`→«Рейтинги» · `individual_passport`/`legal_passport`→«Документ физлица/юрлица» · `attraction`→«Способ привлечения» · `discount`→«Персональная скидка» · `user`→«Пользователь» · `agreement_id`→«Номер договора» (`agreement_number`) · `signed`→«Договор подписан» (`is_signed`) · `sign_date`→«Дата подписания» · `sign_expires`→«Действует до» · `uuid`/`extra`→«UUID/Доп. данные» · `deleted`/`deleted_at`→«Удалён/Дата удаления»
- **НЕ документировать:** `deposit`

### 9b. Бонусный счёт (`Bonus`) — «Бонусный счёт»
- `client`→«Клиент» · `amount`→«Баланс бонусов» (`balance`)

### 9c. Бонусная операция (`BonusTransaction`) — «Бонусная операция»
- `bonus`→«Бонусный счёт» · `amount`→«Сумма» · `request`→«Аренда» · `type`→«Тип (списание/начисление)» · `created_by`→«Кем создана»

### 9d. Рейтинг клиента (`ClientTick`) — «Рейтинг клиента»
- `name`→«Название» · `code`→«Цвет» (`color`) · `comment`→«Комментарий» · `blacklist`→«Чёрный список» (`is_blacklist`) · `request_count`→«Порог по числу аренд» · `request_amount`→«Порог по обороту» · `debt_limit`→«Лимит долга»

### 9e–i. Остальное
- `ClientTickRelation`→«Присвоение рейтинга»: `client`→«Клиент», `tick`→«Рейтинг».
- `ClientAttractionMethod`→«Способ привлечения»: `name`→«Название».
- `ReferralAgent`→«Реферальный агент»: `name`→«Имя», `phone`→«Телефон», `extra`→«Доп. данные».
- `ClientPassportIndividual`→«Документ физлица»: `iin`→«ИИН», `address`→«Адрес», `document_number`→«Номер документа», `issuer_manual`→«Кем выдан», `issue_date`→«Дата выдачи», `issue_date_end`→«Действует до», `birth_date`→«Дата рождения».
- `ClientPassportLegal`→«Документ юрлица»: `bin`→«БИН», `address`→«Адрес», `director`→«Директор», `iban`→«IBAN», `bik`→«БИК», `bank`→«Банк».
- `Loyalty` — на аккаунте `user.User` (публичная схема), вне `crm`; упомянуть как связанное.

---

## 10. Статусы и справочники (перечисления) ✅

- **Статус аренды** (`OrderRequestStatus`): `REQUEST`→«Заявка», `RESERVED`→«Забронирована», `INRENT`→«В аренде», `COMPLETED`→«Завершена», `DEBTOR`→«Должник», `CANCELED`→«Отменена»; флаг «Просрочено» (не отдельный статус).
- **Статус оплаты** (`OrderRequestPaymentStatus`): `PENDING`→«Ожидает оплаты», `PARTLY_PAID`→«Частично оплачена», `PAID`→«Оплачена».
- **Статус единицы инвентаря** (`InventoryStatus`, вычисляется): `FREE`→«Свободна», `RESERVED`→«Забронирована», `INREND`→«В аренде», `OVERDUE`→«Просрочена», `REPAIR`→«В ремонте», `BROKEN`→«Сломана», `WAREHOUSE`→«На складе», `SOLD`→«Продана», `WRITTEN_OFF`→«Списана», `DISABLED`→«Отключена», `DELIVERY`/`DELIVERY_BACK`→«Доставка»/«Возврат доставки».
- **Статус позиции в аренде** (`OrderRequestInventoryStatus`): `STEADY`→«Ожидает выдачи», `ISSUED`→«Выдана», `RECEIVED`→«Возвращена», `OVERDUE`→«Просрочена».
- **Действие по аренде** (`OrderRequestActionType`): `CREATION`→«Создание», `RESERVATION`→«Бронирование», `COLLECT`→«Сборка», `ISSUE`→«Выдача», `RECEIVEMENT`→«Приём», `CANCEL`→«Отмена», `ARCHIVE`→«Архивирование», `DELIVERY_PICKUP`→«Забор доставкой», `DELIVERY_ISSUE`→«Выдача доставкой».
- **Тип (аренда/продажа)** (`InventoryGroupType`): `RENT`→«Аренда», `SELL`→«Продажа».
- **Единица измерения** (`InventoryGroupUnitType`): `piece`→«Штука», `kg`→«Килограмм», `g`→«Грамм», `litre`→«Литр», `ml`→«Миллилитр», `m3`→«Кубометр».
- **Способ расчёта скидки** (`DiscountCalculationType`): `PERCENTAGE`→«Процент», `PRICE`→«Фиксированная сумма».
- **Тип скидки** (`DiscountType`): `DISCOUNT`→«Скидка», `PROMOCODE`→«Промокод», `AMOUNT`→«Сумма».
- **Применённая скидка — тип** (`OrderRequestDiscountType`): `DISCOUNT`→«Из справочника», `MANUAL`→«Ручная».
- **Применённая скидка — куда** (`OrderRequestDiscountDestination`): `REQUEST`→«Весь заказ», `INVENTORY`→«Инвентарь», `SERVICE`→«Услуга», `DELIVERY`→«Доставка».
- **Услуги** (`ServiceType`): `DELIVERY`→«Доставка», `BACK_DELIVERY`→«Обратная доставка», `TWO_WAY_DELIVERY`→«Туда-обратно», `WORKSHOP`→«Мастерская», `NOT_SELECTED`→«Не выбрано».
- **Залог — тип** (`DepositType`): `STRING`→«Описание (документ)», `AMOUNT`→«Сумма». **Статус** (`DepositStatus`): `DEFAULT`→«Не принят», `RECEIVED`→«Принят», `RETURNED`→«Возвращён».
- **Штраф — тип** (`PenaltyType`): `AUTO`→«Автоматический», `MANUAL`→«Ручной».
- **Транзакция — направление** (`TransactionMethod`): `CREDIT`→«Приход», `DEBIT`→«Расход». **Статус** (`TransactionStatus`): «Ожидает оплаты / Успешно / Ошибка / Истёк срок».
- **Клиент — тип** (`ClientType`): `INDIVIDUAL`→«Физлицо», `LEGAL`→«Юрлицо». **Форма юрлица** (`ClientLegalType`): `IP`→«ИП», `TOO`→«ТОО», `AO`→«АО», `PK`→«ПК». **Пол**: «Мужской / Женский».
- **Бонус — тип** (`BonusTransactionType`): `EARN`→«Начисление», `SPEND`→«Списание».
- **Отключение** (`DisableMethod`): `DELETE`→«Удаление», `ARCHIVE`→«Архив», `WRITTEN_OFF`→«Списание».
- **Продажа** (`SaleStatus`): «Черновик / Продано / Отменена». **Доставка** (`DeliveryStatus`): «Ожидает / В процессе / Выполнена / Отменена»; (`DeliveryType`): `DELIVERY`→«Доставка», `PICK_UP`→«Самовывоз».

---

## Правила переписывания страниц (для авторов)

1. Все технические имена моделей/полей → согласованные простые названия выше. Значения перечислений → русские подписи.
2. **Полностью убрать** из текста: пути к файлам (`crm/....py`), номера строк (`:123`), обратные кавычки с кодовыми идентификаторами. Остаётся чистый бизнес-текст.
3. Поля из списков «НЕ документировать» — **не упоминать вовсе**.
4. Сохранить: структуру, компоненты Mintlify, mermaid-схемы (узлы — простыми названиями), таблицы, числовые примеры, формулы (словами/значениями, без кодовых имён), перекрёстные ссылки `/ru/logic/...`.
5. Раздел «⚠️ Замечания по коду» → переименовать в «⚠️ Известные особенности и ограничения»; каждый пункт переписать простым языком (что происходит с точки зрения логики), убрав файлы/строки; severity-метки (высокий/средний/низкий) оставить.

---

## 11. Флаги функций (feature flags) ✅

Опубликованы отдельной страницей-справочником `ru/logic/feature-flags.mdx` («Флаги функций», вкладка «Логика системы» → группа «Инфраструктура»). Это единственная страница, где технические ключи настроек приводятся намеренно (они и есть предмет справочника) — плюс понятное русское название, эффект и значение по умолчанию.

Ключевой для расчёта — `feature_transaction_schedule` → «Посуточный график платежей» (по умолчанию выкл.). Его влияние на ценообразование (непрерывное время vs посуточный график: календарные сутки, нерабочие дни, бесплатный первый день, план платежей по дням, распределение оплат, списания Kaspi) описано в разделе «Тарифы и расчёт стоимости». Связанные флаги: `feature_transaction_schedule_initial_fee` («Плата за первый день»), `order_autoweekday` («Авто‑выходной день»), `client_kaspi_balance` («Списание с баланса Kaspi»).

Полный список (~60 флагов по группам: расчёт/график, аренды, штрафы, налог, комиссии персонала, инвентарь/товары, инвентаризация, доставка, бонусы, клиенты/метрики/интеграции) — на самой странице.
