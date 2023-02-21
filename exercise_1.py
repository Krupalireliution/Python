# Exercise 1 :- Write a program to display the statement in two different lines.
print("Exercise 1 :-",'\n', "I am using python" , '\n' , "It's my first assignment")


# Exercise 2 :- Write a program to display the statement.
print("Exercise 2 :-",'\n',"Ohhh!" , '\n', '\t',  "What a python language is!!!", '\n' ,"It's essay!get started")


# Exercise 3 :- write a program to display the pattern.



# Exercise 4 :- write a program to display the pattern.
n = 5
for i in range(0,n):
    for j in range(0,n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print("0",end=" ")
        else:
            print(" " , end=" ")
    print()
