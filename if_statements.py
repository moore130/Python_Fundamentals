# If statements examine a set of conditions and what action to take based on those conditions.

presidents = ['lincoln', 'bush', 'clinton', 'obama']

for person in presidents:
    if person == 'obama':
        print(person)
    else:
        print('No one by that name sorry')

for person in presidents:
    if person == 'bush':
        print(person)
    else:
        print('These are my favorite!')

# At the heart of an if statement is a true false statement. 
president = 'obama' # This sets the variable president equal to obama.
president == 'obama' # This checks whether the value of president if obama ...
# When the value is anything other than obama the conditional will be false.

# Not =!
requested_topping = 'Olives'

if requested_topping != 'salami':
    print('Hold the salami!')
# If the values dont match the statment is true and the if statement will be printed.

# Testing to see if two numbers are not equal. 
answer = 19

if answer != 69:
    print("That answer is wrong!. Try again.")

# of conditinons are false only if BOTH conditions fail. If one passes the 
# test then it will return true. AND statemetns both conditions need to be true.


