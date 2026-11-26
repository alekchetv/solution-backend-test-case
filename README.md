# Тестовое задание

REST API на Django + DRF, которое возвращает категории блюд с вложенным списком
**опубликованных** блюд (`is_publish=True`). Категории без опубликованных блюд
в выборку не попадают.

- **Вью:** [`api/views.py`](https://github.com/alekchetv/solution-backend-test-case/blob/main/api/views.py)

## Стек

- Python 3.14
- Django 6.1
- Django REST Framework
- SQLite

## Запуск


```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
pip install -r requirements.txt
```


### 3. Миграции и данные

```powershell
python manage.py migrate
```


```powershell
python manage.py runserver
```

## Просмотр эндпоинта

```
GET http://127.0.0.1:8000/api/v1/foods/
```

Возвращает JSON-массив категорий с вложенными блюдами.

