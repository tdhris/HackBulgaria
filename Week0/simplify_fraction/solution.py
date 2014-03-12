def GCD(fraction):
	a = fraction[0]
	b = fraction[1]
	r = a%b

	while r != 0:
		a = b
		b = r
		r = a%b

	return b

def simplify_fraction(fraction):
	gcd = GCD(fraction)
	a = fraction[0]
	b = fraction[1]

	while gcd != 1:
		a = fraction[0]//gcd
		b = fraction[1]//gcd
		gcd = GCD((a,b))

	return (a,b)

