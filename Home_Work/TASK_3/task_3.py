value = input("შეიყვანეთ რიცხვი").strip()
number = float(value) if value else 0

square = number ** 2

print(int(square) if square == int(square) else square)