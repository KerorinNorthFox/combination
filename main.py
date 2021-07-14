import permutation_module as pf

while True:
    n = input(">>nを入力してください:")
    r = input(">>rを入力してください:")
    
    try:
        n = int(n)
        r = int(r)

        ans = pf.permutation(n, r)
    except:
        print(">>整数を入力してください")
        continue
    
    keep_R = r
    r = 1

    for Range_R in range(1, keep_R+1):
        r *= Range_R

    fans = ans/r
    print(f">>順列:{ans}")
    print(f">>組み合わせ:{fans}")
    
    select = input(">>終了しますか?:[y/n]")
    
    if select == "y":
        print(">>終了")
        break
    elif select == "n":
        continue
    else:
        print(">>入力が間違っています")
        print(">>終了します")
        break
