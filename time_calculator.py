days = {'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6}
key_list = list(days.keys())
val_list = list(days.values())

def add_time(start, duration, *args):
    new_hour = 0
    new_mins = 0
    count = 0
    day = ''
    
    time,period = start.split()
    hour,mins = time.split(':')   
    dhour,dmins = duration.split(':')
    
    dhour,dmins,hour,mins = int(dhour),int(dmins),int(hour),int(mins)
    dperiod = period
    
    if(args):
        day = args[0]
    
    while(dhour > 24):
        dhour -= 1
        dmins += 60

    new_mins = mins + dmins
    while(new_mins >= 60):
        new_hour += 1
        new_mins -= 60  
    new_hour += hour + dhour
    
    while(new_hour >=24):
        new_hour -= 24
        count += 1

    while(new_hour >= 12):
        if(new_hour > 12):
            new_hour -= 12
        if(period == 'AM'):
            dperiod = 'PM'
        else:
            count += 1
            dperiod = 'AM'
        if(new_hour == 12):
            break

    temp_time = str(new_hour),'{:0>2}'.format(str(new_mins))
    d_time = ':'.join(temp_time)
    temp_time = d_time,dperiod
    new_time = ' '.join(temp_time)

    new_time = append_days(new_time, count, day)
    return new_time

def append_days(new_time, count, day):
    if(day):
        index = 0
        index = (days[day.lower()] + count) % 7
        new_day = key_list[val_list.index(index)].capitalize()
        new_time = new_time + ', ' + new_day
    if(count > 0):
        if(count > 1):
            new_time = new_time + ' (' + str(count) + ' days later)'
        else:
            new_time = new_time + ' (next day)' 
    return new_time