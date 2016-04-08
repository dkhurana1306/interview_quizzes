import numpy as np

def ispalindrome(N):
	N = int(N)
	return str(N) == str(N)[::-1]



A = np.arange(100,1000)
B = np.zeros(A.size**2)

k = 0 
for i in range(A.size):
	for j in range(A.size):
		B[k] = int(A[i]*A[j])
		k = k+1

index = np.zeros(B.size)
for i in range(B.size):
	index[i] = ispalindrome(B[i])

print int(max(B[index == 1]))
