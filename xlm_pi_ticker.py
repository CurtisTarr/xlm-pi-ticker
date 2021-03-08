import requests
import logging
import time
import matplotlib.pyplot

from collections import deque
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw

Y_TICKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

matplotlib.use('agg')
logging.basicConfig(level=logging.INFO)
running = True
first_pass = True

ticks = deque(maxlen=60)
for tick in Y_TICKS:
    ticks.append(0)

epd = epd2in13_V2.EPD()
try:
    logging.info("Clearing display")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
except Exception as e:
    logging.error(e)
    exit()

while running:
    try:
        logging.info("Getting XLM price in GBP")
        r = requests.get(url="https://api.coinbase.com/v2/prices/XLM-GBP/buy")
        data = r.json()
        xlm_price =  data['data']['amount']
        logging.info("XLM current price is £" + xlm_price)
        ticks.append(float(xlm_price))

        fig = matplotlib.pyplot.figure()
        plt = fig.add_subplot(1, 1, 1)
        plt.plot(Y_TICKS, ticks, linewidth=3)
        plt.axis('off')
        fig.canvas.draw()

        image = Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
        fig.close()
        image = image.convert('1')
        image = image.resize((epd2in13_V2.EPD_HEIGHT, epd2in13_V2.EPD_WIDTH))
        draw = ImageDraw.Draw(image)
        draw.text((5, 5), "XLM=£" + xlm_price, fill=0)

        if first_pass:
            epd.displayPartBaseImage(epd.getbuffer(image))
            epd.init(epd.PART_UPDATE)
            first_pass = False
        else:
            epd.displayPartial(epd.getbuffer(image))

        time.sleep(3)

    except Exception as e:
        logging.error(e)
        running = False

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        running = False

epd.sleep()
exit()
