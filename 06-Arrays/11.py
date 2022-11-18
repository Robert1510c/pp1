import calendar

def month(n):
    array=[]
    if n>=1 and n<=12:
        array.append(calendar.month_name[n])
    return array

print(month(12))