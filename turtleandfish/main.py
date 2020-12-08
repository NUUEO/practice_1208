from turtleandfish import Turtle, Fishs
import  time
turtle = Turtle()
fishs = [Fishs() for i in range(10)]
print('遊戲開始！'.center(50,'*'))
while True:
    if turtle.power <= 0:
        print('烏龜沒有體力了')
        print('---------------------')
        print('魚兒獲勝')
        break
    elif len(fishs) == 0:
        print('魚被吃光了！')
        print('---------------------')
        print('烏龜獲勝')
        break
    else:
        turtle.move()
        for fish in fishs:
            fish.move()
            if turtle.x == fish.x and turtle.y == fish.y:
                turtle.eat()
                fishs.remove(fish)
                print('魚被烏龜吃了！')
                print(f'烏龜當前體力值為：{turtle.power}' )
        else:
            print(f'烏龜沒有吃到魚，烏龜體力值：{turtle.power}')
    time.sleep(0.1)



