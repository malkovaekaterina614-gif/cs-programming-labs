t=7384
hours=t//3600 #цел.деление
minutes=(t%3600)//60
second=t%60 #остаток берет
print(f'{hours:02d}:{minutes:02d}:{second:02d}')