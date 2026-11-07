# Exchange Demo

Синтетический Python-репозиторий для проверки code RAG и coding loop. Он не связан с реальной биржей и не содержит production-данных, секретов или торговых ключей.

## Состав

- `orders.py` — валидация стоимости и параметров заявки;
- `matching.py` — выбор лучшей заявки по price-time priority;
- `market_data.py` — определение устаревшего market data snapshot;
- `docs/` — нормативные правила для синтетического домена;
- `tests/` — рабочие проверки и три `expectedFailure`, фиксирующие известные дефекты.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

Тестовый suite зелёный: ожидаемые падения помечены `unittest.expectedFailure`. Это исходные задачи для будущего patch/test цикла, а не пример корректной торговой реализации.

## Намеренные дефекты

1. `validate_order` отклоняет заявку ровно на границе допустимого notional.
2. `best_bid` учитывает время, но не сравнивает цену.
3. `is_stale` не считает snapshot устаревшим точно на пороге.

Исправления выполняются только через отдельный diff и человеческий review в основном проекте `local-coding-copilot`.
