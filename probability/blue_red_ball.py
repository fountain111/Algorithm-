import  numpy as np
import sys

# 1 = red,0 =blue

#三个相同的盒子里各有两个球，其中一个盒子里放了2个红球，一个盒子里放了2个红球，一个盒子里放了红球和蓝球各一个，
# 随机选择一个盒子后从中随机摸出一个球是红球，则这个和资历另一个球是红球队概率为

def blue_red_box(argv):

    box_1 = [1,1]
    box_2 = [0,0]
    box_3 = [1,0]
    box_list = [box_1,box_2,box_3]
    double_red = 0
    counts = 0
    for i in range(1000000):
        box_id = np.random.randint(1,4)
        seq = np.random.randint(0,2)

        balls = box_list[box_id-1]
        first_ball = balls[seq]
        second_ball = balls[1-seq]


        if first_ball==1:
            counts+=1
            if second_ball==1:
                double_red +=1
                prob = double_red/counts
                print(prob,i)

'''
假设有两箱同种零件：
第一箱内装有50件，其中10件一等品；
第二箱内30件，其中18件一等品。
现从两箱中随意挑选一箱，然后从箱中随机取出2个零件（不放回），试求：

1）先取出的零件是一等品的概率p；
2）在先取出的零件是一等品的条件下，第二次取出的零件仍然是一等品的条件概率q。

#1 = 一等品, 0=其他

'''

def components(q1=True,q2=True):
    box_1 = [1 for i in range(10)] + [0 for i in range(40)]
    box_2 = [1 for i in range(18)] + [0 for i in range(12)]

    box_list = [box_1, box_2]
    for box in [box_1, box_2]:
        np.random.shuffle(box)
    first_is_1_counts = 0

    for i in range(10000000):
        box_id = np.random.randint(0, 2)
        box = box_list[box_id]
        if q1:

            if box_id == 0:

                component_id = np.random.randint(0,50)
            else:
                component_id=np.random.randint(0,30)

            first_component =  box[component_id]

            if first_component==1:
                first_is_1_counts+=1
                print('question 1=',first_is_1_counts/i)

        if q2:






def main(argv):
    components()

if __name__ == '__main__':

    main(sys.argv)


