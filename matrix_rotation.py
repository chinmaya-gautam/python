#!/usr/bin/python

'''
a simple code to rotate a nxn matrix 90* anti-clockwise
'''

N = input() #dimension of matrix
matrix = [ [] for y in range(N)]

def print_matrix(matrix):
    print ''
    for i,c in enumerate(matrix):
        for j, d in enumerate(c):
            print d,
        print ''
    print ''

def rotate_matrix(matrix):
    mid = len(matrix)/2
    m_len = len(matrix)-1
    for i in range(mid):
        for j in range(i,m_len -i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][m_len-i]
            matrix[j][m_len-i]=matrix[m_len-i][m_len-j]
            matrix[m_len-i][m_len-j]=matrix[m_len-j][i]
            matrix[m_len-j][i]=temp
while(N):
    N-=1
    matrix[N].extend(raw_input().split(' '))
    
matrix.reverse()
rotate_matrix(matrix)
print_matrix(matrix)
