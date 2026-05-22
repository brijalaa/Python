import sys
spam = ['apples', 'bananas', 'tofu', 'cats']
def CommaCode(lst):
    comma = ''
    if not lst:
        sys.exit()
    for i in lst:
        if i == lst[0]:
            comma = i
        elif i != lst[-1]:
            comma = comma + ', '+ i
        else:
            comma = comma + ' and ' + i
    return comma
print(CommaCode(spam))
