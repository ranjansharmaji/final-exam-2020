import numpy as np
import numpy.linalg as nl
A=np.array([[2,1],[1,0],[0,1]])
F=nl.eigvals(np.dot(np.transpose(A),A))

#As we know singuler values of matrix is squreroot of eigen values of A^t*A
result1=np.sqrt(F)
print("singuler value of 1st matrix",result1)

B=np.array([[1,1,0],[1,0,1],[0,1,1]])
J=nl.eigvals(np.dot(np.transpose(B),B))
result2=np.sqrt(J)
print("singuler value of 2nd matrix",result2)
