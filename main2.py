#activity3
list = [45 , 67 , 89 , 23 , 0]
list.sort()
print(list)
print("The smallest number is" , list[0])
print("The largest number is " , list[-1])
count = 0
for i in list:
    count +=i
    print(count)
print(count , "hello")