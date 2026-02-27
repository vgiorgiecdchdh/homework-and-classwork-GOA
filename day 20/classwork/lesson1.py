# 1) განსხვავება for loop-სა და while loop-ს შორის
# for loop ვიყენებთ როცა ვიცით რამდენჯერ უნდა განმეორდეს ციკლი.
# while loop მუშაობს მანამ, სანამ პირობა მართალია.


# 2) პაროლის შემოწმება while loop-ით
password = "goa123"
user_password = input("შეიყვანე პაროლი: ")

while user_password != password:
    print("პაროლი არასწორია, სცადე თავიდან.")
    user_password = input("შეიყვანე პაროლი: ")

print("პაროლი სწორია!")


# 3) ასაკის შემოწმება
age = int(input("შეიყვანე ასაკი: "))

if age > 18:
    print("age ცვლადი არის მეტი 18 ზე")
else:
    print("age ცვლადი არის ნაკლები 18 ზე")