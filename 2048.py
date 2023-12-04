
import keyboard 
import random

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
    word_length =  len(grid[0])
    print("\t","-"*(4*word_length))
    count :int = 1
    for ligne in grid:
        separator = " | "
        L = separator.join(ligne)
        print("\t |",L,"|")
        print("\t", "-"*(4*word_length))

def Game(grid: list[list[str]]):
    Refresh(grid)
    while True:
        if keyboard.is_pressed("left arrow"):
            ax = "lign" ; dir = -1
        elif keyboard.is_pressed("right arrow"):
            ax = "lign" ; dir = 1
        elif keyboard.is_pressed("down arrow"):
            ax = "column" ; dir = 1
        elif keyboard.is_pressed("up arrow"):
            ax = "column" ; dir = -1
        grid = Moving(ax,dir)
        grid = Addnum(grid)
        Refresh(grid)

def GetAvailableTiles(grid : list[list[str]]) -> list[tuple[int, int]]:
    Availabletiles :list  = []

    for lign in range(len(grid)) : 
        for column in range(len(grid)) : 
            if grid[lign][column] == " ":
                Availabletiles.append([lign,column])
    return Availabletiles

def Addnum(grid:list[list[str]]):
    availabletiles = GetAvailableTiles(grid)
    for i in range(2):
        randomindex1 = random.randint(0,len(availabletiles)-1)
        randomtile = availabletiles[randomindex1]
        grid[randomtile[0]][randomtile[1]] == random.randint()
    
    

def  Moving(axis: str,direction: int,grid: list[list[str]]) -> list[list[str]]:
    new_grid = Creategrid(len(grid))

    if axis == "lign":
        if direction == 1:

            for lign in range(len(grid)):
                for column in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid),0):
                            if new_grid[lign][count] == " ":
                                new_grid[lign][count] == grid[lign][column]
                                break

        elif direction == -1:

            for lign in range(len(grid)):
                for column in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)):
                            if new_grid[lign][count] == " ":
                                new_grid[lign][count] == grid[lign][column]
                                break

    elif axis == "column":
        
        if direction == 1:

            for column in range(len(grid)):
                for lign in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid),0):
                            if new_grid[count][column] == " ":
                                new_grid[count][column] == grid[lign][column]
                                break

        elif direction == -1:

            for column in range(len(grid)):
                for lign in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)):
                            if new_grid[count][column] == " ":
                                new_grid[count][column] == grid[lign][column]
                                break
    return new_grid
