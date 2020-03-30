from random import SystemRandom

rand = SystemRandom()

class Alice():
	def __init__(self,g,p,n):
		self.private_key = rand.getrandbits(n) ## x
		self.public_key = pow(g,self.private_key)%p ## g^x % p
		self.g = g

	def send_random(self,p,n):
		self.r = rand.getrandbits(n) ## r
		return pow(g,self.r)%p ## g ^ r % p

	def receive_c(self,p,n,c):
		self.z = c*self.private_key + self.r ## cx+r


class Bob():
	def __init__(self,g,y,p):
		self.public_key = y
		self.g = g

	def receive_random(self,m1):
		self.m1 = m1 ## g^x %p

	def send_c(self,n,p):
		return rand.getrandbits(n)%p

	def verify(self,g,z,c,p):
		X = pow(g,z)%p
		Y = ((pow(self.public_key,c)%p)*(self.m1%p))%p

		if(X == Y):
			print("Yes")
		else:
			print("NO")



p = 17
g = 3
n = 5

M = rand.getrandbits(n)

A = Alice(g,p,n)
B = Bob(g,A.public_key,p)

print(A.private_key)

m1 = A.send_random(p,n)
B.receive_random(m1)
c = B.send_c(n,p)
A.receive_c(p,n,c)
B.verify(g,A.z,c,p)
