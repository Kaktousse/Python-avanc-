
import keyboard 
import random
import time

def Refresh(grid : list[list[str]]):
    #print("\n"*100)
    Drawgrid(grid)
    #print("\n"*3)

def Creategrid(lenght:int) -> list[list[str]]:
    grid = []
    for lign in range(lenght):
        new_lign = []
        for column in range(lenght):
            new_lign.append(0)
        grid.append(new_lign)
    return grid


def Drawgrid(grid: list[list[str]]):
    printed_grid = []
    for lign in range(len(grid)):
        newlign = []
        for tile in range(len(grid)): 
            if grid[lign][tile] != 0:
                newlign.append(str(grid[lign][tile]))
            elif grid[lign][tile] == 0:
                newlign.append(" ")
        printed_grid.append(newlign)

    print("\t","-"*(64))
    for ligne in printed_grid:
        separator = " \t|\t "
        L = separator.join(ligne)
        print("\t |\t",L,"\t|")
        print("\t", "-"*(64))





def Game(grid: list[list[str]]):
    grid = Addnum(grid,GetAvailableTiles(grid))
    Refresh(grid)
    pressed = False
    ending = False
    while ending == False:
        if keyboard.is_pressed("left arrow"):
            time.sleep(0.1)
            direction = "left"
            pressed = True      
        elif keyboard.is_pressed("right arrow"):
            time.sleep(0.1)
            direction ="right"
            pressed = True
        elif keyboard.is_pressed("up arrow"):
            time.sleep(0.1)
            direction ="up"
            pressed = True
        elif keyboard.is_pressed("down arrow"):
            time.sleep(0.1)
            direction ="down"
            pressed = True
        if pressed == True:
            grid = Moving(direction,grid)
            empty_tiles = GetAvailableTiles(grid)
            if len(empty_tiles) > 0:
                grid = Addnum(grid,empty_tiles)
            Refresh(grid)
            pressed = False
            if CheckEnding(grid,'Win'):
                print("Well done, you won !")
                break
            if CheckEnding(grid,'Loose'):
                print("You loose, better luck next time !")
                break

            


def CheckEnding(grid,win_or_loose):
    if win_or_loose == 'Loose':
        if len(GetAvailableTiles(grid)) == 0:
            if Checkmerge(grid) == True:
                return True
            return False
        return False
    
    if win_or_loose == 'Win':
        for lign in grid:
            for column in lign:
                if column == 2048:
                    return True
        return False

def GetAvailableTiles(grid : list[list[str]]) -> list[tuple[int, int]]:
    Availabletiles :list  = []

    for lign in range(len(grid)) : 
        for column in range(len(grid)) : 
            if grid[lign][column] == 0:
                Availabletiles.append([lign,column])
    return Availabletiles

def Addnum(grid:list[list[str]],empty_tiles: int) -> list[list[str]]:
    if len(empty_tiles) > 1:
        count = 2
    else: 
        count = 1
    for i in range(count):
        randomindex = random.randint(0,len(empty_tiles)-1)
        randomtile = empty_tiles[randomindex]
        grid[randomtile[0]][randomtile[1]] = int(random.choice([2,4]))
        empty_tiles.pop(randomindex)
    return grid
    

def Checkmerge(grid:list[list[str]]) -> tuple[int,int]:
    for lign in range(len(grid)):
        for column in range(len(grid)):
            if column+1 < len(grid):
                if grid[lign][column] == grid[lign][column+1]:
                    return False
            if lign+1 < len(grid):
                if grid[lign][column] == grid[lign+1][column]:
                    return False
    
    return True


def  Moving(axis: str,grid: list[list[str]]) -> list[list[str]]:

    alreadymerge = []
    
    if axis == "left":
        for lign in range(4):
            start = 0
            for column in range(4):
                if grid[lign][column] != 0 and column > 0:
                    for search in range(start,column):
                        if grid[lign][column] == grid[lign][search]:
                            grid[lign][search] = grid[lign][column] + grid[lign][search]
                            start = search + 1
                            grid[lign][column] = 0
                            break
                        elif grid[lign][search] == 0:
                            grid[lign][search] = grid[lign][column]
                            grid[lign][column] = 0
                            start = search
                            break
                        if search == column - 1:
                            start +=1
                
    elif axis == "right":
         for lign in range(4):
            start = 3
            for column in range(3,-1,-1):
                if grid[lign][column] != 0 and column < 3:
                    for search in range(start,column,-1):
                        if grid[lign][column] == grid[lign][search]:
                            grid[lign][search] = grid[lign][column] + grid[lign][search]
                            start = search - 1
                            grid[lign][column] = 0
                            break
                        elif grid[lign][search] == 0:
                            grid[lign][search] = grid[lign][column]
                            grid[lign][column] = 0
                            start = search
                            break
                        if search == column+1:
                            start -= 1

                        

    
    elif axis == "up":
        for column in range(4):
            start = 0
            for lign in range(4):
                if grid[lign][column] != 0 and lign > 0:
                    merge = [-1,-1]
                    for search in range(start,lign):
                        if grid[lign][column] == grid[search][column]:
                            grid[search][column] = grid[lign][column] + grid[search][column]
                            start = search + 1
                            grid[lign][column] = 0
                            break
                        elif grid[search][column] == 0:
                            grid[search][column] = grid[lign][column]
                            grid[lign][column] = 0
                            start = search
                            break
                        if search == lign -1:
                            start +=1



    elif axis == "down":    
        for column in range(4):
            start = 3
            for lign in range(3,-1,-1):
                if grid[lign][column] != 0 and lign < 3:
                    merge = [-1,-1]
                    for search in range(start,lign,-1):
                        if grid[lign][column] == grid[search][column]:
                            grid[search][column] = grid[lign][column] + grid[search][column]
                            start = search - 1
                            grid[lign][column] = 0
                            break
                        elif grid[search][column] == 0:
                            grid[search][column] = grid[lign][column]
                            grid[lign][column] = 0
                            start = search
                            break
                        if search == lign + 1:
                            start -=1

    return grid

def Try_again(T:str) -> bool:
    return T != "N"

def Ask_str(sPossibilities: list) -> str:
    while True:
        print("Please enter ", sPossibilities,")")
        given_input:str = input(": ")   
        for element in sPossibilities:
            if element == given_input:
                return given_input

def Start(start : bool):
    while start:
        grid = Creategrid(4)
        Game(grid)
        print("\n Do you want to retry ?")
        retry:str = Ask_str(["Y","N"])
        start: bool = Try_again(retry)
    print("Game Over")

Start(True)



