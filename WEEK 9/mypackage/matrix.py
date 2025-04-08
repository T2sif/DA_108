import numpy as np
def input_matrix(rows,columns):
    matrix=[]
    print("enter the element row-wise:")
    for i in range(rows):
        row=list(map(int, input().split()))
        if len(row) !=columns:
            print("error")
            return None
        matrix.append(row)
    return np.array(matrix)
def matrix_addition(A,B):
    return np.add(A,B)
def matrix_multiplication(A, B):
    return np.dot(A, B)
def matrix_inverse(A):
    det_A = np.linalg.det(A)
    if det_A==0:
        return None
    else:
        return np.linalg.inv(A)