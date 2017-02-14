import classes as cl
import time as t

while True:
    print(cl.Goons.hp)
    t.sleep(1)
    cl.Goons.hp -= cl.Logan.att
    print('"Yaaaah"')
    if cl.Goons.hp <=0:
        print("Logan has slayed the Goons")
        t.sleep(3)
        exit()
    
