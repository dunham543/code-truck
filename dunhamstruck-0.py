# Base project format.
# Documentation https://github.com/raspberrypilearning/getting-started-with-minecraft-pi/blob/master/worksheet.md
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
    ip = "192.168.7.226"
    #ip = "127.0.0.1"
    mc = Minecraft.create(ip, 4711)
    #mc.setting("world_immutable",True)
    #x, y, z = mc.player.getPos()        
    return mc
    
def clearAir(mc,x,y,z):
    mc.setBlocks(x-10,y-5,z-20,x+10,y+20,z+20,0)
    mc.setBlocks(-128,-3,-128,128,64,128,0)
    for k in range (-10,0,1):
        m = 2
        if k < -5:
            m = 7
        if k > -3 and k < -1 :
            m = 3
        mc.setBlocks(-128,k,-128,127,k,127,m)
    mc.postToChat("World Cleared!!!!")
    
def truck(mc,x,y,z):
  print("xyz",x,y,z)
  mc.setBlocks(x-20,y-5,z-20,x+20,y+50,z+20,0)
  X = ["            11111111       ",
       "            51555515       ",
       "            11555515       ",
       "  111111111111111111111111 ",
       "  111111111112111111111111 ",
       " 31111122211111111122211113",
       "       222         222     "]
     # "0123456789ABCDEF0123456789A"
  #print(X)
  for k in range (0,7):
    for l  in range (0,27):
      print(X[k][l],end="")
      theBlock = X[k][l]
      m = 0
      if (theBlock == "1"):
        m = 4
      if (theBlock == "2"):
        m = 9
      if (theBlock == "3"):
        m = 1
      if (theBlock == "5"):
        m = 2
      if (theBlock == "6"):
        m = 6
      if (theBlock == " "):
        m = 0
      if m == 0:
        mc.setBlocks(x-3,6-y-k,z+l,x+3,6-y-k,z+l,0)
      else:
        print("m",m)
        mc.setBlocks(x-3,y-k,z+l,x+3,y-k,z+l,35,m)
        #mc.setBlocks(x-3,6-y-k,z+l,x+3,6-y-k,z+l,35,m)
    print()
    
def main():
         
  mc = init()
  x,y,z = mc.player.getPos()
  #clearAir(mc,x,y,z)
  print("xyz",x,y,z)
  truck(mc,x,y,z+5)
  mc.player.setPos(x,y,z-2)


if __name__ == "__main__":
    main()

'''
#API Blocks
#====================
#   AIR                   0
#   STONE                 1
#   GRASS                 2
#   DIRT                  3
#   COBBLESTONE           4
#   WOOD_PLANKS           5
#   SAPLING               6
#   BEDROCK               7
#   WATER_FLOWING         8
#   WATER                 8
#   WATER_STATIONARY      9
#   LAVA_FLOWING         10
#   LAVA                 10
#   LAVA_STATIONARY      11
#   SAND                 12
#   GRAVEL               13
#   GOLD_ORE             14
#   IRON_ORE             15
#   COAL_ORE             16
#   WOOD                 17
#   LEAVES               18
#   GLASS                20
#   LAPIS_LAZULI_ORE     21
#   LAPIS_LAZULI_BLOCK   22
#   SANDSTONE            24
#   BED                  26
#   COBWEB               30
#   GRASS_TALL           31
#   WOOL                 35
#   FLOWER_YELLOW        37
#   FLOWER_CYAN          38
#   MUSHROOM_BROWN       39
#   MUSHROOM_RED         40
#   GOLD_BLOCK           41
#   IRON_BLOCK           42
#   STONE_SLAB_DOUBLE    43
#   STONE_SLAB           44
#   BRICK_BLOCK          45
#   TNT                  46
#   BOOKSHELF            47
#   MOSS_STONE           48
#   OBSIDIAN             49
#   TORCH                50
#   FIRE                 51
#   STAIRS_WOOD          53
#   CHEST                54
#   DIAMOND_ORE          56
#   DIAMOND_BLOCK        57
#   CRAFTING_TABLE       58
#   FARMLAND             60
#   FURNACE_INACTIVE     61
#   FURNACE_ACTIVE       62
#   DOOR_WOOD            64
#   LADDER               65
#   STAIRS_COBBLESTONE   67
#   DOOR_IRON            71
#   REDSTONE_ORE         73
#   SNOW                 78
#   ICE                  79
#   SNOW_BLOCK           80
#   CACTUS               81
#   CLAY                 82
#   SUGAR_CANE           83
#   FENCE                85
#   GLOWSTONE_BLOCK      89
#   BEDROCK_INVISIBLE    95
#   STONE_BRICK          98
#   GLASS_PANE          102
#   MELON               103
#   FENCE_GATE          107
#   GLOWING_OBSIDIAN    246
#   NETHER_REACTOR_CORE 247
'''

