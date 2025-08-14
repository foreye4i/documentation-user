# Timesheet SaaS (Django + DRF)

## Quickstart

```bash
cd /workspace/timesheet_saas
python3 virtualenv.pyz .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

- API docs: http://localhost:8000/api/docs/
- JWT: `POST /api/auth/jwt/token/` with username/password

## Apps
- organizations, accounts (custom `User`), clients, projects, tasks, timesheets

## Environment
- `DATABASE_URL` for Postgres or default sqlite
- Celery configured via `CELERY_BROKER_URL`