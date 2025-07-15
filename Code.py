import random

# creates an array with the people you have
people = input("Which people will join this group: ")
group = people.split()

# creates a condition to remove the number (they are strings)
nonIntGroup = []
for a in group:
    if not a.isdigit():
        nonIntGroup.append(a)       

# how many people will join this group
desiredNum = int(input("How many people will be joining this group: "))

# creates a condition where the desired number is higher than the length of group, which will start over with the question
while desiredNum > len(nonIntGroup):
    print("Try again")
    desiredNum = int(input("How many people will be joining this group: "))

# create a new list but containing the desired amount of people in the group, no repeating person
group = []
b = 0
while b < desiredNum:
    randNum = random.randint(0, len(nonIntGroup)-1)
    x = nonIntGroup.pop(randNum)
    group.append(x)
    b += 1

# display the finishing results
print(group)
