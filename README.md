# tic-tac-toc-AI

所有的内容都基于《深度学习入门——基于Python的理论与实践》。

---

我将从0开始构建一个井字棋AI。以下是各部分的Deadline：

1. 井字棋的基础框架 2019/5/4
2. 感知器的框架 2019/5/12
3. 误差反向传播算法 2019/5/19

如果你跟着我学习，你需要的基础知识有：

* Python的基础语法，numpy库的大致了解
* 偏导数

写完这个后，我会整理成一份论文，作为选修课的作业。

```flow
gameStart=>start: 开始游戏
newBoard=>operation: 新建棋盘
isWin=>condition: 是否有赢家
isFull=>condition: 是否下满了
inMove=>inputoutput: 输入
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
