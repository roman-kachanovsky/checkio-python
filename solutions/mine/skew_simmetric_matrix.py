""" --- Skew-simmetric matrix --- Elementary

In mathematics, particularly in linear algebra, a skew-symmetric matrix
(also known as an antisymmetric or antimetric) is a square matrix A whose
transpose is also its negative. This means it satisfies the equation A = -A^T.
If the entry in the i-th row and j-th column is aij, i.e. A = (a[i][j]) then
the symmetric condition becomes a[i][j] = -a[j][i].

You should determine whether the specified square matrix
is skew-symmetric or not.

Input:              A square matrix as a list of lists with integers.
Output:             If the matrix is skew-symmetric or not as a boolean.
How it is used:     Skew-symmetric matrices can be useful for the cross
                    product, an operation in mathematics used in
                    the calculation of movement of forces. Matrixes
                    are basis for the linear algebra and vector graphics.
Precondition:       0 < N < 5

"""


def my_solution(m):
    return all(m[i][j] == -m[j][i] for i in xrange(len(m)) for j in xrange(i + 1))


makoto_yamagata_solution = lambda m: (m == [[-x for x in row] for row in list(zip(*m))])


def gyahun_dash_solution(matrix):
    return matrix == [[-element for element in row] for row in zip(*matrix)]
