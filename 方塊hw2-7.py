from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
a=0
while a<20:
    mc.setBlocks(x,y-1,z,x+25,y-25,z,19)
    a=a+1
    z=z+3
    

    
    

    


    

        