from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

Pos=mc.player.getPos()
x=Pos.x
y=Pos.y
z=Pos.z

time.sleep(10)
mc.player.setPos(x,y,z)