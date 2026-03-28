# 1) შედარებითი ოპერატორები (comparison operators)

# == (უდრის)
print(5 == 5)
print(3 == 4)
print("a" == "a")
print(10 == 10)
print(7 == 8)

# != (არ უდრის)
print(5 != 3)
print(4 != 4)
print("a" != "b")
print(9 != 1)
print(2 != 2)

# > (მეტია)
print(5 > 3)
print(2 > 7)
print(10 > 1)
print(6 > 6)
print(8 > 4)

# < (ნაკლებია)
print(3 < 5)
print(7 < 2)
print(1 < 10)
print(6 < 6)
print(4 < 8)

# >= (მეტია ან ტოლია)
print(5 >= 5)
print(6 >= 3)
print(2 >= 7)
print(9 >= 9)
print(1 >= 0)

# <= (ნაკლებია ან ტოლია)
print(3 <= 5)
print(7 <= 2)
print(4 <= 4)
print(1 <= 9)
print(6 <= 6)


# 2) Logical operators (ლოგიკური ოპერატორები)
# Logical operators გამოიყენება რამდენიმე პირობის ერთად შესამოწმებლად

# and — აბრუნებს True-ს თუ ორივე პირობა სწორია
# or — აბრუნებს True-ს თუ לפחות ერთი პირობა სწორია
# not — აბრუნებს საპირისპირო მნიშვნელობას (True -> False, False -> True)


# 3) მაგალითები logical operator-ებზე

# and
print(5 > 3 and 10 > 7)
print(2 > 5 and 1 < 3)
print(4 == 4 and 6 > 2)

# or
print(5 > 3 or 2 > 10)
print(1 > 5 or 3 < 4)
print(7 == 8 or 9 > 3)

# not
print(not(5 > 3))
print(not(2 > 7))
print(not(4 == 4))


# 4) რიცხვის შედარება
num = int(input("შეიყვანე რიცხვი: "))
my_num = 10

print(num > my_num)


# 5) სახელის შედარება
name = input("შეიყვანე შენი სახელი: ")
my_name = "Giorgi"

print(name == my_name)


# 6) ასაკის შემოწმება
age = int(input("შეიყვანე შენი ასაკი: "))

print(age > 18)