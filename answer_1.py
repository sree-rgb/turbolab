import datetime

def server_cost(d1, m1, y1, d2, m2, y2):
    start_date= datetime.date(day=d1,month=m1,year=y1)
    end_date=datetime.date(day=d2,month=m2,year=y1)
    day_difference=(end_date-start_date).days
    if day_difference > 365:
        return 20000
    if day_difference > 30:
        return 1000*(day_difference//30)
    if day_difference > 0:
        return 30*day_difference

    return 20

# if __name__ == '__main__':
#     d1M1Y1 = input().split()
#     d1 = int(d1M1Y1[0])
#     m1 = int(d1M1Y1[1])
#     y1 = int(d1M1Y1[2])

#     d2M2Y2 = input().split()
#     d2 = int(d2M2Y2[0])
#     m2 = int(d2M2Y2[1])
#     y2 = int(d2M2Y2[2])

#     result = server_cost(d1, m1, y1, d2, m2, y2)
#     print(str(result) + '\n')

if __name__ == '__main__':
    print(server_cost(6,6,2020,9,7,2020))

8589073722