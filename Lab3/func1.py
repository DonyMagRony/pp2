#Task 1
def task1():
    global grams
    grams=int(input("write grams:"))
    print(f'{28.3495231 * grams:.2f}')
#Task 2
def task2():
    global temp
    temp=int(input("write temp:"))
    print (f'{5*(temp-32)/9:.2f}')
    

#Task3
def task3():
    for i in range(1,35):
        if (i*4+(35-i)*2) == 94:
            break

    b=35-i
    print (f"{i} rabbits")
    print(f"{b} chikens")

# Task4
def task4():
    global nums
    nums = [int(x) for x in input().split()]
    nums=list(filter(lambda x: x!=1,nums))
    is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
    primes=list(filter(is_prime,nums))
    print(primes)
# Task5
import itertools
def task5():
    global string
    string=list(input("enter").split(" "))
    permutat=list(itertools.permutations(string))
    print(permutat)
#Task 6
def task6():
    global string
    string=list(input("enter").split(" "))
    string.reverse()
    for i in string:
        print(i,end=(" ")) 
#Task 7
def task7():
    global nums
    nums = [int(x) for x in input().split()]
    for i in nums:
        if i==3:
            if nums[nums.index(i)+1]==3:
                print(True)
                exit(0)
    print(False)
    

#Task 8
def task8():
    global nums
    nums = [int(x) for x in input().split()]
    for i in nums:
        if i==0:
            if nums[nums.index(i)+1]==0:
                if nums[nums.index(i)+2]==7:
                   print(True)
                   exit(0)
    print(False)

#Task 9
def task9():
    global rad
    rad=int(input())
    print(4/3*pow(rad,3))
#Task 10
def task10():
    global nums
    nums = [int(x) for x in input().split()]
    x = []
    for a in nums:#
        if a not in x:
            x.append(a)
    print(x)
#Task11
def task11():
    string=input("enter word:")
    left = 0
    right = len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            print(False)
        left += 1
        right -= 1
    print(True)
#Task 12
def task12(  ):
    items=[int(x) for x in input().split()]
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
#Task13
import random
def task13():
    global name,number,guess,count
    name = input("Hello! What is your name?\n")
    print ("Well, %s, I am thinking of a number between 1 and 20." % name)
    number = random.randint(1, 20)
    guess = int(input("Take a guess.\n"))
    count = 1
    while guess != number:
        if guess < number:
            print ("/nYour guess is too low.")
        elif guess > number:
            print ("/nYour guess is too high.")
        guess = int(input("Take a guess.\n"))
        count += 1
    print ("Good job, %s! You guessed my number in %d guesses!" % (name, count))
