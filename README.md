# Vector

`Vector`is a minimal package that allows to work with vectors in 3D without needing more complicated packages like `numpy`

Its purpose is only **pedagogical** and intends to show how to create and organize a minimal package. 


## Installation

```
git clone https://github.com/mig-ver/Vector


pip install -e .
```




## Usage

Vectors can be declared in different forms




```
from vector import Vector

v1 = Vector(1, 2, 3)

v2 = Vector([1, 2, 3])

v3 = Vector((1, 2, 3))

```

They will all produce the same vector


### Properties


Magnitude of the vector can be obtained with `vector.magnitude` and direction with `vector.direction`




### Operations

All operations between vectors are implemented




```python
v1 = Vector(1, 2, 3)

v2 = Vector([2.1, -1.5, 5.3])


v3 = v1 + v2

v4 = 3*v1 + v2*5.5 - v3/2

v5 = v4.cross(v1)

value = V5.dot(v4)
```


# Issues

If you find the code useful or you feel they are omisions, please feel free to raise an issue



