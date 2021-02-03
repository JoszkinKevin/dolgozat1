"""2. Írjon programot szavak.py néven! A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a
hosszabb!"""

szo1 = input()
szo2 = input()

if len(szo1) < len(szo2):
    print(szo1)
else:
    print(szo2)