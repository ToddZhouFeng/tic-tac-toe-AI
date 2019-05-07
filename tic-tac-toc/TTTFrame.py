#井字棋的框架
#井字棋的简介：井字棋（Tic-Tac-Toe），是一种在3*3格子上进行的连珠游戏，和五子棋类似，最先连成3子的一方获胜。

import numpy as np

def initBoard():
    """初始化棋盘"""
    return np.array( [ [1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]) #好像array内不支持[0 for i int (0, 10)]的形式

def isEmpty(board):
    """判断其棋盘是否为空"""
    if np.sum(board[0])>0:
        return False
    return True

def getEmpty(board):
    """返回棋盘中的空格"""
    return board[0]

def getPlayerA(board):
    """返回棋盘中玩家A下的格子"""
    return board[1]

def getPlayerB(board):
    """返回棋盘中玩家B下的格子"""
    return board[2]

def judgePlayer(player):
    """判断输赢，用1表示赢，0未赢"""
    for i in range(0,3):
        if player[i*3]==player[i*3+1]==player[i*3+2]==1:#横
            return 1
        if player[i]==player[i+3]==player[i+6]==1:#竖
            return 1
    if player[2]==player[4]==player[6]==1:#捺
        return 1
    elif player[0]==player[4]==player[8]==1:#撇
        return 1
    return 0

def judgeAll(board):
    """判断谁赢，用0表示打平，1表示A赢，-1表示B赢"""
    if judgePlayer(getPlayerA(board)):
        return 1
    elif judgePlayer(getPlayerB(board)):
        return 2
    else:
        return 0

def judgeMove(board, move):
    """判断能否走那一个格"""
    if getEmpty(board)[move]==1:
        return True
    else:
        return False

def makeMove(board, move, player=1):
    """下子，有限制"""
    if not judgeMove(board, move):
        return False
    else:
        if np.sum(board[1])>np.sum(board[2]):
            board[2][move]=1
            board[0][move]=0
            return True
        elif np.sum(board[1])<np.sum(board[2]):
            board[1][move]=1
            board[0][move]=0
            return True
        elif player==1 or player=="A":
            board[1][move]=1
            board[0][move]=0
            return True
        elif player==-1 or player==2 or player=="B":#推荐用-1表示玩家B，也可用2表示玩家B
            board[2][move]=1
            board[0][move]=0
            return True
    return False

def visualize(board):
    """将棋盘可视化输出"""
    vision=[' ' for i in range(0, 9) ]
    for i in range(0, 9):
        if board[1][i]==1:
            vision[i]='x'
    for i in range(0, 9):
        if board[2][i]==1:
            vision[i]='o'
    for i in range(0, 9):
        if board[0][i]==1:
            vision[i]=str(i)
    output="---------\n "+vision[0]+" | "+vision[1]+" | "+vision[2]+" \n "\
            +"---------\n "+vision[3]+" | "+vision[4]+" | "+vision[5]+" \n "\
            +"---------\n "+vision[6]+" | "+vision[7]+" | "+vision[8]+" \n "
    print(output)

def rotate(board, time=1):
    """将棋盘逆时针旋转，默认旋转一次，不改变原棋盘"""
    newboard=initBoard()
    for i in range(0,3):
        temp=np.reshape(board[i], (3,3))
        temp=np.rot90(temp, time)
        newboard[i]=temp.flat
    return newboard

def mirror(board, axis='y'):
    """将棋盘沿axis轴镜面对称，默认为y轴"""
    newboard=initBoard()
    trans=np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    if axis=='y':
        for i in range(0,3):
            temp=np.reshape(board[i], (3,3))
            temp=np.dot(temp, trans)
            newboard[i]=temp.flat
    else:
        for i in range(0,3):
            temp=np.reshape(board[i], (3,3))
            temp=np.dot(trans, temp)
            newboard[i]=temp.flat
    return newboard

'''
board=np.array( [ [0, 0, 1, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1]])
visualize(board)
newboard=rotate(board)
visualize(newboard)
visualize(board)
'''



