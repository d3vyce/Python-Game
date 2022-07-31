
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

def Snake_move(M, L, dir):
    Fruit = False
    List_save = L
    Save_Value = L.val
    Next_pos = (DIRECTION[dir][0] + L.val[0], DIRECTION[dir][1] + L.val[1])

    if M[Next_pos[0]][Next_pos[1]] == 3:
        Fruit = True
        M[Next_pos[0]][Next_pos[1]] == 0
    elif M[Next_pos[0]][Next_pos[1]] == 2: 
        raise ValueError(1)         # Error : You take a wall !
        quit
    elif M[Next_pos[0]][Next_pos[1]] == 1:
        raise ValueError(2)         # Error : You ate your tale !
        quit

    L.val = Next_pos
    L = L.next

    while L is not None:
        Save_bis_Value = L.val
        L.val = Save_Value
        Save_Value = Save_bis_Value
        L = L.next
    
    if Fruit:
        List_save = List.List_add(List_save, Save_Value)

    return List_save