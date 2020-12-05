from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    poz = mc.player.getPos()
    podstopami = mc.getBlock(poz.x, poz.y-1, poz.z)

    if podstopami == 2:
        mc.postToChat('Stoisz na trawie')
    else:
        mc.postToChat('nie stoisz na trawie')
