from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    poz = mc.player.getPos()
    podstopami = mc.getBlock(poz.x, poz.y-1, poz.z)
    mc.postToChat(podstopami)
