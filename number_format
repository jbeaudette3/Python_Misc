def number_format(num):
    '''
    : 2024.09.26
    : does a lot of messy formatting of numbers
    : works with $1 -> $999 Billion
    : (Trillion+ not included)
    :
    : To call this function:
    : x = 412346.456
    : number_format(x)
    : -> $412.3K
    '''
    pn = '-' if num < 0 else ''     # pn = positive/negative
    num = abs(num)
    length = len(str(int(num)))
    
    if length < 4:
        num = round(num, 0)
        num = f'{pn}${abs(num):.0f}'
    elif length < 7:
        num = round(num, -1)
        num = f'{pn}${abs(num):,.0f}'.replace(',', '.')[:-1] + 'K'
    elif length < 10:
        num = round(num, -4)
        num = f'{pn}${abs(num):,.0f}'.replace(',', '.')[:-5] + 'M'
    elif length < 13:
        num = round(num, -7)
        num = f'{pn}${abs(num):,.0f}'.replace(',', '.')[:-9] + 'B'
    else:
        return num
    
    return num
