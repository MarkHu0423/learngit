import random
secret = random.randint(1,3)
# 模拟电脑随机出拳
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
        # 列举出所有输赢情况

    else:
        print("请输入1到3的数字.")
        number = secret
print("----------------Game Over!----------------")