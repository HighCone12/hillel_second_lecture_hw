user_name: str = input('What is your name?\t')

user_age: int = int(input('Fill up your age\t'))

if user_age == 16:
    print('Dear ' + user_name + ' need to wait one year.')

elif 70 < user_age < 90:
    print('You are lucky ' + user_name)

elif user_age > 121:
    print('You are not real ' + user_name)

elif user_age > 16:
    print('Welcome ' + user_name)

else:
    print("I'm sorry " + user_name + " you are too young")
