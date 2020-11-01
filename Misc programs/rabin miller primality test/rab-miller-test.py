from random import randrange

def is_prime(p, k=20):
	phi = int(p - 1)
	d = phi
	r = 0

	while d % 2 == 0:
		r += 1
		d /= 2

	for i in range(k):
		a = int(randrange(2, p-2))
		exp = pow(a, int(d), p)

		if exp == 1 or exp == p-1:
			continue

		for k in range(r - 1):
			exp = pow(exp, 2, p)

			if exp == 1:
				return False

			if exp == p - 1:
				break 

		else:
			return False

	return True

print(is_prime(9746347772161))
