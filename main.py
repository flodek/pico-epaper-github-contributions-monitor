import time
import network
import urequests as requests
from machine import Pin, SPI, deepsleep
import ujson
import math
import framebuf
import utime

ssid = ''
password = ''
gitnik = ''

# Display resolution
EPD_WIDTH       = 128
EPD_HEIGHT      = 296

RST_PIN         = 12
DC_PIN          = 8
CS_PIN          = 9
BUSY_PIN        = 13

class EPD_2in9_B:
    def __init__(self):
        self.reset_pin = Pin(RST_PIN, Pin.OUT)
        
        self.busy_pin = Pin(BUSY_PIN, Pin.IN, Pin.PULL_UP)
        self.cs_pin = Pin(CS_PIN, Pin.OUT)
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
        
        self.spi = SPI(1)
        self.spi.init(baudrate=4000_000)
        self.dc_pin = Pin(DC_PIN, Pin.OUT)
        
        self.buffer_black = bytearray(self.height * self.width // 8)
        self.buffer_red = bytearray(self.height * self.width // 8)
        self.imageblack = framebuf.FrameBuffer(self.buffer_black, self.width, self.height, framebuf.MONO_HLSB)
        self.imagered = framebuf.FrameBuffer(self.buffer_red, self.width, self.height, framebuf.MONO_HLSB)
        self.init()

    def digital_write(self, pin, value):
        pin.value(value)

    def digital_read(self, pin):
        return pin.value()

    def delay_ms(self, delaytime):
        utime.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        self.spi.write(bytearray(data))

    def module_exit(self):
        self.digital_write(self.reset_pin, 0)

    # Hardware reset
    def reset(self):
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)
        self.digital_write(self.reset_pin, 0)
        self.delay_ms(2)
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)


    def send_command(self, command):
        self.digital_write(self.dc_pin, 0)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([command])
        self.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([data])
        self.digital_write(self.cs_pin, 1)
        
    def ReadBusy(self):
        print('busy')
        self.send_command(0x71)
        while(self.digital_read(self.busy_pin) == 0):
            self.send_command(0x71)
            self.delay_ms(10)
        print('busy release')
        
    def TurnOnDisplay(self):
        self.send_command(0x12)
        self.ReadBusy()

    def init(self):
        print('init')
        self.reset()
        self.send_command(0x04)
        self.ReadBusy() #waiting for the electronic paper IC to release the idle signal

        self.send_command(0x00) #panel setting
        self.send_data(0x0f)    #LUT from OTP,128x296
        self.send_data(0x89)    #Temperature sensor, boost and other related timing settings

        self.send_command(0x61) #resolution setting
        self.send_data (0x80)
        self.send_data (0x01)
        self.send_data (0x28)

        self.send_command(0X50) #VCOM AND DATA INTERVAL SETTING
        self.send_data(0x77)    #WBmode:VBDF 17|D7 VBDW 97 VBDB 57
                                # WBRmode:VBDF F7 VBDW 77 VBDB 37  VBDR B7
        return 0
        
    def display(self):
        self.send_command(0x10)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(self.buffer_black[i + j * int(self.width / 8)])   
        self.send_command(0x13)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(self.buffer_red[i + j * int(self.width / 8)])   

        self.TurnOnDisplay()

    
    def Clear(self, colorblack, colorred):
        self.send_command(0x10)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(colorblack)
        self.send_command(0x13)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(colorred)
                                
        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0X02) # power off
        self.ReadBusy()
        self.send_command(0X07) # deep sleep
        self.send_data(0xA5)
        
        self.delay_ms(2000)
        self.module_exit()

wlan = None
status = None
def wifi_connector():
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

weekday = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}

msg = 'Contrib: '
last_upd = 'Last upd: '

if __name__=='__main__':
    if wifi_connector():
        try:
            print("sending...")
            
            # Get current date in Amsterdam timezone
            response = requests.get("https://www.timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam")
            date = ujson.loads(response.text)
            last_upd = last_upd + date['time']
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
            
            msg = msg + str(commits)
            
        except Exception as e:
            msg = 'github fetch err'
            print("wlan connection status =" + str(wlan.status()))
            print(e)
            pass
    else:
        msg = 'wifi con err: ' + str(wlan.status())
        
    epd = EPD_2in9_B()
    epd.Clear(0xff, 0xff)
    
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0xff)
    epd.imageblack.text(last_upd, 0, 10, 0x00)
    epd.imagered.text(msg, 0, 25, 0x00)
    epd.display()

    epd.delay_ms(2000)
    print("sleep")
    epd.sleep()

    deepsleep(1800000)
