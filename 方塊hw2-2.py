from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
Block=random.randrange(0,150) 
x,y,z,=mc.player.getPos()
mc.setBlock(x+1,y,z-1,57)

mc.setBlocks(x,y,z,x+10,y+10,z+10,Block)        