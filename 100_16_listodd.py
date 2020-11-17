# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.
# Input  : 1,2,3,4,5,6,7,8,9
# Output : 1,3,5,7,9

listall = map(int, input().split(','))
odds = [str(i) for i in listall if i%2!=0]
print(','.join(odds))
