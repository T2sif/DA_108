import mypackage.matrix
rows_A = int(input("Enter number of rows for Matrix A: "))
columns_A = int(input("Enter number of columns for Matrix A: "))

rows_B = int(input("Enter number of rows for Matrix B: "))
columns_B = int(input("Enter number of columns for Matrix B: "))
print("enter the first matrix:")
A=mypackage.matrix.input_matrix(rows_A,columns_A)
print("enter the second matrix:")
B=mypackage.matrix.input_matrix(rows_B,columns_B)
if A is not None and B is not None:
        print("the first matrix:\n",A)
        print("the second matrix:\n",B)
        if rows_A==rows_B and columns_A==columns_B:
            C=mypackage.matrix.matrix_addition(A, B)
            print("the matrix addition is:\n",C)
        else:
             print("error in addition")
        if columns_A==rows_B:
             D=mypackage.matrix.matrix_multiplication(A, B)
             print("the matrix multiplication is:",D)
        else:
             print("error in multiplication")
        
else:
    print("error")
print("inverse of  matrix is:\n")
A_inv=mypackage.matrix.matrix_inverse(A)
if A_inv is not None:
     print("inverse of first matrix is:\n",A_inv)
B_inv=mypackage.matrix.matrix_inverse(B)
if B_inv is not None:
     print("inverse of second matrix is:\n",B_inv)
