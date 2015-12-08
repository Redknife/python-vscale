## Установка
python setup.py install

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

