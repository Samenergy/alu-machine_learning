#!/usr/bin/env python3
'''
    A function def add_matrices(mat1, mat2):
    that adds two matrices
'''

def add_matrices(mat1, mat2):
    '''
        A function def add_matrices(mat1, mat2):
        that adds two matrices
    '''
    # Check if both inputs are lists (for nested structure)
    if isinstance(mat1, list) and isinstance(mat2, list):
        # Ensure that both matrices have the same length
        if len(mat1) != len(mat2):
            return None
        # Recursively add each element
        return [add_matrices(a, b) for a, b in zip(mat1, mat2)]
    # Check if both are numbers (base case)
    elif isinstance(mat1, (int, float)) and isinstance(mat2, (int, float)):
        return mat1 + mat2
    # If any structure mismatch occurs, return None
    return None
