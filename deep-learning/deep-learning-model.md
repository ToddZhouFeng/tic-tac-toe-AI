
* content
{:toc}
>摘要：深度学习是一种机器学习方法。对比传统的机器学习方法，深度学习无需人为设计特征值，可自动提取特征值。利用这一特点，我们将在不输入规则的情况下，利用多层感知器模型，通过监督学习，来构建一个井字棋的神经网络。



# 1 相关模型

## 1.1 M-P模型

&emsp;&emsp;M-P模型（The McCulloch-Pitts neural model）是一种模仿神经元的模型，其基本组成为：输入$x$、权重$w$、阈值$h$、输出$y$，类似于神经元的树突-轴突结构。输入输出的关系为：若输入 $x$ 的加权和大于阈值 $h$ ，则输出$1$，否则输出$0$。利用函数可以表示为：
$$
y=f( \sum_{i=1}^n w_i x_i - h)\\
\begin{equation}
f(x)={\rm sgn}(x)= 
\begin{cases}
1 &x\geq0\\
0 &x<0
\end{cases}
\end{equation}
$$
&emsp;&emsp;利用M-P模型，我们可以将与、或等逻辑运算表述出来。以逻辑或为例，取$w_1=1$、$w_2=1$、$h=0.5$，当输入$x_1$、$x_2$中至少有一个为$1$时，输出$1$，当输入全为$0$时，输出$0$。

&emsp;&emsp;但M-P模型只能表示线性可分问题，无法表示线性不可分问题。这是因为对于含有$n$个未知量的线性方程$\sum_{i=1}^n \, w_ix_i-h=0$，其基础解系为$n-1$维，只能将$n$维空间线性划分成两部分。以二维为例，若取$x_1$为横坐标，$ x_2 $为纵坐标，则$ w_1 x_1 + w_2x_2 - h=0$只能表示一条直线，即只能将二维空间线性划分成两个部分。

&emsp;&emsp;M-P模型的另一个问题是：需要人为设定参数，无法通过输出与期望值的差异来调整参数。



## 1.2 多层感知器

&emsp;&emsp;为了解决线性不可分问题，人们提出了多层感知器模型（multilayer perceptron），多层感知器采用三层结构：输入层、中间层、输出层，各层之间的输入输出与M-P模型相同。为了让各层之间的连接权重能够自动调整，我们采用的是误差反向传播算法。

&emsp;&emsp;误差反向传播算法的目标是：寻找使误差达到最小值的权重。其基本步骤为

1. 正向计算出输出
2. 根据输出与期望的误差，反向逐层调整连接权值
3. 重复1. 2.步骤，直到取得误差的极小值

&emsp;&emsp;权重的调整主要使用梯度下降法，即通过向梯度的反方向调整权重$w$，让 误差$E$ 逐步下降到极小值。其基本的数学推导如下：
$$
\text{误差}E\, \text{与权重}w_i \text{构成一个多元函数}E=g(w_1,w_2,\cdots,w_n)\\
\text{权重的调整值}\Delta w_i \text{可以表示为:} \Delta w_i = -\eta \frac{\partial E}{\partial w_i}\\
$$

$$
\text{而} E \text{通过误差函数确定:}E=\frac{1}{2}\sum_{i=1}^n \left| r_i - y_i \right|^2\\
y \text{通过激活函数} f(u) \text{确定:}y=f(u)=sgn(u),\, u=\sum_{i=1}^n w_i x_i\\
\text{有时候，为了让}f(u)\text{可求导，我们采用sigmoid函数:}f(u)=\frac{1}{1+{\rm e}^u}
$$

$$
\text{综上，我们可以通过求导的链式法则求出}\frac{\partial E}{\partial w_i}: \\
\frac{\partial E}{\partial w_i} =\frac{\partial E}{\partial y}\frac{\partial y}{\partial u} \frac{\partial u}{\partial w_i} = -(r-y)y(1-y)x_i\\
\text{从而}w_i\leftarrow w_i-\eta \frac{\partial E}{\partial w_i}
$$

&emsp;&emsp;上面只是梯度下降法对应单层感知器的公式，我们可与类比推导出对应多层感知器的情况。



# 实现

在net文件中，通过TTTAi_train.py来获得一个神经网络，然后再通过TTTAi.py来与Ai对弈。其中TTTAi.py有几个参数可由你来定义：

~~~python
batch_size=5 #每次训练用几个数据
iters_num=5000 #训练次数
network=TwoLayerNet(input_size=27, hidden_size=200, output_size=9) 
#神经网络的输入层，中间层，输出层。只能改中间层的神经数
~~~

