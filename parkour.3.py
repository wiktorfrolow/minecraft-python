from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    poz = mc.player.getPos()
    podstopami = mc.getBlock(poz.x, poz.y-1, poz.z)
    if podstopami == 152:
         start = mc.player.getPos()
         mc.postToChat('Gra sie zaczyna')
         while podstopami != 22:
             poz = mc.player.getPos()
             podstopami = mc.getBlock(poz.x, poz.y-1, poz.z)
             if podstopami == 24:
                 mc.player.setPos(start.x, start.y, start.z)
                 mc.postToChat('przegrana')
         mc.postToChat('WYGRANA!')        
