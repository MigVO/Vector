"""
Tests  development for class vector
"""


from ..vector import Vector, to_polar, from_polar
import pytest

vector1 = [10.5, 2.3, -3.3]
vector2 = [-15.1, 4.7, 8.5]


class TestVectorInput:
    """
    Check for different input possibilities and the Exceptions raised when input is incorrect.
    """

    def test_ducktyping(self):

        v = [1.1, 2.2, 3.3]
        v1 = Vector(v)
        v2 = Vector(tuple(v))
        v3 = Vector(set(v))
        v4 = Vector(v[0], v[1], v[2])
        v5 = Vector(Vector(v))
        assert v1 == v2
        assert v1 == v3
        assert v1 == v4
        assert v1 == v5

    def test_input_string(self):
        with pytest.raises(TypeError):
            Vector('abc')

    def test_input_bad_array(self):
        with pytest.raises(TypeError):
            Vector([1, 2, "a"])

    def test_wrong_input(self):
        with pytest.raises(TypeError):
            Vector({"x":1, "y":2, "z":3})


class TestVectorCalculations:
    def test_dot_product_input(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        result1 = v1.dot(v2)
        result2 = v1.dot(vector2)
        assert result1 / result2 - 1 < 0.0001

    def test_dot_product_result(self):
        v1 = Vector(2,2,2)
        v2 = Vector(1,1,1)
        dot_result = v1.dot(v2)
        assert dot_result == 6

    def test_cross_product(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        assert isinstance(v1.cross(v2), Vector)

    def test_cross_product_result(self):
        v1 = Vector(vector1)
        v2 = Vector(vector2)
        assert v1.cross(v2) == -1*v2.cross(v1)

    def test_cross_product_result_2(self):
        v1 = Vector(1, 0 , 0)
        v2 = Vector(0, 1, 0)
        v3 = Vector(0, 0, 1)
        assert v1.cross(v2) == v3
        assert v1.cross(v3) == v2
        assert v2.cross(v3) == v1


class TestVectorOperations:
    def test_magnitude(self):
        v1 = Vector([1,1,0])
        assert v1.magnitude == 2**0.5

    def test_sum(self):
        v1 = Vector([1,1,1])
        v2= Vector([3, 0, 0])
        assert v1 + v2 == [4, 1, 1]

    def test_mul(self):
        v1 = Vector([2,2,2])
        assert v1 * 3 == [6,6,6]
        assert v1 * 5 == 5 * v1

    def test_div(self):
        v1 = Vector([2.0, 2, 2])
        assert v1 / 2 == [1, 1, 1]


def test_simple_polar_conversion():
    v1 = Vector(vector1)
    v2 = to_polar(v1)
    v3 = from_polar(v2)

    assert v1.x - v3.x < 0.0001  # needed because float approximation
    assert v1.y - v3.y < 0.0001
    assert v1.z - v3.z < 0.0001

