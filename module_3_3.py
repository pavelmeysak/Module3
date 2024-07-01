def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)


print_params()
print_params(45, 90, 67)
print_params(30)
print_params(b = 25)
print_params('apple', 65)
print_params(c=[1, 2, 3])

values_list = ['Pine', False, 44]
values_dict = {'a': [4, 8, 7], 'b': 500, 'c': 'something in English'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, False]
print_params(*values_list_2, 42)