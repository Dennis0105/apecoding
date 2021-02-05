from mcpi.minecraft import Minecraft


mc = Minecraft.create()
import random,time
def pt(x,y,z):
    mc.setBlocks(x+1,y+2,z,x+3,y+5,z+2,169)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,17)
x,y,z=mc.player.getPos()
for i in range(10):
    for c in range(10):
        pt(x+i*c,y+i*c,z+i*c)
    
        
    


    
   
    





    

    
    

    


    

        