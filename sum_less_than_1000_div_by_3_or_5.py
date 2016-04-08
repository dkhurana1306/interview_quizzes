import numpy as np
N = 1000 ; Ia = 3; Ib = 5;

A = np.arange(1,N+1)
print sum(A[A%Ia==0]) + sum(A[A%Ib==0]) -  sum(A[A%(Ia*Ib)==0])
