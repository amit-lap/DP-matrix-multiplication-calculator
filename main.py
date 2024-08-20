"""
Matrix Multiplication Calculator

This script implements a matrix multiplication calculator using dynamic programming (DP) -
solving the Matrix chain multiplication optimization problem
and finding the minimum number of multiplication operations required for multiplying a chain of matrices
by selecting the best order to multiply the matrices (identifying the optimal way to parenthesize the matrices).

Functions:
    - calc_cell(row, col, arr, d): Computes the minimum cost of multiplying matrices from row to col.
    - matrix_multiplication(n, d): Uses dynamic programming to find the minimum cost for matrix multiplication.
    - validate_num_of_matrices(num_of_matrices): Validates that the number of matrices is a positive integer.
    - validate_dim_lst(num_of_matrices, dim_lst): Validates that the dimension list is a list of positive integers
      with the correct length.
    - get_user_input(): Handles user input and validates it before performing the matrix multiplication.
"""


def calc_cell(row, col, arr, d):
    """
    Calculate the minimum number of operations required to multiply matrices
    from row to col (which is each cell in The dynamic programming table representation).

    Parameters:
    row (int): The starting index of the matrix chain.
    col (int): The ending index of the matrix chain.
    arr (list): The dynamic programming table that stores sub-problem solutions.
    d (list): The dimensions list representing the matrices.

    Returns:
    tuple: A tuple containing the minimum multiplication cost and the division point.
    """
    if row == col - 1:
        return d[row] * d[row + 1] * d[col + 1], 0

    min_value = float('inf')
    s = 0
    for k in range(row + 1, col + 1):
        value = arr[row][k - 1][0] + arr[k][col][0] + (d[row] * d[k] * d[col + 1])
        if value < min_value:
            min_value = value
            s = k

    return min_value, s


def matrix_multiplication(n, d):
    """
    Calculate the minimum number of operations required to multiply a chain of n matrices.
    The function prints for each cell in the dynamic programming table the
    minimum multiplication cost and the division point.

    Parameters:
    n (int): The number of matrices.
    d (list): The dimensions list representing the matrices.

    Returns:
    tuple: A tuple containing the minimum multiplication cost and the first division point.
    """
    rows = cols = n
    arr = [[(0, 0) for _ in range(cols)] for _ in range(rows)]

    rows_end = n - 1
    cols_start = 2

    while rows_end >= 1 and cols_start <= n:
        i = 1
        j = cols_start

        while i <= rows_end and j <= n:
            print(f"cell[{i},{j}]:")
            arr[i - 1][j - 1] = calc_cell(i - 1, j - 1, arr, d)
            print(f"value, division point: {arr[i - 1][j - 1]}")
            i += 1
            j += 1

        rows_end -= 1
        cols_start += 1

    return arr[0][n - 1]


def validate_num_of_matrices(num_of_matrices):
    """
    Validate that the number of matrices is a positive integer.

    Parameters:
    num_of_matrices (int): The number of matrices to be validated.

    Raises:
    ValueError: If the number of matrices is not a positive integer.
    """
    if num_of_matrices <= 0:
        raise ValueError("Number of matrices must be a positive integer.")


def validate_dim_lst(num_of_matrices, dim_lst):
    """
    Validate that the dimension list is correctly formatted.

    Parameters:
    num_of_matrices (int): The number of matrices.
    dim_lst (list): The dimension list representing the matrices.

    Raises:
    ValueError: If the dimension list is not valid.
    """
    if not isinstance(dim_lst, list) or not all(isinstance(x, int) and x > 0 for x in dim_lst):
        raise ValueError("Dimension list must be a list of positive integers.")
    if len(dim_lst) != num_of_matrices + 1:
        raise ValueError(f"Dimension list length must be {num_of_matrices + 1}.")


def get_user_input():
    """
    Handle user input and validate it before performing matrix multiplication.

    The function prompts the user for the number of matrices and their dimensions,
    validates the input, and then calculates and displays the minimum number of operations.
    """
    while True:
        try:
            # Getting and validating the number of matrices
            num_of_matrices = int(input("Enter the number of matrices: "))
            validate_num_of_matrices(num_of_matrices)

            # Get and validate the matrices dimensions list
            while True:
                try:
                    dim_lst = list(map(int, input(
                        f"Enter the dimensions as {num_of_matrices + 1} space-separated integers: ").split()))
                    validate_dim_lst(num_of_matrices, dim_lst)
                    break  # Exit the loop if dim_lst is valid
                except ValueError as ve:
                    print(f"Input error: {ve}. Please try again.")

            break  # Exit the outer loop if all inputs are valid
        except ValueError as ve:
            print(f"Input error: {ve}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    # Calculate the solution
    solution = matrix_multiplication(num_of_matrices, dim_lst)
    print(f"Minimum number of operations when multiplying matrices is: {solution[0]},"
          f" The first division point is: {solution[1]}")


# Start the program
get_user_input()
