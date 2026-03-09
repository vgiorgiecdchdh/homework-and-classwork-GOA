name = input("შეიყვანე სახელი: ")

vowels = "აეიოუ"

found = False

for i in name:
    if i in vowels:
        print(i)
        found = True

if found == False:
    print("არ არის ხმოვნები")