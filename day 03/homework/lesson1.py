# 1) ასაკი
age = int(input("შეიყვანე ასაკი: "))
if age < 10:
    print("შენ პატარა ხარ")
elif age <= 15:
    print("შენ უკვე დიდდები")
else:
    print("შენ უკვე მოზარდი ხარ")

# 2) ტემპერატურა
temp = int(input("შეიყვანე ტემპერატურა: "))
if temp > 30:
    print("ძალიან ცხელა")
elif temp >= 15:
    print("კარგი ამინდია")
else:
    print("ცივა")

# 3) ლუწი თუ კენტი
num = int(input("შეიყვანე რიცხვი: "))
if num % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")

# 4) პაროლი
password = input("შეიყვანე პაროლი: ")
if password == "1234":
    print("შესვლა წარმატებულია")
else:
    print("არასწორი პაროლი")

# 5) ქულა
score = int(input("შეიყვანე ქულა (0-100): "))
if score >= 90:
    print("შენი შეფასება: A")
elif score >= 70:
    print("შენი შეფასება: B")
elif score >= 50:
    print("შენი შეფასება: C")
else:
    print("შენი შეფასება: F")

# 6) სიჩქარე
speed = int(input("შეიყვანე სიჩქარე: "))
if speed > 120:
    print("სწრაფად მიდიხარ! დაჯარიმდები")
elif speed >= 60:
    print("ნორმალური სიჩქარეა")
else:
    print("ძალიან ნელა მიდიხარ")

# 7) რიცხვების შედარება
a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))
if a > b:
    print("პირველი რიცხვი უფრო დიდია")
elif b > a:
    print("მეორე რიცხვი უფრო დიდია")
else:
    print("ორივე ტოლია")

# 8) თვეები
month = int(input("შეიყვანე თვე (1-12): "))
if 1 <= month <= 3:
    print("ზამთარი")
elif 4 <= month <= 6:
    print("გაზაფხული")
elif 7 <= month <= 9:
    print("ზაფხული")
elif 10 <= month <= 12:
    print("შემოდგომა")
else:
    print("არასწორი თვეა")

# 9) სახელი
name = input("შენი სახელი: ")
if name == "Giorgi" or name == "Gio":
    print("ვაა ტოპ სახელი გაქვს ძმაო")
else:
    print("კარგი სახელი გაქვს")

# 10) ნულზე გაყოფა
x = int(input("შეიყვანე პირველი რიცხვი: "))
y = int(input("შეიყვანე მეორე რიცხვი: "))
if y == 0:
    print("ნულზე გაყოფა არ შეიძლება!")
else:
    print("შედეგი:", x / y)
