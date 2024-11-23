def is_leap_year(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False


def dates(date: str):
    date = date.split('.')
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    last_date = [int(date[0]) - 1, int(date[1]), int(date[2])]
    next_date = [int(date[0]) + 1, int(date[1]), int(date[2])]

    if last_date[0] == 0:
        last_date[1] -= 1
        if last_date[1] == 0:
            last_date[2] -= 1
            last_date[1] = 12
            last_date[0] = 31
        else:
            if last_date[1] in day_31:
                last_date[0] = 31
            elif last_date[1] in day_30:
                last_date[0] = 30
            else:
                if is_leap_year(last_date[2]):
                    last_date[0] = 29
                else:
                    last_date[0] = 28

    if (next_date[1] in day_31) and next_date[0] == 32:
        next_date[0] = 1
        next_date[1] += 1
        if next_date[1] == 13:
            next_date[2] += 1
            next_date[1] = 1
    elif (next_date[1] in day_30) and next_date[0] == 31:
        next_date[0] = 1
        next_date[1] += 1
        if next_date[1] == 13:
            next_date[2] += 1
            next_date[1] = 1
    else:
        if is_leap_year(next_date[2]):
            if next_date[0] == 30:
                next_date[0] = 1
                next_date[1] += 1
        else:
            if next_date[0] == 29:
                next_date[0] = 1
                next_date[1] += 1

    returning_last_date = '{:02}.{:02}.{}'.format(*last_date)
    returning_next_date = '{:02}.{:02}.{}'.format(*next_date)
    return returning_last_date, returning_next_date


print(dates('31.03.2016'))