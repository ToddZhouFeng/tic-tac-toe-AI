# 井字棋的简介

井字棋（Tic-Tac-Toe），是一种在3*3格子上进行的连珠游戏，和五子棋类似，最先连成3子的一方获胜。

# 实现方法

我设想有两种方法：灰度法和01法。01法更符合直觉，故采用该法。而灰度法有个好处就是可以借用图像识别的程序，当作一种分类任务。

## 灰度法

图片每个像素的灰度是用0~255来表示，故我们可以将棋盘的格子看作图片的像素，其中空白的为0，甲方下的为128，乙方下的为255，即比如说下面这种情况则对应`board=[128, 255, 128, 0, 255, 0, 0, 128, 255]`或`board=[255, 128, 255, 0, 128, 0, 0, 255, 128]`

![井字棋](https://cn.bing.com/th?id=OIP.KgQ75KgxM3iFHVQLYkA_IAHaHa&pid=Api&rs=1&p=0 "示例")

## 01法

棋盘分为三部分：未下的，甲下的，乙下的，我们分别用三个数组表示（每个数组包含九个元素，对应九个格），1表示这个位置在数组中，0表示不在。比如我们用下面三个数组表示上图的情况：

~~~python
empty=[0, 0, 0, 1, 0, 1, 1, 0, 0]
Xs=[0, 1, 0, 0, 1, 0, 0, 0, 1]
Os=[1, 0, 1, 0, 0, 0, 0, 1, 0]
~~~

那么对于整个棋盘，我们可以把它当成一个3*9的矩阵

~~~python
board=[
    [0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1,
    [1, 0, 1, 0, 0, 0, 0, 1, 0]
]
~~~

当然，我们输入的时候是输入一个1*27的数组，即

~~~python
input=numpy.resize(board,(1,27))
~~~



# 程序

详情见TTTFrame.py，这里只给出函数原型：

~~~python
def initBoard():
    """初始化棋盘"""

def getEmpty(board):
    """返回棋盘中的空格"""

def getPlayerA(board):
    """返回棋盘中玩家A下的格子"""

def getPlayerB(board):
    """返回棋盘中玩家B下的格子"""

def judgePlayer(player):
    """判断输赢，用1表示赢，0未赢"""

def judgeAll(board):
    """判断谁赢，用0表示打平，1表示A赢，-1表示B赢"""

def judgeMove(board, move):
    """判断能否走那一个格"""

def makeMove(board, move, player=1):
    """下子，有限制"""

def visualize(board):
    """将棋盘可视化输出"""
~~~

下面给出流程图：

```flow
gameStart=>start: 开始游戏
newBoard=>operation: 新建棋盘
isWin=>condition: 是否有赢家
isFull=>condition: 是否下满了
inMove=>inputoutput: 输入棋子
judgeMove=>condition: 是否可下
makeMove=>operation: 下子
nextPlayer=>operation: 交换下子方
gameEnd=>end: 游戏结束

gameStart->newBoard->isWin
isWin(yes)->gameEnd
isWin(no)->isFull
isFull(yes)->gameEnd
isFull(no)->inMove->judgeMove
judgeMove(no)->inMove
judgeMove(yes)->makeMove->nextPlayer->isWin
```

可见，我们的AI将作用于`输入棋子`处。当然，这个程序也可以用来和你的朋友对战~