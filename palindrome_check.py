#string12 = input("enter a string to check palindrome:  ")
#string12 = string1.casefold()
string12 = "madam"
rev_string = reversed(string12)
if list(string12) == list(rev_string):
    print "the given string is a palindrome"
else:
    print "the given string is not a palindrome"
