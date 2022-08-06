
DIRECTION = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}

class List:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next == None:
            return(f"{self.val} -> None")
        else:
            return(f"{self.val} -> {str(self.next)}")

    def is_empty(L):
        return L is None

    def List_add(L, value):
        if L == None:
            return List(value, None)
        else:
            return List(L.val, List.List_add(L.next, value))

    def List_size(L):
        i = 0
        while L is not None:
            i += 1
            L = L.next
        
        return i

def Snake_move(M, L, dir, score, heigh, width):
    Fruit = False
    List_save = L
    Save_Value = L.val
    
    # Calculate new snake head coord
    if dir == 'left' and L.val[1] == 0:
        Next_coord = (L.val[0], width-1)
    elif dir == 'right' and L.val[1] == width-1:
        Next_coord = (L.val[0], 0)
    elif dir == 'up' and L.val[0] == 0:
        Next_coord = (heigh-1, L.val[1])
    elif dir == 'down' and L.val[0] == heigh-1:
        Next_coord = (0, L.val[1])
    else:
        Next_coord = (DIRECTION[dir][0] + L.val[0], DIRECTION[dir][1] + L.val[1])

    # Check nature of the future snake head coord
    if M[Next_coord[0]][Next_coord[1]] == 3:
        Fruit = True
    elif M[Next_coord[0]][Next_coord[1]] == 2: 
        raise ValueError(1)         # Error : You take a wall !
        quit
    elif M[Next_coord[0]][Next_coord[1]] == 1:
        raise ValueError(2)         # Error : You ate your tale !
        quit

    # Update snake head coord and print on matrix
    L.val = Next_coord
    M[Next_coord[0]][Next_coord[1]] = 1
    L = L.next

    # Loot to update snake segment coord
    while L is not None:
        Save_bis_Value = L.val
        L.val = Save_Value
        Save_Value = Save_bis_Value
        L = L.next
    
    # If snake eat fruit -> spawn new segment at the end of the snake
    if Fruit:
        List_save = List.List_add(List_save, Save_Value)
        score += 50
    else:
        M[Save_Value[0]][Save_Value[1]] = 0

    return List_save, M, Fruit, score