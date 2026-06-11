"""
Simple package to manage 3D vectors
The purpose of it is purely pedagogical and shouldn't be used in production environment

I want the following operations
TODO::
    v1 = Vector(list1)     -> It should also work with tuples, numpy arrays, etc ducktyping
    v2 = Vector(list2)
    v1 + v2 = Vector   ->  valid operation
    v1 - v2 = Vector   -> valid operation
    3 * v1  = Vector   -> valid operation
    v1 * v2 = Exception   ->  invalid operation
    v1 / v2 = Exception   ->  invalid operation
    v1 + 3  = Exception   ->  invalid operation
    v1.magnitude = float     -> returns the magnitude of the vector
    v1.direction = Vector    -> returns a Vector of magnitude = 1, so v1 = v1.magnitude * v1.direction
    v1.distance(v2) = Vector -> returns the vector between these two points
    v1.dot(v2) = float       -> returns the dot product of two vectors
    v1.cross(v2) = Vector    -> returns the cross product of two vectors
    v1.angle(v2) = float     -> returns the angle between two vectors
"""

import math
from collections.abc import Iterable
from typing import List, Union, overload


class Vector:
    """
    Class to work with vectors without help of numpy. Designed for teaching purposes

    Class can be initialized either with a vector-like input (list, tuple, set, numpy.array) or with a sequence of numbers

    Examples:

        v1 = Vector([1,2,3])
        v2 = Vector((1,2,3))
        v3 = Vector({1,2,3})
        v4 = Vector(numpy.array([1,2,3]))
        v5 = Vector(1,2,3)


    Parameters
    ----------
    x : float or array-like (default None)
    y : float (default None)
    z : float (default None)

    """

    @overload
    def __init__(self, items: List[float]) -> None:
        if all(isinstance(item, (int, float)) for item in items) is False:
            raise ValueError("Source vector cannot contain non-numeric values")

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        items = [x, y, z]
        if all(isinstance(item, (int, float)) for item in items) is False:
            raise ValueError("Source vector cannot contain non-numeric values")

    def __init__(self, *args):
        # Your existing logic here
        if len(args) == 1 and isinstance(args[0], Iterable):
            self.data = list(args[0])
        elif len(args) == 3:
            self.data = [float(x) for x in args]
        else:
            raise TypeError("Must provide either a list/tuple or three floats")

        if isinstance(args, Vector):
            self.data = args.data

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @property
    def z(self):
        return self.data[2]

    @property
    def magnitude(self):
        """
        the magnitude of the vector
        """
        mag = sum([x**2 for x in self.data]) ** 0.5
        return mag

    @property
    def direction(self):
        """
        the direction of the vector
        """
        d = self / self.magnitude
        return d

    def distance(self, vector) -> float:
        """
        Returns the distance between two points

        Parameters:
            vector: Vector to compare against
        """
        if not isinstance(vector, Vector):
            vector = Vector(vector)

        dist = sum([(x - y) ** 2 for x, y in zip(self.data, vector.data)]) ** 2

        return dist

    def angle(self, vector) -> float:
        """
        Returns the angle between two vectors

        Parameters:
            vector: Vector to compare against
        """
        if not isinstance(vector, Vector):
            vector = Vector(vector)

        return self.dot(vector) / (self.magnitude * vector.magnitude)

    def dot(self, vector) -> float:
        """
        Returns the dot product of two vectors

        Parameters:
            vector: Vector to compare against
        """
        if not isinstance(vector, Vector):
            vector = Vector(vector)
        return sum([x * y for x, y in zip(self.data, vector.data)])

    def cross(self, vector):
        """
        Returns the cross product of two vectors
        """
        if not isinstance(vector, Vector):
            vector = Vector(vector)
        a1, a2, a3 = self.data
        b1, b2, b3 = vector.data
        return Vector([a2 * b3 - a3 * b2, a1 * b3 - a3 * b1, a1 * b2 - a2 * b1])

    def __getitem__(self, item):
        """
        This does some magic
        """
        return self.data[item]

    def __setitem__(self, idx, value):
        self[idx] = value

    def __repr__(self):
        return "Vector(%s, %s, %s)" % (self.x, self.y, self.z)

    def __add__(self, other):
        """
        Define addition of vectors and forbid the addition with other objects
        """
        newvector = Vector(other)
        suma = Vector(self.x + newvector.x, self.y + newvector.y, self.z + newvector.z)
        return suma

    def __sub__(self, other):
        """
        Define subtraction of vectors and forbid it with other objects
        """
        newvector = Vector(other)
        sub = Vector(self.x - newvector.x, self.y - newvector.y, self.z - newvector.z)
        return sub

    def __mul__(self, other):
        """
        Define what can be multiplied and what not
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Can only operate con scalars")

        return Vector(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other):
        """
        Define what can be multiplied and what not
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Can only operate con scalars")

    def __truediv__(self, other):
        """
        Define what can be divided and what not
        """
        if not isinstance(other, (int, float)):
            raise TypeError("Can only operate con scalars")

        return Vector(self.x / other, self.y / other, self.z / other)

    def __radd__(self, other):

        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __eq__(self, other) -> bool:

        newvector = Vector(other)
        return (
            self[0] == newvector[0]
            and self[1] == newvector[1]
            and self[2] == newvector[2]
        )

    def __iter__(self):
        for value in self.data:
            yield value


"""
Utility functions to convert from and to polar coordinates
Ideally the class Vector should be able to handle them natively
"""


def from_polar(
    r: Union[int, float, list, tuple, set, "Vector"],
    theta: Union[int, float],
    phi: Union[int, float],
) -> "Vector":
    """
    Convert from polar coordinates to cartesian coordinates

    """
    tmp_vector = Vector(r, theta, phi)  # Should use a proper class for Polar vectors
    r = tmp_vector.x
    theta = tmp_vector.y
    phi = tmp_vector.z

    x = r * math.sin(theta) * math.cos(phi)
    y = r * math.sin(theta) * math.sin(phi)
    z = r * math.cos(theta)

    return Vector(x, y, z)


def to_polar(
    x: Union[int, float, list, tuple, set, "Vector"],
    y: Union[int, float],
    z: Union[int, float],
) -> list:

    vector = Vector(x, y, z)
    r = vector.magnitude
    theta = math.acos(vector.z / r)
    phi = math.atan(vector.y / vector.x)

    return [r, theta, phi]
