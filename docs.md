# Vector and Matrix Operations

## Vector Functions

### `scalar_product(v1, v2)`
Calculates dot product of two vectors.
- **Parameters:** `v1`, `v2` - lists of numbers
- **Returns:** float - dot product
- **Raises:** `ValueError` if vectors have different lengths

### `vector_length(v)`
Calculates Euclidean length of a vector.
- **Parameters:** `v` - list of numbers
- **Returns:** float - vector length

### `angle_between_vectors(v1, v2, form="r")`
Calculates angle between two vectors.
- **Parameters:** `v1`, `v2` - vectors, `form` - "r" for radians, "d" for degrees
- **Returns:** float - angle in specified format
- **Raises:** `ValueError`, `ZeroDivisionError`, `SyntaxError`

## Matrix Functions

### `matrix_addition(mat1, mat2)`
Adds two matrices element-wise.
- **Parameters:** `mat1`, `mat2` - 2D lists
- **Returns:** list - resulting matrix
- **Raises:** `ValueError` if matrices have different dimensions

### `matrix_multiplication(mat1, mat2)`
Multiplies two matrices.
- **Parameters:** `mat1`, `mat2` - 2D lists
- **Returns:** list - product matrix
- **Raises:** `ValueError` if dimensions are incompatible

### `matrix_transpose(matrix)`
Transposes a matrix (swaps rows and columns).
- **Parameters:** `matrix` - 2D list
- **Returns:** list - transposed matrix

## Examples

```python
# Vectors
v1, v2 = [1, 2, 3], [4, 5, 6]
dot = scalar_product(v1, v2)  # 32
length = vector_length([3, 4])  # 5.0
angle = angle_between_vectors([1, 0], [0, 1], 'd')  # 90.0

# Matrices
A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
sum_AB = matrix_addition(A, B)  # [[6, 8], [10, 12]]
product = matrix_multiplication(A, B)  # [[19, 22], [43, 50]]
transpose = matrix_transpose(A)  # [[1, 3], [2, 4]]
