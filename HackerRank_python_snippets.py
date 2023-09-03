#First snippet
#Connect a iterable of integers into a single line 
values = ' '.join(str(v) for v in value_list)

#Intro to Sets
#An overview of how sets function
#learn that sets are used to check membership and eliminate duplicates mainly
#Command for adding all elements of a set together
x = set(1,2,3)
print(sum(x))
>>> 6 

#Symmetric Difference
#Delimiter = inputs are given on one line separated by a character (usually a space)
#.update() adds an iterable object to the set
#Shows some more basic set stuff

#Boilerplate code for creating sets for an input
#set size, create set, set size, create set
size_a = int(input())
a = set(map(int, input().split()))
size_b = int(input())
b = set(map(int, input().split()))

#.symmetric_difference()
#Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.

#Set Mutations
#Similiar to the lists problem, very similiar solution
#Learning different ways not to create a new set, but to change the set itself
#Add given element to set
.update() or |=
#make the set become the instersection between the two sets
.intersection_update() or &=
#Remove the elements found in the given set/iterable
.difference_update() or -=
#make the set become the symmetric difference 
.symmetric_difference_update() or ^=
#To create the command chain, the command "update" is found inside the other chains, what way can I differentiate this command?
#.startswith() string method checks whether the string is at the beginning of string, which solves this problem
elif command.startswith("update") == True:

#Lists 
#Snippet for a long command chain problem
list = []
commands = []
N = int(input())
for x in range(N):
    commands.append(input())

for command in commands:
    if "insert" in command:
        insert_command = command.split()
        list.insert(int(insert_command[1]), int(insert_command[2]))
    elif "append" in command:
        append_command = command.split()
        list.append(int(append_command[1]))
    elif "remove" in command:
        remove_command = command.split()
        list.remove(int(remove_command[1]))
    elif command == "print":
        print(list)
    elif command == "sort":
        list.sort()
    elif command == "pop":
        list.pop()
    elif command == "reverse":
        list.reverse()
    elif command == "sort":
        list.sort()
    elif command == "reverse":
        list.reverse()

#The Captain's Room
#Wants to come up with a creative solution to solve this problem
#Using a set to check membership

#collections.Counter()
#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter
dict(Counter(myList))
Counter(myList).items()
>>> [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
Counter(myList).keys()
Counter(myList).values()


