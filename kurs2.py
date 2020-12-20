from mcpi import minecraft
from mcpi import block
mc = minecraft.Minecraft.create()
pozycja_gracza = mc.player.getTilePos()
mc.postToChat(pozycja_gracza)
mc.setBlock(pozycja_gracza.x, 
            pozycja_gracza.y, 
            pozycja_gracza.z, 
                 block.WOOD.id)
