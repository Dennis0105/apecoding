from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x=1100
y=100
z=1100
mc.player.setTilePos(x,y,z)
time.sleep(5)
mc.player.setTilePos(x+3000,y,z+3000)
time.sleep(5)
mc.player.setTilePos(x+3200,y,z+3100)