# 1) რაში გვეხმარება if / else
# if და else გვეხმარება შევამოწმოთ პირობა.
# თუ პირობა მართალია შესრულდება if-ის კოდი,
# სხვა შემთხვევაში შესრულდება else-ის კოდი.


# 2) შევამოწმოთ რიცხვი მეტია თუ ნაკლები 0-ზე
num = int(input("შეიყვანე რიცხვი: "))

if num > 0:
    print("num არის მეტი 0 ზე")
else:
    print("num არის ნაკლები 0 ზე")


# 3) პაროლის შემოწმება
password = input("შეიყვანე პაროლი: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


# 4) 1-დან შეყვანილ რიცხვამდე ჯამის გამოთვლა
number = int(input("შეიყვანე რიცხვი: "))
total = 0

for i in range(1, number + 1):
    total += i

print("ჯამი არის:", total)