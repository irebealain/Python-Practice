
my_list = ["January", "Febeuary", "March", "April"]
print(my_list[2])
my_list.append("May")
print(my_list)
my_list.remove("January")
# set in python: there are are not arranged in order and they have no index.
my_set = {"January", "February", "March"}
for element in my_set:
    print(element)
my_set.add("May")
print(my_set)
my_set.remove("January")