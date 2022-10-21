fruits = ("Mango", "Pear", "Banana", "Apple")

count = 0
for fruit in fruits:
    if (fruit == "Mango"):
        print(str(count) + " I like " + fruit)
    elif (fruit == "Apple"):
        print(str(count) + " I barely like " + fruit)
    else:
        print(str(count) + " I don't like " + fruit)
    count = count + 1

for number in range(10):
    if (number%2 == 0):
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

print(list(enumerate(fruits)))

for index, fruit in enumerate(fruits):
    if (fruit == "Mango"):
        print(str(index) + " I like " + fruit)
    elif (fruit == "Apple"):
        print(str(index) + " I barely like " + fruit)
    else:
        print(str(index) + " I don't like " + fruit)
