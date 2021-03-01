import datetime

def server_cost(d1, m1, y1, d2, m2, y2):
    start_date= datetime.date(day=d1,month=m1,year=y1)
    end_date=datetime.date(day=d2,month=m2,year=y1)
    day_difference=(end_date-start_date).days

    return 

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
    print(server_cost(6,6,2020,9,6,2020))

8589073722