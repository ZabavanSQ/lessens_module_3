data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
set_c = []


def suum(x):
    set_a = 0
    set_b = []
    for i in range(len(x)):
        set_a = 0
        if isinstance(x[i], str):
            set_a = len(x[i])
        if isinstance(x[i], int):
            set_a = int(x[i])
        if isinstance(x[i], list):
            set_b = list(x[i])
            suum(set_b)
        if isinstance(x[i], set):
            set_b = list(x[i])
            suum(set_b)
        if isinstance(x[i], tuple):
            set_b = list(x[i])
            suum(set_b)
        if isinstance(x[i], dict):
            set_b = list(dict(x[i]).items())
            suum(set_b)
        if set_a > 0:
            set_c.append(set_a)
        else:
            continue
    
suum(data_structure)

print(sum(set_c))