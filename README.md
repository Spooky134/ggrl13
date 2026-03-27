# ggrl13 — Руководство по развертыванию 

## Операционная система

 - Linux Ubuntu 24.04

## Установка системы

### 1. Обновление системы

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Установка зависимостей

```bash
sudo apt install -y python3 python3-venv python3-pip nginx postgresql postgresql-contrib curl git
```

### 3. Установка Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```

## Клонирование проекта

```bash
git clone https://github.com/Spooky134/ggrl13.git
cd ggrl13
```

## Настройка базы данных (PostgreSQL)

Войдите в PostgreSQL:

```bash
sudo -u postgres psql
```

Создать пользователя и базу данных:
```sql
CREATE USER ggrl_user WITH PASSWORD 'strong_password';
CREATE DATABASE ggrl13 OWNER ggrl_user;
GRANT ALL PRIVILEGES ON DATABASE ggrl13 TO ggrl_user;
\q
```

## Переменные окружения

Создать файл `.env` в корне проекта:

```bash
nano .env
```

Пример содержимого:

```env
DEBUG=False
SECRET_KEY=django-insecure-$7w=*po!q^@mra)4bu_9_y6%jyppq_pnuy)m1=--03*!ry*)uz

DB_NAME=ggrl13
DB_USER=ggrl_user
DB_PASSWORD=strong_password
DB_HOST=localhost
DB_PORT=5432
```

## Установка зависимостей Python

```bash
poetry config virtualenvs.in-project true
poetry install --no-interaction --no-ansi
```

## Настройка Django

Выполнение миграции:
```bash
poetry run python manage.py migrate
```

Сбор статических файлов:
```bash
poetry run python manage.py collectstatic --noinput
```

## Запуск сервера (Gunicorn)
```bash
nohup poetry run gunicorn ggrl13.wsgi:application --bind 127.0.0.1:8000 > gunicorn.log 2>&1 &
```

## Настройка Nginx

Копирование конфигурации:

```bash
sudo cp nginx.conf /etc/nginx/sites-available/ggrl13
```

Активация сайта:
```bash
sudo ln -s /etc/nginx/sites-available/ggrl13 /etc/nginx/sites-enabled/
```

Удаление стандартного сайта:
```bash
sudo rm -f /etc/nginx/sites-enabled/default
```

Проверка и перезапуск:
```bash
sudo nginx -t
sudo systemctl restart nginx
```


