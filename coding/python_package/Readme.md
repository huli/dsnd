## Tiny module for working with Gaussian distributions

### Usage instructions

* `pip install .`
* fire up python
* you're ready to go:
```python
from distributions import Gaussian

gaussian1 = Gaussian(10, 5)
gaussian2 = Gaussian(12, 4)
print(gaussian1 + gaussian2)
# mean 22, standard deviation 6.4031242374328485
```
