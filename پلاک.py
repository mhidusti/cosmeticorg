t = int(input())  # تعداد تست‌ها

for _ in range(t):
    x, y = map(int, input().split())  # مختصات خانه
    
    # محاسبه شماره پلاک خانه
    if x == 0 and y == 0:
        print(1)
    elif x == 0:
        print(2 * abs(y))
    elif y == 0:
        print(2 * abs(x) - 1)
    else:
        if abs(x) > abs(y):
            if x > 0:
                print(4 * x * x - 2 * x + y)
            else:
                print(4 * x * x + y)
        else:
            if y > 0:
                print(4 * y * y - 3 * y + x)
            else:
                print(4 * y * y + x)
