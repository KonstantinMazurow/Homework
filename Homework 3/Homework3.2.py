# First way
my_dict_1 = {
    "Oranges": 114.99, 
    "Candy": 280.00,
    "Book": 199.99,
    "Juice": 119.99,
    "Trout": 399.99
    }
print(my_dict_1)
dct_1 = list(my_dict_1.items())
my_dict_1.clear()
dct_1[0], dct_1[-1] = dct_1[-1], dct_1[0]
dct_1.pop(1)
my_dict_1.update(dct_1)
my_dict_1["Pen"] = 50.00
print(my_dict_1)

# Second way
import collections
my_dict_2 = {
    "Oranges": 114.99, 
    "Candy": 280.00,
    "Book": 199.99,
    "Juice": 119.99,
    "Trout": 399.99
    }
print(my_dict_2)
dict_2 = collections.OrderedDict(my_dict_2)
first_element_of_dict_2 = list(dict_2.items())[0]
last_element_of_dict_2 = list(dict_2.items())[-1]
second_element_of_dict_2 = list(dict_2.items())[1]
dict_2.move_to_end(key = first_element_of_dict_2[0])
dict_2.move_to_end(key = last_element_of_dict_2[0], last=False)
del dict_2[second_element_of_dict_2[0]]
dict_2['Pen'] = 50.00
my_dict_2.clear()
my_dict_2 |= dict_2
print(my_dict_2)

