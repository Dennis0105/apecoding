from mcpi.minecraft import Minecraft


mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
a=input('你是誰')
mc.postToChat('Hello '+a+'今天天氣真好')

mc.setBlocks(x+2,y+4,z+2,x-2,y-2,z-2,169)
mc.setBlocks(x+1,y+3,z+1,x-1,y-1,z-1,0)
mc.setBlocks(x+2,y,z,x+2,y-1,z,0)
mc.setBlocks(x+2,y+2,z+2,x-2,y+2,z-2,169)
早安你好






    

    
    

    


    

        