from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z,=mc.player.getPos()
    mc.postToChat('你在x:'+str(x)+'y:'+str(y)+'z:'+str(z))
    