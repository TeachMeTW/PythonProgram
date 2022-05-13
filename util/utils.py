def strdollartonum(a:str):
    a = a.replace('$','')
    a = a.replace(',','')
    return int(a)