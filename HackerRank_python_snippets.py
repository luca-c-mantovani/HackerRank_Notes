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

