# Counting Sundays

# Bruteforce. For the sake of consistency, assume we do not care about the days in the outer bounds.
def counting_sundays(m1 = 1, y1 = 1901, m2 = 12, y2 = 2000):
    day = 0
    total = 0
    for y in range(1900, y2 + 1):
        for m in range(1, 13):
            if y == y2 and m > m2: break
            day += months[m]
            if is_leap_year(y) and m == 2: day +=1
            day %= 7
            if ((y > y1) or (y == y1 and m > m1)) and day == 6: total += 1
    return total
    
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    return (not year%4) if year%100 else (not year%400)

'''
import datetime

# One-liner using datetime
def counting_sundays():
    return sum(1 for y in range(1901, 2001) for m in range(1, 13) if datetime.date(y, m, 1).weekday() == 6)

'''

def compute():
    return str(counting_sundays())

if __name__ == "__main__":
    print(compute())
