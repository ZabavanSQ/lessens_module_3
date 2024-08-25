calls = 0

def count_calls():
    global calls
    calls = calls + 1
def string_info(stng):
    rez = []
    rez.append(len(stng))
    rez.append(stng.upper())
    rez.append(stng.lower())
    print(tuple(rez))
    count_calls()
def  is_contains(a, list_a):
    a = a.lower()
    list_b = []
    for i in range(0, len(list_a)):
        list_b.append(list_a[i].lower())
    b = True
    if a in list_b:
        b = True
    else:
        b = False
    print(b)
    count_calls()

string_info('Urban')
string_info('Ronan')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
