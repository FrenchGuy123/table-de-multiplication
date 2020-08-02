import time
print("table de multiplication par emilien")
a = input("combien de chiffre(s) par de table ? ")
b = input("nombre de table ? ")
e= input("quelle table ? table (a)datition, table de (s)oustraction, table de (m)ultiplication, table de (X)OR, ou table de (mo)dulo ? ")
#if not e == "a" or not e == "s" or not e == "m" or not e == "d" or not e == "mo":
if not e == "a":
    if not e == "s":
        if not e == "m":
            if not e == "mo":
                if not e == "x":
                    if not e == "X":
                       print(e)
                       print ("sérieusement. relance le programme..")
                       while True:
                           pass
if e == "X":
    e = "x"
c = time.time()
try:
     a = int(a)
     b = int(b)
except:
    print("erreur: veulliez relancer ce programme.")
    while 1:
        pass
for x in range (1,(b+1)):
    print("table des",x)
    for y in range (1,(a+1)):
        if e == "a":
            print(x,"+",y,"=",x+y)
        elif e == "s":
            print(x,"-",y,"=",x-y)
        elif e == "m":
            print(x,"*",y,"=",x*y)
        elif e == "mo":
            print(x,"modulo",y,"=",x%y)
        elif e == "x":
            print(x,"XOR",y,"=",x^y)
d = time.time()
print("voila !")
print("seconde(s) écoulé:",(d-c))
