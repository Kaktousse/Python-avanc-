
import keyboard 
import random

def Refresh(grid : list[list[str]]):
    #print("\n"*100)
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
    while True:
        k = input(' : ')
        if k == 'q':
            print("left")
            grid = Moving('left',grid)
            grid = Addnum(grid)
            Refresh(grid)
        elif k == 'd':
            print("right")
            grid = Moving('right',grid)
            grid = Addnum(grid)
            Refresh(grid)  
        elif k == 'z':
            print("up")
            grid = Moving('up',grid)
            grid = Addnum(grid)
            Refresh(grid)  
        elif k == 's':
            print("down")
            grid = Moving('down',grid)
            grid = Addnum(grid)
            Refresh(grid)       

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
        grid[randomtile[0]][randomtile[1]] = str(random.choice([2,4]))
        availabletiles.pop(randomindex)
    return grid
    
    

def  Moving(axis: str,grid: list[list[str]]) -> list[list[str]]:
    new_grid = Creategrid(len(grid))
    already_merge = []
    if axis == "right":
            
            for lign in range(len(grid)):
                for column in range(len(grid)-1,-1,-1):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)-1,-1,-1):
                            if new_grid[lign][count] == " ":
                                new_grid[lign][count] = grid[lign][column]
                                grid[lign][column] = " "
                                break
                            elif new_grid[lign][count] == grid[lign][column] and [lign,count] not in already_merge:
                                new_grid[lign][count] = str(int(grid[lign][column]) + int(new_grid[lign][count]))
                                grid[lign][column] = " "
                                break
                               
    elif axis == "left":
                                        
            for lign in range(len(grid)):
                for column in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)):
                            if new_grid[lign][count] == " ":
                                new_grid[lign][count] = grid[lign][column]
                                grid[lign][column] = " "
                                break
                            elif new_grid[lign][count] == grid[lign][column] and [lign,count] not in already_merge:
                                new_grid[lign][count] = str(int(grid[lign][column]) + int(new_grid[lign][count]))
                                grid[lign][column] = " "
                                break

    elif axis == "up":

            for column in range(len(grid)):
                for lign in range(len(grid)):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)):
                            if new_grid[count][column] == " ":
                                new_grid[count][column] = grid[lign][column]
                                grid[lign][column] = " "
                                break
                            elif new_grid[count][column] == grid[lign][column] and [count,column] not in already_merge:
                                new_grid[count][column] = str(int(grid[lign][column]) + int(new_grid[count][column]))
                                grid[lign][column] = " "
                                break
                                
    elif axis == "down":
            
            for column in range(len(grid)):
                for lign in range(len(grid)-1,-1,-1):
                    if grid[lign][column] != " ":
                        for count in range(len(new_grid)-1,-1,-1):
                            if new_grid[count][column] == " ":
                                new_grid[count][column] = grid[lign][column]
                                grid[lign][column] = " "
                                break
                            elif new_grid[count][column] == grid[lign][column] and [count,column] not in already_merge:
                                new_grid[count][column] = str(int(grid[lign][column]) + int(new_grid[count][column]))
                                already_merge.append([count,column])
                                grid[lign][column] = " "
                                break
    return new_grid


Game(Creategrid(4))