from mcpi.minecraft import Minecraft


mc = Minecraft.create()
import random,time
a=[]
b=[]
c=[]
for i in range(1,4):
    a.append(1*i)
for i in range(1,4):
    b.append(2*i)
for i in range(1,4):
    c.append(3*1)
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,8,str(a),str(b),str(c))


    
        
    


    
   
    





    

    
    

    


    

        