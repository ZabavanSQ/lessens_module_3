
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(a = 25)
print_params(c = [1, 2,3])
print_params()

values_list_2=[54.32, (12, 'Roman',31.12)]
print_params(*values_list_2, 42)

values_dict={'a': 123, 'b':'вертикаль', 'c': 12.34 }

print_params(**values_dict)