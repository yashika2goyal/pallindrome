#just made it like this for you to check all test case without running it again and again

print("\n===> type 'stop' to terminate the code <===\n")

while True:
    n = input("Enter an integer: ")
    res = False

    if type(n) == str and n.lower() == 'stop':
        break
    elif n.isdigit() == False:
        print("Please give a valid integer")
        continue
    elif n == n[::-1]:
        res = True
    else:
        res = False
        
    print(res)


'''explaination:-
This simply works by reversing the string and checking if they are comparable.
It also checks for if the string is not a number, it gives an invalid input message
as it was asked to input and integer'''
