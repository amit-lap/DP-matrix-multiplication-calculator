def calc_cell(row, col, arr, d):
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
    if num_of_matrices <= 0:
        raise ValueError("Number of matrices must be a positive integer.")


def validate_dim_lst(num_of_matrices, dim_lst):
    if not isinstance(dim_lst, list) or not all(isinstance(x, int) and x > 0 for x in dim_lst):
        raise ValueError("Dimension list must be a list of positive integers.")
    if len(dim_lst) != num_of_matrices + 1:
        raise ValueError(f"Dimension list length must be {num_of_matrices + 1}.")


def get_user_input():
    while True:
        try:
            # Getting and validating the number of matrices
            num_of_matrices = int(input("Enter the number of matrices: "))
            validate_num_of_matrices(num_of_matrices)

            # Getting and validating the matrices dimensions list
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

    # Calculating the solution
    solution = matrix_multiplication(num_of_matrices, dim_lst)
    print(f"Minimum number of operations when multiplying matrices is: {solution[0]},"
          f" The first division point is: {solution[1]}")


# Starting the program
get_user_input()
