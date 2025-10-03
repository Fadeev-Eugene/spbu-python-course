"""
Matrix operations test module
"""

import pytest
from project.vector_matrix_operations.Matrix_oper import matrix_addition, matrix_multiplication, matrix_transpose


def test_matrix_addition_basic():
    """Test addition of two matrices"""
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    result = matrix_addition(mat1, mat2)
    assert result == [[6, 8], [10, 12]]


def test_matrix_addition_zero():
    """Test addition with zero matrix"""
    mat1 = [[1, 2], [3, 4]]
    zero_mat = [[0, 0], [0, 0]]
    result = matrix_addition(mat1, zero_mat)
    assert result == mat1


def test_raise_matrix_addition():
    """Test addition of matrices with different sizes"""
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError) as excinfo:
        matrix_addition(mat1, mat2)
    assert str(excinfo.value) == "Matrix should have same sizes"


def test_matrix_multiplication_basic():
    """Test multiplication of two matrices"""
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 0], [1, 3]]
    result = matrix_multiplication(mat1, mat2)
    assert result == [[4, 6], [10, 12]]


def test_matrix_multiplication_identity():
    """Test multiplication with identity matrix"""
    mat1 = [[1, 2], [3, 4]]
    identity = [[1, 0], [0, 1]]
    result = matrix_multiplication(mat1, identity)
    assert result == mat1


def test_matrix_multiplication_zero():
    """Test multiplication with zero matrix"""
    mat1 = [[1, 2], [3, 4]]
    zero_mat = [[0, 0], [0, 0]]
    result = matrix_multiplication(mat1, zero_mat)
    assert result == [[0, 0], [0, 0]]


def test_raise_matrix_multiplication():
    """Test multiplication of incompatible matrices"""
    mat1 = [[1, 2, 3]]
    mat2 = [[1, 2]]
    with pytest.raises(ValueError) as excinfo:
        matrix_multiplication(mat1, mat2)
    assert "columns" in str(excinfo.value) and "rows" in str(excinfo.value)


def test_matrix_transpose_square():
    """Test transpose of square matrix"""
    matrix = [[1, 2], [3, 4]]
    result = matrix_transpose(matrix)
    assert result == [[1, 3], [2, 4]]


def test_matrix_transpose_rectangular():
    """Test transpose of rectangular matrix"""
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = matrix_transpose(matrix)
    assert result == [[1, 4], [2, 5], [3, 6]]


def test_matrix_transpose_single_row():
    """Test transpose of single row matrix"""
    matrix = [[1, 2, 3]]
    result = matrix_transpose(matrix)
    assert result == [[1], [2], [3]]


def test_matrix_transpose_empty():
    """Test transpose of empty matrix"""
    matrix = []
    result = matrix_transpose(matrix)
    assert result == []


def test_matrix_transpose_twice():
    """Test double transpose returns original matrix"""
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = matrix_transpose(matrix_transpose(matrix))
    assert result == matrix