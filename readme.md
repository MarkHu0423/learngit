# 剪刀石头布的python实现  
## 1. 代码主体  
```python  
import random
secret = random.randint(1,3)
number = secret

print("----------------Game Start!----------------")
while number == secret :
    number = int (input("石头请按1,剪刀请按2,布请按3:"))   
    if secret == number:
        print("平局,再来")
        secret = random.randint(1,3)
        number = secret

    elif secret == 1 and number == 2:
        print("电脑出石头,你输了")
    elif secret == 1 and number == 3:
        print("电脑出石头,你赢了")

    elif secret == 2 and number == 3:
        print("电脑出剪刀,你输了")
    elif secret == 2 and number == 1:
        print("电脑出剪刀,你赢了")

    elif secret == 3 and number == 1:
        print("电脑出布,你输了")
    elif secret == 3 and number == 2:
        print("电脑出布,你赢了")

    else:
        print("请输入1到3的数字.")
        number = secret
print("----------------Game Over!----------------")
```  
## 2. 代码解释  
首先定义1，2，3分别对应石头，剪刀，布，再通过random函数生成的1，2，3模拟电脑的随机打出的姿势，最后用elif语句列举出所有可能遇到的胜负情景。  
## 3. 代码问题  
在玩家获胜后游戏就直接结束，可以添加一个循环来询问玩家获胜后是否继续游戏等等