year_price = int(input())

def basketballEquipment(year_price):
    basketball_shoes = year_price - (year_price * 40 / 100)
    basketball_outfit = basketball_shoes - (basketball_shoes * 20 / 100)
    basketball_ball = basketball_outfit * 1 / 4
    basketball_accessoar = basketball_ball * 1 / 5
    sum = year_price + basketball_shoes + basketball_outfit + basketball_ball + basketball_accessoar

    print("%.2f" % sum)

basketballEquipment(year_price)