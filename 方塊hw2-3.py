from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
x,y,z,=mc.player.getPos()
mc.setBlocks(x,y,z,x+5,y+5,z+5,57)
mc.setBlocks(x,y,z,x+4,y+4,z+4,57)


    

        