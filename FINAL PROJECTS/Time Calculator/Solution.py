def add_time(start, duration, day = None):
    # Split the start time into hours, minutes, and period (AM/PM)
    hour, minutes = start.split(':')
    minute, period = minutes.split(' ')
    
    # Split the duration into hours and minutes
    durHour, durMinutes = duration.split(':')
    
    # Convert strings to integers
    hour, minute = int(hour), int(minute)
    durHour, durMinutes = int(durHour), int(durMinutes)
    
    # Initialize extraHour to handle minute overflow
    extraHour = 0
    newMinu = durMinutes + minute
    
    # If newMinu is 60 or more, adjust minutes and add to extraHour
    if newMinu >= 60:
        newMinu = 00 + (newMinu - 60)
        extraHour = 1
    
    # Ensure newMinu is two digits
    if len(str(newMinu)) == 1:
        newMinu = '0' + str(newMinu)
    
    # Calculate newHour by adding hours and extraHour
    newHour = hour + durHour + extraHour
    newDay = 0  # Initialize newDay to keep track of days passed
    
    # Handle case when newHour is exactly 12
    if newHour == 12:
        if period == "AM":
            period = 'PM'
        else:
            period = 'AM'
            newDay = 'next day'
    
    # Adjust newHour for the PM to AM transition and set newDay if needed
    if 24 > newHour > 12:
        newHour -= 12
        if period == "PM":
            period = "AM"
            newDay = 'next day'
        else:
            period = "PM"
    
    # Check if hour exceeds 24 and adjust accordingly
    newHour, newDay, period = hourCheck(newHour, newDay, period)

    # Initialize testday for day name if provided
    testday = ''
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # If day is provided, calculate the new day of the week
    if day is not None:
        day = day.capitalize()
        if day in week:
            day_index = week.index(day)
            new_day_index = (day_index + newDay) % 7
            testday = ', ' + week[new_day_index]
        
        # Return the formatted time with day and day count
        if newDay == 0:
            return f'{newHour}:{newMinu} {period}{testday}'
        elif newDay == 1 or newDay == 'next day':
            return f'{newHour}:{newMinu} {period}{testday} (next day)'
        else:
            return f'{newHour}:{newMinu} {period}{testday} ({newDay} days later)'

    # Return the formatted time without day if day is not provided
    if newDay == 0:
        return f'{newHour}:{newMinu} {period}'
    elif newDay == 1 or newDay == 'next day':
        return f'{newHour}:{newMinu} {period} (next day)'
    else:
        return f'{newHour}:{newMinu} {period} ({newDay} days later)'
    
def hourCheck(hour, newDay, period):
    # If hour exceeds 24, adjust the hour and increment newDay
    if hour > 24:
        hour = 0 + (hour - 24)
        if period == "PM":
            period = "AM"
            newDay += 1
            return hourCheck(hour, newDay + 1, period)
        else:
            period = "AM"
            return hourCheck(hour, newDay + 1, period)
    
    # If hour exceeds 12, adjust the hour
    if hour > 12:
        hour -= 12
    
    return hour, newDay, period

# Example call to the function
print(add_time('3:30 PM', '2:12', 'Monday'))
