from random import SystemRandom
from Crypto.Util import number
import gensafeprime

rand = SystemRandom()

def Hashing(x,y,k):
	global g,p
	h = pow(g,x+k*y,p)
	return h


class Alice():
	def __init__(self,g,p,n):
		self.private_key = rand.getrandbits(n) ## x
		self.public_key = pow(g,self.private_key,p) ## g^x % p
		self.g = g

	def Signing(self,p,n):
		self.r = rand.getrandbits(n) ## r
		t = pow(self.g,self.r,p) ## g ^ r % p
		c = Hashing(p,self.g,self.public_key) ## H(p,g,y)
		z = c*self.private_key+self.r ## x*(H(p,g,y))+r

		return (t,z)

class Bob():
	def __init__(self,g,y,p):
		self.public_key = y
		self.g = g

	def Verifying(self,p,z,t):
		c = Hashing(p,self.g,self.public_key)
		X = pow(self.g,z,p)
		Y = ((pow(self.public_key,c,p))*(t%p))%p

		if X == Y:
			return True
		else:
			return False







if __name__ == "__main__":
	n = 256
	print("Length of prime "+str(n))
	p = gensafeprime.generate(n)
	print("Prime p = "+str(p))
	q = (p-1)//2

	t = 1
	while t == 1:
		h = number.getRandomRange(2,p-2)
		t = pow(h,2,p)

	g = h

	print("Generator g = "+str(g))

	M = rand.getrandbits(n)

	print("Message m = "+str(M))

	A = Alice(g,p,n)
	B = Bob(g,A.public_key,p)

	t,z = A.Signing(p,n)
	print(B.Verifying(p,z,t))


	# print("x = "+str(A.private_key))
# print("y = "+str(A.public_key))
