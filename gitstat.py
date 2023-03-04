"""
MicroPython GitHub statistic monitor
MIT License Copyright (c) 2023 Volodymyr Shumara
"""

import time
import network
import urequests as requests
import ujson
import math

wlan = None
status = None
def wifi_connector(ssid, password):
    global wlan, status
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(2)

    # Handle connection error
    if wlan.status() != 3:
        return None
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
        return True

def get_github_stat(ssid, password, gitnik, timezone='Europe/Amsterdam'):
    count = 'error'
    last_upd = 'error'
    weekday = {
        'Sunday': 0,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
    }

    if wifi_connector(ssid, password):
        try:
            print("sending...")
            
            # Get current date in Amsterdam timezone
            response = requests.get(f"https://www.timeapi.io/api/Time/current/zone?timeZone={timezone}")
            date = ujson.loads(response.text)
            last_upd = date['time']
            response.close()
            
            # Format date as yyyy-mm-dd
            formatted_date = f"{date['year']}-{date['month']:02d}-{date['day']:02d}"
            print(formatted_date)
            
            # Get day of the year
            response = requests.get(f"https://www.timeapi.io/api/Conversion/DayOfTheYear/{formatted_date}")
            day_of_year = int(ujson.loads(response.text)["day"])
            print(day_of_year)
            response.close()
            
            # Get day of the week for January 1st of the current year
            response = requests.get(f"https://www.timeapi.io/api/Conversion/DayOfTheWeek/{date['year']}-01-01")
            day_of_week = ujson.loads(response.text)['dayOfWeek']
            print(day_of_week)
            response.close()
            
            # Calculate the week number
            week_number = math.floor((weekday[day_of_week] + day_of_year) / 7)
            print(week_number)
            
            # Calculate the shift within the week (0 = Sunday, 1 = Monday, etc.)
            shift = weekday[date['dayOfWeek']]
            print(shift)
            
            # Get the number of commits for the given week and day
            response = requests.get(f"https://skyline.github.com/{gitnik}/{date['year']}.json")
            commits = ujson.loads(response.text)["contributions"][week_number]["days"][shift]["count"]
            print(commits)
            response.close()
            
            wlan.disconnect()
            wlan.active(False)
            
            count = str(commits)
            
        except Exception as e:
            count = 'github fetch err'
            print("wlan connection status =" + str(wlan.status()))
            print(e)
            pass
    else:
        count = 'wifi con err: ' + str(wlan.status())

    return last_upd, count
