import numpy as np
import numpy.linalg as la
import scipy.linalg as spla

A = np.array([[1,1,2],
     [1,2,1],
     [2,1,1],
     [2,2,1],])

y = np.array([[1],
     [-1],
     [1],
     [-1]])

m = 4
n = 3

Q, R = la.qr(A)
Q2, R2 = la.qr(A, mode="complete")
x2 = spla.solve_triangular(R[:n], Q.T[:n].dot(y), lower=False)

x_exp = np.array([[ 0.6       ],
       [-1.4       ],
       [ 0.93]])

norm = la.norm(A.dot(x_exp)-y)