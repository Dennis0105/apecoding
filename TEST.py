from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time
x,y,z=mc.player.getPos()
y=y-1
for i in range(15):
    mc.setBlocks(x+1,y,z,x+1,y,z+7,174)
    
    mc.setBlocks(x+1,y+1,z,x+1,y+1,z+7,70)
    mc.setBlocks(x+3,y+1,z,x+13,y+1,z+7,174)
    x+=3
    mc.setBlocks(x,y,z,x,y+100,z+7,0)
    mc.setBlocks(x+3,y+1,z,x+10,z+7,0)
    
    y=y+1
    x=x+2
    