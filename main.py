__all__=(
    'seconds_to_str',
)

def second_to_str(seconds: int):
    days=seconds//86400

    if 10>days>0:
        d='0'+str(days)+'d'

    if days >= 10:
        d = str(days) + 'd'

    if days==0:
        d=''

    hours=(seconds%86400)//3600

    if 9>hours>0:
        h='0'+str(hours)+'h'

    if hours >= 10:
        h = str(hours) + 'h'

    if hours==0:
        h=''


    minutes=seconds%86400%3600//60

    if 9>minutes>0:
        m='0'+str(minutes)+'m'

    if minutes >= 10:
        m = str(minutes) + 'm'

    if minutes==0:
        m='00m'

    sec=seconds%86400%3600%60

    if 9>sec>0:
        s='0'+str(sec)+'s'

    if sec >= 10:
        s = str(sec) + 's'

    if sec==0:
        s='00s'

    result=d+h+m+s

    return (result)

print(second_to_str(20))
