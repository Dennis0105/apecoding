from mcpi.minecraft import Minecraft


mc = Minecraft.create()
while True:
    h=mc.events.pollBlockHits()
    if len(h)>0:
        hit=h[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,57)






    

    
    

    


    

        