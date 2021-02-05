from mcpi.minecraft import Minecraft


mc = Minecraft.create()
import random,time
def pt(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,169)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
for i in range(10):
    x,y,z=mc.player.getPos()
    x=x+i*5
    pt(x,y,z)
        
    


    
   
    





    

    
    

    


    

        