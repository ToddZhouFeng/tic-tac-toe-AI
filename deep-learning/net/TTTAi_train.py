# coding: utf-8
import sys, os
sys.path.append(os.pardir)

from two_layer_net import TwoLayerNet
import pickle, random
import numpy as np
import TTTFrame as t3f

def shuffle(board, clock, mirror):
    newboard=t3f.rotate(board, clock)
    newboard=t3f.mirror(board, mirror)
    return newboard

def shuffle_move(move, clock, mirror):
    newmove=t3f.rotate_move(move, clock)
    newmove=t3f.mirror_move(move, mirror)
    return newmove

file=open("database.pkl", "rb")
database=pickle.load(file)
x_train=[]
t_train=[]
for i in database:
    x_train.append(i[0])
    t_train.append(i[1])
"""
for i in database:
    x_train.append(i[0].flatten())
    target=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    target[i[1]]=1
    t_train.append(target)
"""
train_loss_list=[]
#下面几个是参数
learning_rate=1#学习率（每次调整的权值）
batch_size=5#每次训练使用的数据个数
iters_num=8000#训练次数
train_size=len(x_train)

network=TwoLayerNet(input_size=27, hidden_size=200, output_size=9)
all_loss=0
total=0
for i in range(iters_num):
    x_batch=[]
    t_batch=[]
    batch_mask = np.random.choice(train_size, batch_size)
    for j in batch_mask:
        x=x_train[j]
        t=t_train[j]

        clock=random.randint(0,3)
        mirror=random.randint(1,2)
        x=shuffle(x, clock, mirror)
        t=shuffle_move(t, clock, mirror)

        x_batch.append(x.flatten())
        target=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        target[t]=1
        t_batch.append(target)
    """
    for j in batch_mask:
        x_batch.append(x_train[j])
        t_batch.append(t_train[j])
    """

    x_batch=np.array(x_batch)
    t_batch=np.array(t_batch)
    grad = network.gradient(x_batch, t_batch)
    #grad = network.numerical_gradient(x_batch, t_batch)#太慢了

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss=network.loss(x_batch, t_batch)
    
    all_loss+=loss
    total+=1
    if total==200:
        print(all_loss/total)
        if all_loss/total<0.04:
            learning_rate=0.1#学习率
        elif all_loss/total>0.05 and all_loss/total<0.06:
            learning_rate=0.2#学习率
        all_loss=0
        total=0
    train_loss_list.append(loss)

file.close()
file=open("net.pkl", "wb")
pickle.dump(network, file)
file.close()
