# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

true = 0
true += name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
true += name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

love = 0
love += name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love += name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

score = int(str(true) + str(love))
message = f"Your score is {score}"

if score < 10 or score > 90:
    message += ", you go together like coke and mentos"
elif score > 40 and score < 50:
    message += ", you are alright together"

print(message + ".")

