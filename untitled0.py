from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getPos()
y-=1
mc.setBlocks(x,y,z,x+100,y,z+10,174)
mc.setBlocks(x,y+1,z,x+100,y+1,z+10,169)
mc.setBlocks(x,y+1,z+1,x+100,y+1,z+9,0)
 
