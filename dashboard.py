import logging
import time
import os

from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw

logging.basicConfig(level=logging.INFO)
epd = epd2in13_V2.EPD()
try:
    logging.info("Clearing display")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
except Exception as e:
    logging.error(e)
    exit()

running = True
first_pass=True
while running:
    try:
        stream = os.popen('cat /sys/class/thermal/thermal_zone0/temp')
        output = stream.read()
        stream.close()
        cpu_temp = str(round(float(output) / 1000, 1)) + "'C"
        print(cpu_temp)

        stream = os.popen('vcgencmd measure_temp')
        output = stream.read()
        stream.close()
        qpu_temp = output.strip('temp=')
        print(qpu_temp)

        curr_time = time.strftime('%H:%M')
        day = time.strftime('%a')
        date = time.strftime('%d')
        month = time.strftime('%b')
        year = time.strftime('%Y')

        image = Image.new('1', (epd.width, epd.height), 255)
        draw = ImageDraw.Draw(image)
        draw.text((10, 30), curr_time, fill = 0)
        draw.text((10, 50), day, fill = 0)
        draw.text((10, 70), date, fill = 0)
        draw.text((10, 90), month, fill = 0)
        draw.text((10, 110), year, fill = 0)
        draw.text((10, 200), "CPU " + cpu_temp, fill = 0)
        draw.text((10, 220), "GPU " + qpu_temp, fill = 0)

        if first_pass:
            epd.displayPartBaseImage(epd.getbuffer(image))
            epd.init(epd.PART_UPDATE)
            first_pass = False
        else:
            epd.displayPartial(epd.getbuffer(image))

        print('sleeping')
        time.sleep(60)

    except Exception as e:
        logging.error(e)
        running = False

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        running = False

epd.sleep()
exit()
