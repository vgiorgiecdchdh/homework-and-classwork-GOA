# Input — ეს არის ის, რასაც მომხმარებელი შეჰყავს პროგრამაში. მაგალითად, როცა ვწერთ სახელებს, რიცხვებს და სხვა инфოს.
# Output — ეს არის ის, რასაც პროგრამა ბეჭდავს ekraanze — პასუხები, შეტყობინებები, შედეგები.

# მოკლედ:

# input = შეყვანა

# output = გამოტანა




#------------------------------------------------------------------------------------------------------------------------------------------------------



# int — მთელი რიცხვი. მაგ: 5, 10, 999

# str — ტექსტი. მაგ: "Giorgi", "Hello", "123" (რიცხვი ბრჭყალებში = ტექსტია)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------






name = input("Enter your name: ")
surname = input("Enter your surname: ")

if len(name) > 8:
    print("try again")
else:
    password = input("Create password: ")
    repeat = input("Repeat password: ")

    if password == repeat:
        print("Registration complete!")
    else:
        print("Passwords don't match")







#---------------------------------------------------------------------------------------------------------------------------------------------------------------





numbers = [5, 1, 9, 5]

numbers.append(7)       # ბოლოში ამატებს
numbers.insert(0, 10)   # ადგილზე ჩასმა
numbers.remove(5)       # პირველი 5-ის წაშლა
numbers.pop()           # ბოლო ელემენტის ამოგდება
numbers.sort()          # დალაგება
numbers.reverse()       # შებრუნება
count_five = numbers.count(5)   # რამდენი 5-ია
index_one = numbers.index(1)    # 1-ის ინდექსი
copy_list = numbers.copy()      # ასლი
numbers.clear()         # სრულად გაწმენდა

print(copy_list)
print("Count of 5:", count_five)
print("Index of 1:", index_one)




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------







secret = 7

guess = int(input("Guess the number: "))

if guess == secret:
    print("You guessed!")
else:
    print("Wrong!")

