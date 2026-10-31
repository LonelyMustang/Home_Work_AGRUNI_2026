while True:
    text = input("ჩაწერეთ წელიწადი : ").strip()
    if text.isdigit() and int(text) > 0:
        year = int(text)
        break
    print("შეყვანილი რიცხვი არასწორია, აუცილებლად ჩაწერეთ ნატურალური რიცხვი.")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "წელიწადი ნაკიანია.")
else:
    print(year, "წელიწადი ნაკიანი არ არის.")
