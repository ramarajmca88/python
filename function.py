def myfun():
    print "My first function"

def myfun_with_args(name , company):
    print "Hello %s , welcome to %s" % (name , company)

def add(a, b):
    return a + b

myfun()
myfun_with_args("Ramaraj" , "Accenture")
c = add(3,3)
print c
