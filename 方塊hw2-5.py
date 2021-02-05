from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

while True:
    x,y,z,=mc.player.getPos()
    a=random.randrange(0,9)
    mc.setBlock(x,y,z,38,a)
    time.sleep(0.1)
    


    

        