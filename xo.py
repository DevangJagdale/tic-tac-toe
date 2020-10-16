import os
#actual board
board=['-','-','-',
       '-','-','-',
       '-','-','-']

#position reference for players       
example=['1','2','3',
       '4','5','6',
       '7','8','9']

checkifused=[] #used to check if position is already taken or not
tielist=[1,2,3,4,5,6,7,8,9] #to check whether its a tie 

#display position reference board
def sampleboard():
    print("position to play are : ")
    c=1      
    for i in range (9):
        print(example[i],"|",end="")
        c+=1
        if(c>3):
            print("\n")
            c=1

print("\n\n")
print("Lets play !!!!!") 

#display actual board
def display():
    c=1      
    for i in range (9):
        print(board[i],"|",end="")
        c+=1
        if(c>3):
            print("\n")
            c=1


player='X'                    
gameon=True #to check whether game is still being played or not
win=False   #to check if any player has won or not

def checkwin():
    #checkfor row method
    i=0
    j=1
    k=2
    for n in range(0,3,1):
        if((board[i]==board[j]==board[k]=='X') or (board[i]==board[j]==board[k]=='O')):
            print("player {} wins the game by row  !!!".format(board[i]))
            return True
        i+=3
        j+=3
        k+=3
    
    #check for column method 
    i=0
    j=3
    k=6
    for n in range(0,3,1):
        if((board[i]==board[j]==board[k]=='X') or (board[i]==board[j]==board[k]=='O')):
            print("player {} wins the game by column !!!".format(board[i]))
            return True
        i+=1
        j+=1
        k+=1
    
    #check for diagonal method            
    if((board[0]==board[4]==board[8]=='X') or (board[0]==board[4]==board[8]=='O')):
        print("player {} wins the game by diagonal match!!!".format(board[0]))
        return True 
        
    if((board[2]==board[4]==board[6]=='X') or (board[2]==board[4]==board[6]=='O')):
        print("player {} wins the game by diagonal match!!!".format(board[0]))
        return True
     
     
    #check for tie 
    checkifused.sort()
    if(tielist==checkifused):
        print("It's a tie")
        return True
    return False



sampleboard()                    
while gameon: 
   
    used=1 #if a position is used it returns 1 or else 0
    print("Player 'X' turn")
    if(player=='X'):
        while(used):
            position=int(input("Enter position for player 'X' : "))
            used=position in checkifused
            checkifused.append(position)
            if(used):
                print("Position is already taken")
            else:
                used=0
            
        board[(position)-1] = "X"
        os.system("cls")
        display()
        if(checkwin()):
            gameon=False
            break
        player='O'
    sampleboard()
    
    
    used=1
    print("Player 'O' turn")    
    if(player=='O'):
        while(used):
            position=int(input("Enter position for player 'O' : "))
            used=position in checkifused
            checkifused.append(position)
            if(used):
                print("Position is already taken")
            else:
                used=0
                
        board[position-1]="O"
        os.system('cls')
        display()
        if(checkwin()):
            gameon=False
            break
        player='X'
        sampleboard()
    

    
                    
                    