## Возможности
 - Получение информации об аккаунте
 - Получение списка серверов
 - Манипуляции над сервером (создание / включение / выключение / перезапуск / etc)
 - Добавление/удаление ssh ключей
 - Получение информации об образах/тарифных планах/текущих задачах

## Зависимости
 - Python 3
 - Requests ( https://github.com/kennethreitz/requests )

## Установка
```bash
python setup.py install
```

## Примеры

### Получить список серверов 
```python
import vscale

manager = vscale.Manager(token="mysecrettoken")
scalets = manager.get_all_scalets()
```

### Получить информацию о сервере
```python
import vscale

manager = vscale.Manager(token="mysecrettoken")
scalet = manager.get_scalet(39624)
```

### Документация
Coming soon...
