# task1
# from datetime import *
# def hallowen(dt):
#     ht = datetime.strptime(dt, "%Y/%m/%d")
#     if ht.month == 10 and ht.day == 31:
#         print("Bonfire toffee")
#     else:
#         print("toffee")
# hallowen(input())
# task2

# from datetime import datetime

# def centuryyear(dt):
#     ht = datetime.strptime(dt, "%Y")
#     c = (ht.year - 1) // 100 + 1
#     print(c)
# centuryyear(input())

# task3
# from datetime import datetime, timedelta
# def after_n_months(year, months):
#     if year is None:
#         return "year missing"
#     elif months is None:
#         return "month missing"
#     ht = year + (months // 12)
#     return ht
# print(after_n_months(2020, 24))

# task4
# from datetime import datetime
# def format_date(dt):
#     ht = datetime.strptime(dt, "%m/%d/%Y")
#     return ht.strftime("%Y%d%m")
# print(format_date(input())) 

# task5
# from datetime import datetime

# def santa(a):
#     dt = datetime.strptime(a, "%Y %m %d")
#     if dt.month == 12 and dt.day == 24:
#         return True
#     else:
#         return False
# print(santa(input()))

# task6
# from datetime import datetime
# def getdate(a):
#     dt = datetime.strptime(a, "%m/%d/%Y")
#     return dt.strftime("%A")
# print(getdate(input()))
