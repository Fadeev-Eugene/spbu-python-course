"""
Vector operations test module
"""

import math
import pytest
from project.vector_matrix_operations.Vector_oper import scalar_product, vector_length, angle_between_vectors


def test_scalar_product_basic():
    """Test scalar product of two vectors"""
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    assert scalar_product(v1, v2) == 32


def test_scalar_product_orthogonal():
    """Test scalar product of orthogonal vectors"""
    v1 = [1, 0]
    v2 = [0, 1]
    assert scalar_product(v1, v2) == 0


def test_raise_scalar_product():
    """Test scalar product of two vectors with different lengths"""
    v1 = [1, 2, 3]
    v2 = [1, 2]
    with pytest.raises(ValueError) as excinfo:
        scalar_product(v1, v2)
    assert str(excinfo.value) == "Vectors should have same length"


def test_vector_length():
    """Test length of vector"""
    v = [3, 4]
    assert vector_length(v) == 5


def test_vector_length_zero():
    """Test length of zero vector"""
    v = [0, 0, 0]
    assert vector_length(v) == 0


def test_vector_length_single():
    """Test length of single element vector"""
    v = [5]
    assert vector_length(v) == 5


def test_wrong_vector_length():
    """Test wrong length of vector"""
    v = [3, 4]
    assert vector_length(v) != 6


def test_angle_90_radians():
    """Test angle between two orthogonal vectors in radians"""
    v1 = [1, 0]
    v2 = [0, 1]
    assert angle_between_vectors(v1, v2, "r") == math.pi / 2


def test_angle_90_degrees():
    """Test angle between two orthogonal vectors in degrees"""
    v1 = [1, 0]
    v2 = [0, 1]
    assert angle_between_vectors(v1, v2, "d") == 90


def test_angle_0():
    """Test angle between two parallel vectors"""
    v1 = [1, 0]
    v2 = [2, 0]
    assert angle_between_vectors(v1, v2, "r") == 0


def test_angle_180():
    """Test angle between opposite vectors"""
    v1 = [1, 0]
    v2 = [-1, 0]
    assert angle_between_vectors(v1, v2, "r") == math.pi


def test_raise_angle_different_lengths():
    """Test angle between two vectors with different lengths"""
    v1 = [1, 2, 3]
    v2 = [1, 2]
    with pytest.raises(ValueError) as excinfo:
        angle_between_vectors(v1, v2)
    assert str(excinfo.value) == "Vectors should have same length"


def test_raise_angle_zero_vector():
    """Test angle with zero vector"""
    v1 = [1, 2]
    v2 = [0, 0]
    with pytest.raises(ZeroDivisionError):
        angle_between_vectors(v1, v2)


def test_raise_angle_invalid_format():
    """Test angle with invalid format parameter"""
    v1 = [1, 0]
    v2 = [0, 1]
    with pytest.raises(SyntaxError) as excinfo:
        angle_between_vectors(v1, v2, "invalid")
    assert "form=[" in str(excinfo.value)