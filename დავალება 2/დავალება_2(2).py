n = int(input("შეიყვანეთ რიცხვი: "))

if n < 1 or n > 1000:
    print("რიცხვი აუცილებლად უნდა იყოს 1 დან 1000 მდე.")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
