ras=float(input())
oil=float(input())
pay=float(input())
d=ras/100*oil
print(f'Топливо:{d:.2f}')
print(f"Стоимость:{d*pay:.2f}")