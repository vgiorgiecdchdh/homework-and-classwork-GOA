score = int(input("შეიყვანე ქულა: "))

if score == 100:
    print("A Group")
elif score >= 80 and score <= 99:
    print("B Group")
elif score >= 40 and score <= 70:
    print("C Group")
else:
    print("D Group")