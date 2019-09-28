#no1
import datetime

n = input('Greetings Love! What is your name? ')
a = int(input(f'And how old are you {n}? ' ))
today = datetime.datetime.now()
future = f"Listen {n}, this may sound a tat strange but you'll be turning 100 in {(100 - a) + today.year}."
print(future)

number = input('Enter any number: ')
for number in future:
    print(future)


# no.2
n = int(input("Let's have some fun! Enter a number: "))
if (n % 2 == 0) and (n % 4 != 0):
    print("I can't-Even!")
elif n % 2 == 1:
    print("You're a very odd chap!")
elif n % 4 == 0:
    print("Yep that's right; You're a fourth generation twat!")
else:
    print("You're sort-a undefined")


# no.3
# 1st question
def less_than_5(a):
    new = []
    for number in a:
        if number > 5:
            ++number
        else:
            new.append(number)
    print(new)
less_than_5([6,3,2,1,4,32,56,23,90,109])

# writing code in one line 
a = [1, 3, 4, 5, 6, 10, 18, 19, 35]
print('')
print(list(filter(lambda n: n < 5, a)))

