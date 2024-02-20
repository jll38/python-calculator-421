import pytest
from calculator.operations import operations
class TestOperations:

    # Add two integers
    def test_add_two_integers(self):
        assert operations.add(2, 3) == 5

    # Add two floats
    def test_add_two_floats(self):
        assert operations.add(2.5, 3.5) == 6.0

    # Subtract two integers
    def test_subtract_two_integers(self):
        assert operations.subtract(5, 3) == 2

    # Divide by zero raises ValueError
    def test_divide_by_zero_raises_ValueError(self):
        with pytest.raises(ValueError):
            operations.divide(5, 0)

    # Floor divide by zero raises ValueError
    def test_floor_divide_by_zero_raises_ValueError(self):
        with pytest.raises(ValueError):
            operations.floorDivide(5, 0)

    # Modulo by zero raises ValueError
    def test_modulo_by_zero_raises_ValueError(self):
        with pytest.raises(ValueError):
            operations.modulo(5, 0)