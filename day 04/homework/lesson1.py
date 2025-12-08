# 1) სიები
cars = ["BMW", "Audi", "Mercedes"]
cars.append("Toyota")
cars.pop()

print(cars)


#cars1 = ["toyota","Ford"]
#cars1.reverse()
# cars1.sort()
# cars1.remove()
# cars1.insert(1,"bmw")
# cars1.count("toyota")
# cars1.extend(cars)
# cars1.index("Ford")
# cars1.copy()

# 2) მომხმარებლის მონაცემები
# name = input("შეიყვანე შენი სახელი: ")
# surname = input("შეიყვანე შენი გვარი: ")
# age = int(input("რამდენი წლის ხარ?: "))
# city = input("სად ცხოვრობ?: ")

# print("\nგამარჯობა " , name   , surname , ", შენ ხარ " , age ," წლის და ცხოვრობ ", city , ".\n")


# 3) Guess game
# secret = 5
# guess = int(input("გამოიცანი რიცხვი 1-დან 10-მდე: "))

# if guess == secret:
#     print("შენ გამოიცანი!")
# elif guess != secret:
#     print("შენ ვერ გამოიცანი!")
# else:
#     print("Error")


# 4) ქულები
score = int(input("\nშეიყვანე შენი ქულაc: "))

if score >= 90:
    print("ჩააბარე!🔥")
elif score > 70 and score < 80:
    print("ჩააბარე!👌")
elif score > 60 and score < 70:
    print("იმეცადინე!📚")
elif score < 50:
    print("ვერ ჩააბარე ❌")
else:
    print("Error")
