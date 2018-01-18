# Solver of Quadratic Equations

The program "Solver of quadratic equations" is designed to find the real roots of a quadratic equation by its coefficients.

# How to Use

The module ```python quadratic_equation``` contains the function ```python get_roots(a, b, c)```, which takes real numerical coefficients of the quadratic equation and returns a tuple containing its two real roots ```python (root1, root2)```. If there are no real roots, the function will return ```python (None, None)```. If the equation has one real root, the function returns a consistency: ```python (root1, None)```.

## Code Example:

```python
from quadratic_equation import get_roots

a, b, c = map(float, raw_input().split(' '))
print(get_roots(a, b, c))
```

# How to Run

The script requires the installed Python interpreter version 3.5

Running on Linux:

```bash
python tests.py # it may be necessary to call python3 instead of python, depending on the settings of the operating system
```

Running on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers ― [DEVMAN.org](https://devman.org)
