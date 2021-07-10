import math
import numpy as np
import matplotlib.pyplot as plt

x0 = 1 # 開始値
A = 1 # 状態行列
B = 0 # 入力行列
C = 1 # 出力行列
G = 1 # プロセス雑音行列
δx2 = 1 # システムノイズの大きさ (標準偏差1, 分散1)
δy2 = 2 # 観測ノイズの大きさ （標準偏差√2, 分散2）
w = math.sqrt(δx2) #システムノイズ
v = math.sqrt(δy2) #観測ノイズ
x = [x0]
xhat = [x0]
y = []
yhat = []
e = []

P = (δx2+math.sqrt((δx2**2)+4*δx2*δy2))/(2*δx2)
M = P/(δy2+P)
print(f'M={M}')

for k in range(256):
    i = 0
    np.random.seed(k)
    x.append(A*x[len(x)-1] + B*i + G*w*np.random.randn())
    y.append(C*x[len(x)-1] + v*np.random.randn())

    xhatp = xhat[len(xhat)-1]
    yhat.append(xhatp)
    xhat.append(xhatp + M*(y[len(y)-1] - yhat[len(yhat)-1]))
    e.append(x[len(x)-1] - xhat[len(xhat)-1])


plt.plot(np.array(range(len(x))),np.array(x))
plt.title("$x[k]$")
plt.xlabel("$k$")
plt.ylabel("$x[k]$")
plt.show()
plt.clf()
plt.plot(np.array(range(len(y))),np.array(y))
plt.title("$y[k]$")
plt.xlabel("$k$")
plt.ylabel("$y[k]$")
plt.show()
plt.clf()
plt.plot(np.array(range(len(xhat))),np.array(xhat))
plt.title("$\hat{x}[k]$")
plt.xlabel("$k$")
plt.ylabel("$\hat{x}[k]$")
plt.show()
plt.clf()
plt.plot(np.array(range(len(e))),np.array(e))
plt.title("$error(x[k]-\hat{x}[k])$")
plt.xlabel("$k$")
plt.ylabel("$e[k]$")
plt.show()