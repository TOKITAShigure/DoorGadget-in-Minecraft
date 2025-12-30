# This is a generator of Doorgadget
# and this is a partial class,so please prepare your aggregation class in each



from amulet.api.block import Block 
from amulet.api.entity import Entity
from amulet_nbt import StringTag
from amulet_nbt import NamedTag



class DoorGad2Mine():

    game_version=("java",(1,21,6)) # Minecraft Java Edition ver.1.21.6


    # declear the blocks used in the gadget
    stone=Block("minecraft","stone")
    slab=Block("minecraft","stone_slab",{"type":StringTag("top")})
    glass=Block("minecraft","glass")
    dirt=Block("minecraft","dirt")
    drip_up=Block("minecraft","big_dripleaf")
    drip_lo=Block("minecraft","big_dripleaf_stem")
    water_1=Block("minecraft","water",{"level":StringTag("0")})
    water_2=Block("minecraft","water",{"level":StringTag("1")})
    water_3=Block("minecraft","water",{"level":StringTag("2")})
    water_4=Block("minecraft","water",{"level":StringTag("3")})
    door=Block("minecraft","oak_trapdoor",{"half":StringTag("top"),"facing":StringTag("north")})
    chain=Block("minecraft","chain")
    sand=Block("minecraft","sand")
    cactus=Block("minecraft","cactus")
    ladder=Block("minecraft","ladder")
    ladder_2=Block("minecraft","ladder",{"facing":StringTag("east")})
    ice=Block("minecraft","blue_ice")
    air=Block("minecraft","air")
    rail=Block("minecraft","rail",{"shape":StringTag("east_west")})
    rail_2=Block("minecraft","rail")
    bed_1=Block("minecraft","white_bed",{"part":StringTag("head"),"facing":StringTag("west")})
    bed_2=Block("minecraft","white_bed",{"part":StringTag("foot"),"facing":StringTag("west")})
    bed_3=Block("minecraft","white_bed",{"part":StringTag("foot"),"facing":StringTag("south")})
    bed_4=Block("minecraft","white_bed",{"part":StringTag("head"),"facing":StringTag("south")})
    shelf_1=Block("minecraft","oak_shelf",{"facing":StringTag("east")})
    shelf_2=Block("minecraft","oak_shelf",{"facing":StringTag("west")})
    shelf_3=Block("minecraft","oak_shelf",{"facing":StringTag("north")})
    shelf_4=Block("minecraft","oak_shelf",{"facing":StringTag("south")})


    # constructor
    def __init__(self,level,origin_x,origin_y,origin_z):

        self.level=level
        self.origin_x=origin_x
        self.origin_y=origin_y
        self.origin_z=origin_z
    

    # destructor
    def __del__(self):

        self.level.save()
        self.level.close()

    
    # set Block in the input level
    def setBlock(self,x,y,z,name_set):

        self.level.set_version_block(x,y,z,"minecraft:overworld",self.game_version,name_set)



    #set Doorgadget in the input level
    def setGadget(self):
        
        #traverse
        for i in range(32): # z size is 32 blocks

            # set dripleaf
            if i==19:

                self.setBlock(self.origin_x+1,self.origin_y+1,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+2,self.origin_z+i,self.glass)

                self.setBlock(self.origin_x+1,self.origin_y+3,self.origin_z+i-1,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+4,self.origin_z+i-1,self.glass)

                self.setBlock(self.origin_x+1,self.origin_y+3,self.origin_z+i,self.ice)
                self.setBlock(self.origin_x+1,self.origin_y+4,self.origin_z+i,self.slab)

                self.setBlock(self.origin_x+1,self.origin_y+3,self.origin_z+i+1,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+4,self.origin_z+i+1,self.glass)

                self.setBlock(self.origin_x,self.origin_y,self.origin_z+i,self.dirt)

                self.setBlock(self.origin_x,self.origin_y+3,self.origin_z+i-1,self.glass)
                self.setBlock(self.origin_x,self.origin_y+4,self.origin_z+i-1,self.glass)

                self.setBlock(self.origin_x,self.origin_y+1,self.origin_z+i,self.drip_lo)
                self.setBlock(self.origin_x,self.origin_y+2,self.origin_z+i,self.drip_up)

                self.setBlock(self.origin_x,self.origin_y+1,self.origin_z+i+1,self.stone)
                self.setBlock(self.origin_x,self.origin_y+4,self.origin_z+i+1,self.glass)

                self.setBlock(self.origin_x-1,self.origin_y+1,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x-1,self.origin_y+2,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x-1,self.origin_y+3,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x-1,self.origin_y+4,self.origin_z+i,self.glass)

                self.setBlock(self.origin_x-1,self.origin_y+3,self.origin_z+i+1,self.glass)

            # set valve
            elif i==24:

                self.setBlock(self.origin_x,self.origin_y,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x,self.origin_y+1,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x,self.origin_y+2,self.origin_z+i,self.stone)

                self.setBlock(self.origin_x,self.origin_y+1,self.origin_z+i-1,self.ladder)
                self.setBlock(self.origin_x,self.origin_y+2,self.origin_z+i-1,self.ladder)

                for j in range(8):

                    if j==1 or j==5:
                        self.setBlock(self.origin_x,self.origin_y+3,self.origin_z+i+j-3,self.glass)
                        self.setBlock(self.origin_x,self.origin_y+4,self.origin_z+i+j-3,self.glass)

                    elif j>=2 and j<=4:
                        self.setBlock(self.origin_x+1,self.origin_y+4,self.origin_z+i+j-3,self.glass)
                        self.setBlock(self.origin_x,self.origin_y+5,self.origin_z+i+j-3,self.glass)
                        self.setBlock(self.origin_x-1,self.origin_y+4,self.origin_z+i+j-3,self.glass)

                    self.setBlock(self.origin_x+1,self.origin_y+1,self.origin_z+i+j-3,self.glass)
                    self.setBlock(self.origin_x+1,self.origin_y+2,self.origin_z+i+j-3,self.glass)
                    self.setBlock(self.origin_x+1,self.origin_y+3,self.origin_z+i+j-3,self.glass)

                    self.setBlock(self.origin_x-1,self.origin_y+1,self.origin_z+i+j-3,self.glass)
                    self.setBlock(self.origin_x-1,self.origin_y+2,self.origin_z+i+j-3,self.glass)
                    self.setBlock(self.origin_x-1,self.origin_y+3,self.origin_z+i+j-3,self.glass)

            # normal
            else:

                self.setBlock(self.origin_x-1,self.origin_y+1,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x-1,self.origin_y+2,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x,self.origin_y,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x+1,self.origin_y+1,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+2,self.origin_z+i,self.glass)

        #close
        for i in range(32):

            if i<=19:

                # set valve
                if i==2 or i==6:
                    self.setBlock(self.origin_x+4,self.origin_y+8,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+4,self.origin_y+9,self.origin_z+i,self.glass)

                elif i>=3 and i<=5:

                    if i==4:
                        self.setBlock(self.origin_x+4,self.origin_y+6,self.origin_z+i,self.stone)
                        self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i,self.stone)

                        self.setBlock(self.origin_x+4,self.origin_y+6,self.origin_z+i-1,self.ladder)
                        self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i-1,self.ladder)


                    self.setBlock(self.origin_x+3,self.origin_y+8,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+3,self.origin_y+9,self.origin_z+i,self.glass)

                    self.setBlock(self.origin_x+4,self.origin_y+10,self.origin_z+i,self.glass)

                    self.setBlock(self.origin_x+5,self.origin_y+8,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+5,self.origin_y+9,self.origin_z+i,self.glass)

                # normal
                self.setBlock(self.origin_x+5,self.origin_y+6,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+5,self.origin_y+7,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+4,self.origin_y+5,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x+3,self.origin_y+6,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+3,self.origin_y+7,self.origin_z+i,self.glass)

                # set shelves
                if i==18:
                    self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i,self.shelf_1)
                    self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i-1,self.shelf_2)

                    self.setBlock(self.origin_x+4,self.origin_y+4,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+3,self.origin_y+4,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+2,self.origin_y+4,self.origin_z+i,self.glass)

                    self.setBlock(self.origin_x+4,self.origin_y+8,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+4,self.origin_y+9,self.origin_z+i,self.glass)

                # set trapdoor
                elif i==19:

                    self.setBlock(self.origin_x+4,self.origin_y+5,self.origin_z+i,self.air)
                    self.setBlock(self.origin_x+5,self.origin_y+4,self.origin_z+i,self.glass)

                    self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i,self.door)

                    self.setBlock(self.origin_x+4,self.origin_y+4,self.origin_z+i,self.water_1)
                    self.setBlock(self.origin_x+3,self.origin_y+4,self.origin_z+i,self.water_2)
                    self.setBlock(self.origin_x+2,self.origin_y+4,self.origin_z+i,self.water_3)

                    self.setBlock(self.origin_x+4,self.origin_y+3,self.origin_z+i,self.stone)
                    self.setBlock(self.origin_x+3,self.origin_y+3,self.origin_z+i,self.stone)
                    self.setBlock(self.origin_x+2,self.origin_y+3,self.origin_z+i,self.stone)

            else:

                if i==20:

                    self.setBlock(self.origin_x+4,self.origin_y+5,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+4,self.origin_y+4,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+3,self.origin_y+4,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+2,self.origin_y+4,self.origin_z+i,self.glass)

                    self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i,self.bed_3)       
                    self.setBlock(self.origin_x+4,self.origin_y+7,self.origin_z+i+1,self.bed_4)
                    self.setBlock(self.origin_x+4,self.origin_y+8,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+4,self.origin_y+8,self.origin_z+i+1,self.glass)
                    

                # normal
                self.setBlock(self.origin_x+5,self.origin_y+7,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+5,self.origin_y+8,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+4,self.origin_y+6,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x+3,self.origin_y+7,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+3,self.origin_y+8,self.origin_z+i,self.glass)

        #open
        for i in range(20):

            # set valve
            if i==13 or i==17:
                self.setBlock(self.origin_x+8,self.origin_y+8,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+9,self.origin_z+i,self.glass)

            elif i>=14 and i<=16:

                if i==15:
                    self.setBlock(self.origin_x+8,self.origin_y+6,self.origin_z+i,self.stone)
                    self.setBlock(self.origin_x+8,self.origin_y+7,self.origin_z+i,self.stone)

                    self.setBlock(self.origin_x+8,self.origin_y+6,self.origin_z+i-1,self.ladder)
                    self.setBlock(self.origin_x+8,self.origin_y+7,self.origin_z+i-1,self.ladder)

                
                self.setBlock(self.origin_x+7,self.origin_y+8,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+7,self.origin_y+9,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+10,self.origin_z+i,self.glass)

                self.setBlock(self.origin_x+9,self.origin_y+8,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+9,self.origin_y+9,self.origin_z+i,self.glass)

            # add nothing path
            if i==10:

                self.setBlock(self.origin_x+8,self.origin_y+5,self.origin_z+i,self.stone)

                self.setBlock(self.origin_x+8,self.origin_y+6,self.origin_z+i,self.ladder_2)
                self.setBlock(self.origin_x+7,self.origin_y+6,self.origin_z+i,self.stone)

                self.setBlock(self.origin_x+8,self.origin_y+7,self.origin_z+i,self.ladder_2)
                self.setBlock(self.origin_x+7,self.origin_y+7,self.origin_z+i,self.stone)

                self.setBlock(self.origin_x+8,self.origin_y+8,self.origin_z+i,self.ladder_2)
                self.setBlock(self.origin_x+7,self.origin_y+8,self.origin_z+i,self.stone)


                for j in range(3):
                    
                    self.setBlock(self.origin_x+9,self.origin_y+8+j,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+8,self.origin_y+8+j,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+8,self.origin_y+8+j,self.origin_z+i-1,self.glass)

                for j in range(5):

                    self.setBlock(self.origin_x+7-j,self.origin_y+9,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+10,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+9,self.origin_z+i-1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+10,self.origin_z+i-1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+8,self.origin_z+i,self.stone)

                self.setBlock(self.origin_x+2,self.origin_y+8,self.origin_z+i,self.stone)
                self.setBlock(self.origin_x+2,self.origin_y+9,self.origin_z+i-1,self.glass)
                self.setBlock(self.origin_x+2,self.origin_y+10,self.origin_z+i-1,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+9,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+1,self.origin_y+10,self.origin_z+i,self.glass)
                
                for j in range(8):

                    if j==7:

                        self.setBlock(self.origin_x+2,self.origin_y+10,self.origin_z+i+j+1,self.stone)

                    self.setBlock(self.origin_x+3,self.origin_y+9,self.origin_z+i+j+1,self.glass)
                    self.setBlock(self.origin_x+3,self.origin_y+10,self.origin_z+i+j+1,self.glass)
                    self.setBlock(self.origin_x+2,self.origin_y+8,self.origin_z+i+j+1,self.stone)
                    self.setBlock(self.origin_x+1,self.origin_y+9,self.origin_z+i+j+1,self.glass)
                    self.setBlock(self.origin_x+1,self.origin_y+10,self.origin_z+i+j+1,self.glass)


            if i==19:

                self.setBlock(self.origin_x+9,self.origin_y+6,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+9,self.origin_y+7,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+6,self.origin_z+i+1,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+7,self.origin_z+i+1,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+5,self.origin_z+i,self.stone)
                
                for j in range(6):

                    #cactus generator
                    if j==5:

                        self.setBlock(self.origin_x+10-j,self.origin_y+9,self.origin_z+i,self.slab)
                        self.setBlock(self.origin_x+10-j,self.origin_y+9,self.origin_z+i-1,self.glass)
                        self.setBlock(self.origin_x+10-j,self.origin_y+9,self.origin_z+i+1,self.stone)
                        self.setBlock(self.origin_x+10-j,self.origin_y+9,self.origin_z+i+2,self.stone)
                        self.setBlock(self.origin_x+10-j,self.origin_y+8,self.origin_z+i,self.ice)
                        self.setBlock(self.origin_x+10-j,self.origin_y+6,self.origin_z+i,self.air)
                        self.setBlock(self.origin_x+10-j,self.origin_y+7,self.origin_z+i,self.shelf_3)
                        self.setBlock(self.origin_x+11-j,self.origin_y+7,self.origin_z+i,self.shelf_4)
                        self.setBlock(self.origin_x+12-j,self.origin_y+7,self.origin_z+i,self.shelf_4)

                        for k in range(3):

                            self.setBlock(self.origin_x+10-j,self.origin_y+10,self.origin_z+i+k,self.glass)
                            self.setBlock(self.origin_x+10-j,self.origin_y+11,self.origin_z+i+k,self.glass)
                            self.setBlock(self.origin_x+10-j,self.origin_y+12,self.origin_z+i+k,self.glass)

                        for k in range(3):

                            if k==0:

                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+2,self.water_2)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+1,self.water_3)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i,self.water_4)

                            elif k==1:

                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+2,self.water_2)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i,self.water_3)

                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+1,self.stone)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+10,self.origin_z+i+1,self.sand)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+11,self.origin_z+i+1,self.cactus)
                                self.setBlock(self.origin_x+12-j+k,self.origin_y+12,self.origin_z+i+1,self.shelf_2)

                            else:

                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+2,self.water_1)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+1,self.water_2)
                                self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i,self.water_2)

                            self.setBlock(self.origin_x+11-j+k,self.origin_y+8,self.origin_z+i,self.stone)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i-1,self.stone)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+9,self.origin_z+i+3,self.stone)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+8,self.origin_z+i+1,self.stone)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+8,self.origin_z+i+1,self.stone)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+8,self.origin_z+i+2,self.stone)

                            self.setBlock(self.origin_x+11-j+k,self.origin_y+10,self.origin_z+i-1,self.glass)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+11,self.origin_z+i-1,self.glass)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+12,self.origin_z+i-1,self.glass)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+10,self.origin_z+i+3,self.glass)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+11,self.origin_z+i+3,self.glass)
                            self.setBlock(self.origin_x+11-j+k,self.origin_y+12,self.origin_z+i+3,self.glass)

                        for k in range(3):

                            self.setBlock(self.origin_x+11-j+3,self.origin_y+9,self.origin_z+i+k,self.stone)
                            self.setBlock(self.origin_x+11-j+3,self.origin_y+10,self.origin_z+i+k,self.glass)
                            self.setBlock(self.origin_x+11-j+3,self.origin_y+11,self.origin_z+i+k,self.glass)
                            self.setBlock(self.origin_x+11-j+3,self.origin_y+12,self.origin_z+i+k,self.glass)
                        

                for j in range(3):
                    self.setBlock(self.origin_x+7-j,self.origin_y+6,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+7,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+6,self.origin_z+i-1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+7,self.origin_z+i-1,self.glass)
                    self.setBlock(self.origin_x+7-j,self.origin_y+5,self.origin_z+i,self.stone)


                for j in range(5):

                    if j==0:
                        self.setBlock(self.origin_x+3-j,self.origin_y+8,self.origin_z+i-1,self.glass)
                        self.setBlock(self.origin_x+3-j,self.origin_y+9,self.origin_z+i,self.glass)

                        self.setBlock(self.origin_x+2-j,self.origin_y+8,self.origin_z+i,self.bed_1)
                        self.setBlock(self.origin_x+3-j,self.origin_y+8,self.origin_z+i,self.bed_2)

                    
                    elif j>=2:
                        self.setBlock(self.origin_x+3-j,self.origin_y+8,self.origin_z+i-1,self.glass)
                        self.setBlock(self.origin_x+3-j,self.origin_y+9,self.origin_z+i-1,self.glass)

                    self.setBlock(self.origin_x+3-j,self.origin_y+7,self.origin_z+i,self.stone)
                    self.setBlock(self.origin_x+3-j,self.origin_y+8,self.origin_z+i+1,self.glass)
                    self.setBlock(self.origin_x+3-j,self.origin_y+9,self.origin_z+i+1,self.glass)

            # normal
            else:

                self.setBlock(self.origin_x+9,self.origin_y+6,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+9,self.origin_y+7,self.origin_z+i,self.glass)
                self.setBlock(self.origin_x+8,self.origin_y+5,self.origin_z+i,self.stone)

                if i!=10:

                    self.setBlock(self.origin_x+7,self.origin_y+6,self.origin_z+i,self.glass)
                    self.setBlock(self.origin_x+7,self.origin_y+7,self.origin_z+i,self.glass)