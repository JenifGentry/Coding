Row1 = int(input('Enter number of Rows in First Matrix: '))
Column1 = int(input('Enter number of Columns in First Matrix: '))
Row2 = int(input('Enter number of Rows in Second Matrix: '))
Column2 = int(input('Enter number of Columns in Second Matrix: '))
if Column1==Row2:
    matrix1 = []
    matrix2 = []
    result = []
    print('Enter the elements of First Matrix: ')
    for i in range(0,Row1):
        matrix1.append([])
        for j in range(0,Column1):
            matrix1[i].append(int(input()))
    print('Enter the elements of Second Matrix: ')
    for i in range(0,Row2):
        matrix2.append([])
        for j in range(0,Column2):
            matrix2[i].append(int(input()))
    for i in range(0,Row1):
        result.append([])
        for j in range(0,Column2):
            result[i].append(0)
            for k in range(0,Row2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    print('First Matrix is : ')
    for i in range(0,Row1):
        print(matrix1[i])
    print('Second Matrix is : ')
    for i in range(0,Row2):
        print(matrix2[i])
    print('Multiplication of Matrix is : ')
    for i in range(0,Row1):
        print(result[i])
else:
    print('Matrix Multiplication Not Possible')



