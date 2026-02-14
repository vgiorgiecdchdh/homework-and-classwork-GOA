# 1) განსხვავება while და for შორის (კომენტარებში ახსნა)

# for გამოიყენება როცა ვიცით რამდენჯერ უნდა შესრულდეს
# while გამოიყენება როცა მუშაობს მანამდე, სანამ პირობა True არის


# 2) Password შემოწმება

password = "1234"

user_input = input("Enter password: ")

while user_input != password:
    user_input = input("Wrong password. Try again: ")

print("Access granted!")


# 3) 1 დან 10-მდე რიცხვები

num = 1

while num <= 10:
    print(num)
    num += 1


# 4) 20-მდე მხოლოდ ლუწი რიცხვები

num = 2

while num <= 20:
    print(num)
    num += 2


# 5) რაში გამოიყენება while და for

# while გამოიყენება როცა არ ვიცით რამდენჯერ განმეორდება (მაგ: პაროლი)
# for გამოიყენება როცა ზუსტად ვიცით რაოდენობა (მაგ: range, list)
