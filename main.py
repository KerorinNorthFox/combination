import permutation_func as pf

n = input("nを入力してください>>")
r = input("rを入力してください>>")

n = int(n)
r = int(r)

pf.permutation(n, r)

keep_R = r
r = 1

for Range_R in range(1, keep_R+1):
    r *= Range_R

fans = ans/r

print(fans)
