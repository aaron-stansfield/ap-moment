import random
Fsharp = ["f#","g#","a#","c#","d#","e#"]
C = ["c","d","e","f","g","a","b"]
D = ["d","e","f#","g","a","b","c#"]
E = ["e","f#","g#","a","b","c#","d#"]
F = ["f","g","a","a#","c","d","e"]
G = ["g","a","b","c","d","e","f"]
A = ["a","b","c#","d#","e","f#"]
B = ["b","c#","d#","e","f","f#"]
mus = ["","","","","",""]

def keycheck():
    global note
    global ukey
    ukey = str(input("key: "))
    ukey = ukey.lower()
    if ukey == "c":
        note = C
    elif ukey == "d":
        note = D
    elif ukey == "e":
        note = E
    elif ukey == "f":
        note = F
    elif ukey == "g":
        note = G
    elif ukey == "a":
        note = A
    elif ukey == "b":
        note = B
    else:
        keycheck()



def gen(l,key):
    for x in range(l):
        np = random.randint(0,5)
        n = note[np]
        print(n)
        try:
            mus.append(n)
        except:
            print("something when wrong")


mput = int(input("length: "))
keycheck()
gen(mput, ukey)
