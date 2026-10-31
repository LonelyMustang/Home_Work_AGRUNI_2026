import math

a = float(input("შეიყვანეთ გვერდი a: "))
b = float(input("შეიყვანეთ გვერდი b: "))
c = float(input("შეიყანეთ გვერდი c: "))

perimeter = a + b + c
s = perimeter / 2  # half of the perimeter
area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula

print("პერიმეტრი:", perimeter)
print("ფართობი:", round(area, 2))
