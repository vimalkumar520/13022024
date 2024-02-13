#Palindrome Checker:
def Palindrome(st):
    print(st)
    o = ""
    i = len(st) - 1
    while i >= 0:
       o = o + st[i]
       i = i - 1
    print(o)
    if st == o:
        print("The Given String its a Palindrome")
    else:
        print("The Given String its not a Palindrome")

print("####Palindrome Checker####")
s = input("Enter a String to check, its a Palindrome or Not: ")
Palindrome(s)










