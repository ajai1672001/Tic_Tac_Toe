a_1=input("please enter player 1 name : ").strip().upper()
a_2=input("please enter player 2 name : ").strip().upper()
pos= [' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")
def board():
    print("{}|{}|{}".format(pos[0],pos[1],pos[2]))
    print('-----')
    print("{}|{}|{}".format(pos[3], pos[4], pos[5]))
    print('-----')
    print("{}|{}|{}".format(pos[6], pos[7], pos[8]))
board()

def winner(pla):
    if (pos[0] == pla and pos[1] == pla and pos[2] == pla) or \
        (pos[3]  == pla and pos[4]  == pla and pos[5] == pla) or \
        (pos[6] == pla and pos[7] == pla and pos[8] == pla) or \
        (pos[0] == pla and pos[3] == pla and pos[6]== pla)  or \
        (pos[1] == pla and pos[4]  == pla and pos[7]== pla) or \
        (pos[2] == pla and pos[5] == pla and pos[8] == pla)  or \
        (pos[0] == pla and pos[4] == pla and pos[8]== pla) or \
        (pos[2]  == pla and pos[4]  == pla and pos[6]== pla):
        return True
    else:
        return False   

def draw(pla):
    if (pos[0] != " " and pos[1] !=" "and pos[2] !=" ") and \
     (pos[3]  != " " and pos[4]  !=" " and pos[5] !=" ") and \
     (pos[6] != " " and pos[7] !=" "and pos[8] !=" "):
        return True
        
    else:
        return False


user=1
pla='X'
while True:
    if  user==1:
        pla='X'
        name=a_1
        c =input("It's  {} turn:: Enter your position: ".format(a_1))
        if c=="restart":
            pos[1]=pos[2]=pos[3]=pos[4]=pos[5]=pos[6]=pos[7]=pos[8]=pos[0]=" "
        if c=="stop":
            exit() 
        if c.isdigit():
            coin=int(c)
            if coin>=0 and coin<10  :
                if pos[coin-1]==' ':
                    pos[coin-1] = 'X'
                    user = 2
                else:
                    print("Space has taken")
            else:
                print("Enter 0 to 9 numbers only")
        else:
            print("enter  number only")
    else:
        pla='O'
        name=a_2
        c = input("It's  {} turn:: Enter your position: ".format(a_2))
        if c=="restart":
            pos[1]=pos[2]=pos[3]=pos[4]=pos[5]=pos[6]=pos[7]=pos[8]=pos[0]=" "
        if c=="stop":
            exit()
        if c.isdigit():
            coin=int(c)
            if coin>=0 and coin<10:
                if pos[coin-1]==' ' :
                    pos[coin-1] = 'O'
                    user = 1
                else:
                    print("space has taken")
            else:
                print("Enter 0 to 9 numbers only")
        else:
            print("enter  number only")

    board()
    if winner(pla):
        print("the match winner is {}".format(name))
        per=input("play again yes or No : ")
        if per=='yes'or per=='s':
            pos[1]=pos[2]=pos[3]=pos[4]=pos[5]=pos[6]=pos[7]=pos[8]=pos[0]=" "
            board()
        else:
            exit()
      
    if draw(pla):
        print("match is draw")
        per=input("play again yes or No")
        if per=='yes' or per=='s' :
            pos[1]=pos[2]=pos[3]=pos[4]=pos[5]=pos[6]=pos[7]=pos[8]=pos[0]=" "
            board()
        else:   
            exit()

