# test_stripe
Django + Stripe API - Тестовое задание

## Описание

Простой Django-сервер с интеграцией Stripe API, реализующий функционал онлайн-оплаты товаров и заказов.

## Требования

- Python 3.12
- PostgreSQL
- Django
- Stripe API
- Docker

## Функциональность

- Модель Item с полями: name, description, price.
- Эндпоинт GET /item/<id> — HTML страница с информацией о товаре и кнопкой "Buy".
- Эндпоинт GET /buy/<id> — создание Stripe Checkout Session и возврат session_id.
- Редирект на форму оплаты Stripe после нажатия на кнопку.
- Docker контейнеризация.
- Использование .env переменных.
- Модель Order — объединение нескольких товаров.
- Stripe Checkout по Order, с учетом полной суммы.
- Подключено в Django Admin.
- Онлайн-деплой с доступом к админке.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/test_stripe.git
```

```
cd test_stripe 
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Создайте файл .env и заполните его своими данными по образцу:

```
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
POSTGRES_DB=shopdb
POSTGRES_USER=shopuser
POSTGRES_PASSWORD=secret
DB_HOST=db
DB_PORT=5432
```

#### Запустите систему контейнеров.
```bash
docker-compose up --build
```
#### Выполните миграции в контейнере backend.
```bash
docker-compose exec web python manage.py migrate
```
#### Создайте суперпользователя.
```bash
docker-compose exec web python manage.py createsuperuser
```
#### Остановить контейнер.
```bash
docker-compose down
```

### Онлайн доступ
Проект развернут по адресу:
https://test-stripe-635h.onrender.com/

### Пример страницы товара:
https://test-stripe-635h.onrender.com/item/1

### Доступ к админке:
https://test-stripe-635h.onrender.com/admin/
Логин: admin
Пароль: admin123

### Эндпоинты

GET     */*             — Главная страница с формой ввода города.

POST    */weather/*     — Обработка формы, отображение прогноза погоды.

GET     */stats/*       — API со статистикой по частоте введённых городов.

GET     */admin/*       — Панель администратора Django.


## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/