from mcpi.minecraft import Minecraft


mc = Minecraft.create()
import random
x,y,z=mc.player.getPos()
y=y-1
mc.setBlock(x,y,z,169)

for i in range(20):
    r=random.choice(range(1,7))
    if r==1:
        mc.setBlocks(x+1,y,z,x+2,y,z,169)
        x=x+2
    if r==2:
        mc.setBlocks(x-1,y,z,x-2,y,z,169)
        x=x-2
    if r==3:
        mc.setBlocks(x,y,z+1,x,y,z+2,169)
        z=z+2
    if r==4:
        mc.setBlocks(x,y,z-1,x,y,z-2,169)
        z-=2
    if r==5:
        mc.setBlocks(x,y+1,z,x,y+2,z,169)
        y+=2
    if r==6:
        mc.setBlocks(x,y-1,z,x,y-2,z,169)
        y-=2





    

    
    

    


    

        