print([''.join(x[0] * (not n % x[1]) for x in [('fizz', 3), ('buzz', 5)]) or n for n in range(1, 51)])
