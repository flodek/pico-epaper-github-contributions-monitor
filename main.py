# Micropython GitHub statistic extractor
# MIT License Copyright (c) 2023 Volodymyr Shumara
# Thanks to
# https://github.com/petus/ePaper_micropython_libs_RaspberryPiPico
# https://github.com/mcauser/micropython-waveshare-epaper
# https://github.com/ayoy/micropython-waveshare-epd

from machine import Pin, SPI, I2C, deepsleep
import epaper2in9b #import ePaper 2.9" b/w/r
import monaco16bold #import font
import gitstat

COLORED = 1
UNCOLORED = 0
w = 128
h = 296

last_upd=''
count = ''
try:
    last_upd, count = gitstat.get_github_stat('SSID', 'WIFI_PWD', 'GITHUB_USERNAME')
except:
    pass

#SPI pins
dc = Pin(8)
cs = Pin(9)
rst = Pin(12)
busy = Pin(13)

# SPI
spi=SPI(1)
spi.init(baudrate=4000_000)

# ePaper
epd = epaper2in9b.EPD(spi, cs, dc, rst, busy) # Init ePaper | CLK GP6, MOSI GP7
epd.init()
epd.set_rotate(3)

# create frames
fb_size = int(w * h / 8)
frame_black = bytearray(fb_size)
frame_red = bytearray(fb_size)

epd.clear_frame(frame_black, frame_red)

# write strings to the buffer
epd.display_string_at(frame_black, 5, 10, "Last upt: " + last_upd, monaco16bold, COLORED)
epd.display_string_at(frame_red, 5, 40, "Contribs: " + count, monaco16bold, COLORED)

# display the frame
epd.display_frame(frame_black, frame_red)

#sleeps
epd.sleep()

#deep sleeps
deepsleep(1800000)
