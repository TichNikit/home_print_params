# №1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params('одна')
print_params(1, 2.4)
print_params(*[1, 2, 3])

print_params(c=[1, 2, 3])
print_params(b=25)
# №2
values_list = ['мне', 0, 'лет']
values_dict = {'a': 'а', 'b': 'мне', 'c': 1.5}

print_params(*values_list)
print_params(**values_dict)
# №3
values_list_2 = [100, '150']
print_params(*values_list_2, 42)
