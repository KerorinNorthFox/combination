import permutation_func as pf

n = input()
r = input()

pf.permutation(n, r)

keep_R = r
r = 1

for Range_R in range(0, keep_R):
