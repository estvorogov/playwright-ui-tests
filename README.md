# README.md
# Playwright Test Project

Автоматизированные UI тесты с использованием Python + Playwright + Pytest.

## Запуск тестов
```bash
pip install -r requirements.txt
pytest --headed --alluredir=allure-results
```

## Сценарии:
- Авторизация
- Работа с корзиной
- Оформление заказа

## CI/CD
Проект запускается в GitHub Actions при каждом push.
