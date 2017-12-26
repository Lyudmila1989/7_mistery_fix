# Решатель квадратных уравнений

The program "Solver of quadratic equations" is designed to find the real roots of a quadratic equation by its coefficients.

# Как использовать

The module ```quadratic_equation``` contains the function ```get_roots(a, b, c)```, which takes real numerical coefficients of the quadratic equation and returns a tuple containing its two real roots ```route1, route2```. If there are no real roots, the function will return ```None, None```. If the equation has one real root, the function returns a sequence: ```route1, None```.

Example:

'''bash
from quadratic_equation import get_roots

a, b, c = input()
print(get_roots(a, b, c)) 
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
