from mcpi.minecraft import Minecraft


mc = Minecraft.create()
import random,time
x,y,z=mc.player.getPos()
 

for i in range(10):
  
    
    for j in range(10):
        
        c=random.randrange(0,16)
        mc.setBlock(x+j,y,z+i,35,c)
       





    

    
    

    


    

        