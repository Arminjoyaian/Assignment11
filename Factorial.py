def f(x):
    if x == 1 or x == 0:
         print(1) 
    else:
        print(f(x - 1) * x)

number = int(input("enter numebr: "))
o = f(number)
print(0)