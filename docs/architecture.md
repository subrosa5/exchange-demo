# Архитектура

`exchange_demo.orders` проверяет входящие заявки до matching. `exchange_demo.matching` реализует выбор лучшего bid по правилу price-time priority. `exchange_demo.market_data` не выполняет сетевых вызовов и только сравнивает переданные timestamps.

Репозиторий намеренно мал: его можно полностью индексировать на домашнем ПК и использовать для воспроизводимых задач code retrieval, patch и test без реальной биржевой инфраструктуры.
