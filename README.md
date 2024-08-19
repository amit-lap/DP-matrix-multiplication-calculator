# Matrix Multiplication Calculator

This project implements a matrix multiplication calculator using dynamic programming (DP) -  solving the Matrix chain multiplication optimization problem and finding the minimum number of multiplication operations required for multiplying a chain of matrices by selecting the best order to multiply the matrices (identifying the optimal way to parenthesize the matrices).

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Input Format](#input-format)
- [Usage](#usage)
- [Example](#example)
- [Understanding the Code](#understanding-the-code)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Dynamic Programming Approach:** Efficiently computes the minimum number of operations required for matrix multiplication.
- **Input Validation:** Ensures that the user inputs valid data before proceeding with the calculation.
- **User-Friendly Prompts:** Guides the user through the input process, requesting corrections when necessary.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/matrix-multiplication-calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd matrix-multiplication-calculator
    ```

## Input Format
The program expects two inputs from the user:
1. **Number of Matrices (`num_of_matrices`):** The number of matrices to be multiplied (must be a positive integer).
2. **Matrix Dimensions (`dim_lst`):** A list of integers representing the dimensions of the matrices. The length of this list must be `num_of_matrices + 1`.

## Usage
1. Run the `main.py` script:
    ```bash
    python main.py
    ```
2. Follow the prompts to enter the number of matrices and their dimensions.

### Example
- **Number of Matrices:** `3`
- **Matrix Dimensions:** `10 30 5 60`

The program will compute the minimum number of operations required to multiply the matrices and the first division point for the optimal multiplication sequence.

### Sample Output
```plaintext
Enter the number of matrices: 3
Enter the dimensions as 4 space-separated integers: 10 30 5 60
Minimum number of operations when multiplying matrices is: 4500
The first division point is: 1
