import random

player=int(input("《石头剪刀布-单机版》\n 1 代表 ‘石头’\n 2代表‘剪刀’\n 3代表‘布’ \n 请出招吧：\n "))
computer=random.randint(1,3)
print("本局玩家出 %s ，电脑出 %s" %(player,computer))


if((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("厉害哇，玩家胜利！")
elif player == computer:
    print("心有灵犀一点通，平局，哈哈")
else:
    print("再接再厉哦，电脑胜利了！")

