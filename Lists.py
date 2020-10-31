digits = [1,2,3,4,5]
#min(digits)
#print(min(digits))

print(max(digits))
print(sum(digits))

numbs = list(range(1,6))
print(numbs)

#looping through a list
driver =['joe', 'adam', 'stephen', 'dan']
for man in driver:
    print(man)

# indenting
# always indent the line after a for loop:

player = ['ruth', 'trout', 'mantle']
for batter in player:
    print(batter)

#slicing a list; prints a select section of the list
player = ['ruth', 'trout', 'mantle', 'bonds', 'clemens']
print(player[0:2])
print(player[1:3])
print(player[:3])
print("These are the first two All League team players:")
for all_league in player[:2]:
    print(all_league)
    
#tuple; are similar to lists but cannot be changed. Lists can be changed and manipulated. 
dimension = (100, 300)
dimension(0) = 200
print(dimension)
# wont work because you need to write over a tuple to revise it. You cannot edit a specific part of a tuple

