import random
Computer = random.randint(1,3)
number = Computer
print("----------------Game Start!----------------")
while number == Computer :
    number = int (input("石头请按1,剪刀请按2,布请按3:"))   
    if Computer == number:
        print("平局,再来")
        Computer = random.randint(1,3)
        number = Computer
    elif Computer == 1 and number == 2:
        print("电脑出石头,你输了")
    elif Computer == 1 and number == 3:
        print("电脑出石头,你赢了")
    elif Computer == 2 and number == 3:
        print("电脑出剪刀,你输了")
    elif Computer == 2 and number == 1:
        print("电脑出剪刀,你赢了")
    elif Computer == 3 and number == 1:
        print("电脑出布,你输了")
    elif Computer == 3 and number == 2:
        print("电脑出布,你赢了")
    else:
        print("请输入1到3的数字.")
        number = Computer
print("----------------Game Over!----------------")