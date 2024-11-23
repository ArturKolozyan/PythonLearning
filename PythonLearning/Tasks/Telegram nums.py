num = str(input())  # 000 000 000


if len(num) > 6:
    num = num[:-3]
    m_or_k = 'M'
else:
    m_or_k = 'K'


if len(num) > 3:  # 7.0
    num = '{0:,}'.format(int(num)).replace(',', '.')
    num = num[:-1]
    if len(num) > 4:
        num = num[0:4]
    if num[-1] == '0' or num[-1] == '.':
        num = num[:-1]
        if num[-2:] == '.0':
            num = num[:-2]
    num = num + m_or_k


print(num)