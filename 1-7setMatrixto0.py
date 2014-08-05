matrix = [[0,1,2],[3,4,5],[6,7,8]]
matrix2 = [row[:] for row in matrix]
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[i])):
        if matrix[i][j] == 0:
            for p in range(0,len(matrix2)):
                matrix2[p][j] = 0
            for q in range(0,len(matrix2[i])):
                matrix2[i][q] = 0
                
matrix = matrix2
print(matrix)
            
