def aquarium():
    long = int(input())
    width = int(input())
    height = int(input())
    percent = float(input())

    capacity = long * width * height
    capacity_need_water = capacity / 1000
    need_liter = capacity_need_water * (1 - percent / 100)

    print(need_liter)

aquarium()