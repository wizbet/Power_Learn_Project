my_list=[]           #creating of an empty list
numbers = [10,20,30,40]   

my_list.append(numbers)  # Appending of numbers to the empty list

print(my_list)   #output

numbers.insert(1,'15')   #inserting of the number 15 to index/position 2 in the list

print(my_list)     #output

new_num = (50,60,70)

my_list.extend(new_num)   # extending of list with new numbers (50,60,70)

print (my_list)   #output

my_list.pop()  # Remove the last element from my_list.
print(my_list)  #output

# my_list.index(0)
# print(my_list) tried but not working



