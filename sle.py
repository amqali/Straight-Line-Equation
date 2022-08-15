import math

def straight_line():

    # two coordinate points for straight line graph. 
    
    x1,y1 = input("X-Axis for Point A: "), input("Y-axis for Point A: ")
    x2,y2 = input("X-Axis for Point B: "), input("Y-axis for Point B: ")
    

    # stores into list for type number check
    
    input_num = [x1,y1,x2,y2]
    new_num = []

    # if it is in fraction form, convert to decimal.
    # then add into new_num list.
    
    for i in input_num:
        if '/' in i:
            x = i.split('/')
            y = int(x[0])/int(x[1])
            new_num.append(y)

    # if it is not in fractional form , just add to new_num list.
    
        elif '/' not in i:
            z = int(i)
            new_num.append(z)

    # calculate slope and intercept
    
    slope = round((new_num[1]-(new_num[3]))/(new_num[0]-(new_num[2])),3)
    intercept = round((-1*(slope*(new_num[0]))+(new_num[1])),3)

    # print out the straight-line-equation. 
    
    if intercept < 0:
        print(f'y = {slope}x {intercept}')
            
    else:
        print(f'y = {slope}x +{intercept}')


# calling the function

straight_line()
