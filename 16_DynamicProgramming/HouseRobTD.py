def HouseRob(houses,index,memo):
    if index >= len(houses):
        return 0
    if index not in memo:
        steal1stHouse = houses[index] + HouseRob(houses,index+2,memo)
        skip1stHouse = HouseRob(houses,index+1,memo)
        memo[index] = max(steal1stHouse,skip1stHouse)
    return memo[index]

houses = [6,7,1,30,8,2,4]
print(HouseRob(houses,0,{}))
