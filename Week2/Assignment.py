my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list[1] = 15

my_list.extend([50, 60, 70])

my_list.remove(70)
# print(my_list)

my_list.sort()

# print(my_list)

if 30 in my_list:
    #print the index of 30 in my_list
    print(my_list.index(30))
    
