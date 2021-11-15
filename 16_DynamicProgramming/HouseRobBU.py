def HouseRob(houses,index):
    lst = [0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):
        lst[i]= max(houses[i]+lst[i+2],lst[i+1])
    return lst[0]
    

houses = [6,7,1,30,8,2,4]
print(HouseRob(houses,0))
