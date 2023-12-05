
import keyboard 
import random
import time

def Refresh(grid : list[list[str]]):
    print("\n"*100)
    Drawgrid(grid)

def Creategrid(lenght:int) -> list[list[str]]:
    grid = []
    for lign in range(lenght):
        new_lign = []
        for column in range(lenght):
            new_lign.append(" ")
        grid.append(new_lign)
    return grid


def Drawgrid(grid: list[list[str]]):
    for lign in range(len(grid)):
        for tile in range(len(grid)): 
            if grid[lign][tile] != " ":
                grid[lign][tile] = str(grid[lign][tile])

    word_length =  len(grid[0])
    print("\t","-"*(4*word_length))
    count :int = 1
    for ligne in grid:
        separator = " | "
        L = separator.join(ligne)
        print("\t |",L,"|")
        print("\t", "-"*(4*word_length))

    for lign in grid:
        for tile in lign: 
            if tile.isdigit():
                tile = int(tile)

def Game(grid: list[list[str]]):
    grid = Addnum(grid)
    Refresh(grid)
    pressed = False
    while True:
        if keyboard.is_pressed("left arrow"):
            time.sleep(0.1)
            direction = 'left'
            pressed = True      
        elif keyboard.is_pressed("right arrow"):
            time.sleep(0.1)
            direction ='right'
            pressed = True
        elif keyboard.is_pressed("up arrow"):
            time.sleep(0.1)
            direction ='up'
            pressed = True
        elif keyboard.is_pressed("down arrow"):
            time.sleep(0.1)
            direction ='down'
            pressed = True
        if pressed == True:
            grid = Moving(direction,grid)
            grid = Addnum(grid)
            Refresh(grid)
            pressed = False    


def GetAvailableTiles(grid : list[list[str]]) -> list[tuple[int, int]]:
    Availabletiles :list  = []

    for lign in range(len(grid)) : 
        for column in range(len(grid)) : 
            if grid[lign][column] == " ":
                Availabletiles.append([lign,column])
    return Availabletiles

def Addnum(grid:list[list[str]]) -> list[list[str]]:
    availabletiles = GetAvailableTiles(grid)
    for i in range(2):
        randomindex = random.randint(0,len(availabletiles)-1)
        randomtile = availabletiles[randomindex]
        grid[randomtile[0]][randomtile[1]] = random.choice([2,4])
        availabletiles.pop(randomindex)
    return grid
    

def Checkmerge(direction:str ,grid:list[list[str]],wheremerge: tuple[int,int], tiletomerge: int) -> tuple[int,int]:
    # check lign #
    merge = ['none','none']
    if wheremerge[0] != -1:
        lign = wheremerge[0]
        if direction == 'left':
            for tile in range(tiletomerge):
                if grid[lign][tile] == grid[lign][tiletomerge]:
                    merge = [lign,tile]
                if grid[lign][tile] != grid[lign][tiletomerge] and grid[lign][tile] != " ":
                    merge = ['none','none']

        if direction == 'right':
            for tile in range(len(grid)-1,tiletomerge,-1):
                if grid[lign][tile] == grid[lign][tiletomerge]:
                    merge = [lign,tile]
                if grid[lign][tile] != grid[lign][tiletomerge] and grid[lign][tile] != " ":
                    merge = ['none','none']
        
    # check column #
    elif wheremerge[1] != -1:
        column = wheremerge[1]
        if direction == 'up':
            for tile in range(tiletomerge):
                if grid[tile][column] == grid[tiletomerge][column]:
                    merge = [tile,column]
                if grid[tile][column] != grid[tiletomerge][column] and grid[tile][column] != " ":
                    merge = ['none','none']

        if direction == 'down':
            for tile in range(len(grid)-1,tiletomerge,-1):
                if grid[tile][column] == grid[tiletomerge][column]:
                    merge = [tile,column]
                if grid[tile][column] != grid[tiletomerge][column] and grid[tile][column] != " ":
                    merge = ['none','none']
    
    return merge

def Checkempty(direction:str, grid:list[list[str]],wherecheck : tuple[int,int],tiletocheck: int) -> tuple[int,int]:
    check = ['none','none']

    if wherecheck[0] != -1:
        lign = wherecheck[0]
        if direction == 'left':
            for tile in range(tiletocheck):
                if grid[lign][tile] == " " and check == ['none','none']:
                    check = [lign,tile]
                if grid[lign][tile] != " ":
                    check = ['none','none']

        if direction == 'right':
            for tile in range(len(grid)-1,tiletocheck,-1):
                if grid[lign][tile] == " " and check == ['none','none']:
                    check = [lign,tile]
                if grid[lign][tile] != " ":
                    check = ['none','none']

        

    elif wherecheck[1] != -1:
        column = wherecheck[1]
        if direction == 'up':
            for tile in range(tiletocheck):
                if grid[tile][column] == " " and check == ['none','none']:
                    check = [tile,column]
                if grid[tile][column] != " ":
                    check = ['none','none']

        if direction == 'down':
            for tile in range(len(grid)-1,tiletocheck,-1):
                if grid[tile][column] == " " and check == ['none','none']:
                    check = [tile,column]
                if grid[tile][column] != " ":
                    check = ['none','none']
    return check


def  Moving(axis: str,grid: list[list[str]]) -> list[list[str]]:

    if axis == "right":
        for lign in range(len(grid)):
            for column in range(len(grid)-1,-1,-1):
                if grid[lign][column] != " ":
                    merge = Checkmerge("right",grid,[lign,-1],column)
                    place = Checkempty("right",grid,[lign,-1],column)
                    if merge != ['none','none']:
                        grid[merge[0]][merge[1]] = int(grid[lign][column]) + int(grid[lign][column])
                        grid[lign][column] = " "
                    elif place != ['none','none']:
                        grid[place[0]][place[1]] = grid[lign][column]
                        grid[lign][column] = " "
                          
    elif axis == "left":
 
        for lign in range(len(grid)):
            for column in range(len(grid)):
                if grid[lign][column] != " ":
                    merge = Checkmerge("left",grid,[lign,-1],column)
                    place = Checkempty("left",grid,[lign,-1],column)
                    if merge != ['none','none']:
                        grid[merge[0]][merge[1]] = int(grid[lign][column]) + int(grid[lign][column])
                        grid[lign][column] = " "
                    elif place != ['none','none']:
                        grid[place[0]][place[1]] = grid[lign][column]
                        grid[lign][column] = " "

    elif axis == "up":
        for column in range(len(grid)):
            for lign in range(len(grid)):
                if grid[lign][column] != " ":
                    merge = Checkmerge("up",grid,[-1,column],lign)
                    place = Checkempty("up",grid,[-1,column],lign)
                    if merge != ['none','none']:
                        grid[merge[0]][merge[1]] = int(grid[lign][column]) + int(grid[lign][column])
                        grid[lign][column] = " "
                    elif place != ['none','none']:
                        grid[place[0]][place[1]] = grid[lign][column]
                        grid[lign][column] = " "
                                
    elif axis == "down":            
        for column in range(len(grid)):
            for lign in range(len(grid)-1,-1,-1):
                if grid[lign][column] != " ":
                    merge = Checkmerge("down",grid,[-1,column],lign)
                    place = Checkempty("down",grid,[-1,column],lign)
                    if merge != ['none','none']:
                        grid[merge[0]][merge[1]] = int(grid[lign][column]) + int(grid[lign][column])
                        grid[lign][column] = " "
                    elif place != ['none','none']:
                        grid[place[0]][place[1]] = grid[lign][column]
                        grid[lign][column] = " "

    return grid


Game(Creategrid(4))