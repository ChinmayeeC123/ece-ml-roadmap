import numpy as np
V= np.array([[1,2,3],[2,1,3],[3,1,2]])
basis=np.linalg.matrix_rank(V)
dimension=V.shape[0]
print("ROW SPACE",basis)
print("COLUMN SPACE",basis)