#calculator
print "select 1 to enter into loop"
a = 1
choice = 0

while a == 1:
    print "1.Add 2.Sub 3.exit"
    print " "
    choice = input("choose the given options")
    if choice == 1:
        add1 = input("enter the first value")
        add2 = input("enter the second value")
        print add1 + add2
    elif choice == 2:
        sub1 = input("enter the first value")
        sub2 = input("enter the second value")
        print sub1 + sub2
    elif choice == 3:
        a = 10

print "thank you for using calc"
        
