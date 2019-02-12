while True:
    a=input("первое число: ")
    b=input("второе число: ")
    c=input("действие: ")
    if c =='/':
        if int(b) != 0:
            print(int(a) / int(b))
        else:
            print("Деление на ноль")
    if c =='+':
            print(int(a) + int(b))
    if c =='-':
            print(int(a) - int(b))
    if c =='*':
            print(int(a) * int(b))
            
