#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge two lists. Multiply all values in the newlist by 2.
#Use the loop to print the data type of the all values in the new list.

#Question 1
oddList = [1,3,5,7,9]
evenList = [0,2,4,6,8]

oddList.extend(evenList)

newList = [x*2 for x in oddList]

for i in newList: #newList elemanlarını yazdırır.
    print(i, end=" ")

print("\n")

for i in newList: #newlist elemanlarının typelarını yazdırır.
    print(type(i), end=" ")
