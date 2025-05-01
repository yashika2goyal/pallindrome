#just made it like this for you to check all test case without running it again and again

print("\n===> type 'stop' to terminate the code <===\n")

while True:
    n = input("Enter an integer: ")
    res = False

    if type(n) == str and n.lower() == 'stop':
        break
    elif n.isdigit() == False:
        try:
            if int(n)<0:
                print("Negative integers are never pallindromes")
        except:
            print("Please give a valid integer")
        continue
    elif n.isdigit() == True:
        l = ''
        for i in range(len(n)-1,-1,-1):
            l += n[i]
            if l == n:
                res = True
            else:
                res = False
    else:
        res = False
        
    print(res)


'''explaination:-
This simply works by reversing the string and checking if they are comparable.
It also checks for if the string is not a number, it gives an invalid input message
as it was asked to input and integer'''
