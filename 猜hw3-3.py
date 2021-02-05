from mcpi.minecraft import Minecraft


mc = Minecraft.create()
from random import randrange

A=randrange(0,16)
ID=mc.getPlayerEntityId('Dennis0105TW')
while True:
    h=mc.events.pollBlockHits()
    if len(h)>0:
        hit=h[0]
        b=mc.getBlockWithData(hit.pos)
        d=b.data
        if d>A:
            mc.postToChat('猜錯囉---')
        elif d<A:
            mc.postToChat('猜錯囉-/-/-')
        else:
            mc.setBlock(h.pos,169)
            mc.postToTitle(ID,'恭喜-------')
            break
            
