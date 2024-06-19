#Humpyang Game
from random import randint

P1 = input("Your Choice: ")
c2 = randint(0,1)
c3 = randint(0,1)

hayang = 0
kulob = 1

if P1 == kulob:
    print("KULOB")
elif P1 == hayang:
    print("HAYANG")
if c2 == 1:
    print("C2:KULOB")
elif c2 == 0:
    print("C2:HAYANG")
if c3 == 1:
    print("C3:KULOB")
elif c3 == 0:
    print("C3:HAYANG")
    


if P1 == 1 and c2 == 0 and c3 == 1 or P1 == 1 and c2 == 1 and c3 == 0 :
    print("daug ka")
elif P1 == 1 and c2 == 1 and c3 == 0 or P1 == 1 and c2 == 1 and c3 == 1:
    print("daug ka!")
elif P1 == 0 and c2 == 1 and c3 == 1 or P1 == 0 and c2 == 0 and c3 == 0:
    print("daug ka")
else:
    print("LAHI hawa")