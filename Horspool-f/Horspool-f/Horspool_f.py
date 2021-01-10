from itertools import product
from string import ascii_lowercase



def horspool(text,pattern):
    n = len(text)
    m = len(pattern)
    count = 0
    for l in pattern:
        count = count + 1
    found = 0
    i = 0


    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j = j - 1

        if j < 0:
            found = found + 1

        i = i + m - 1

        occurancy = m - 2

        while occurancy >= 0:
            if pattern[occurancy] == text[i]:
                break
            occurancy = occurancy - 1

        i = i - occurancy
    print('Per Textin "{}" gjej patternin {}'.format(text,pattern))
    print('Patterni u gjet {} here'.format(found))

data = {
    'asdfasdaaa':'dfa',
    'Sot kemi inteligjence artificiale':'inteli',
    'une jam qlirimi':'qlirimi',
    'Ne oren e fundit kemi ushtruar horspool':'horspooli',
    'qfar je duke bere':'duke',
    'dizajni i algoritmeve te avancuara':'i',
    'Baza e te dhenave ne databaze':'ava'
}


for x in data:
    horspool(x,data[x])


