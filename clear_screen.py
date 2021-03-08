import logging

from waveshare_epd import epd2in13_V2

logging.basicConfig(level=logging.INFO)

try:
    epd = epd2in13_V2.EPD()
    logging.info("clearing screen")

    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    logging.info("Goto Sleep...")
    epd.sleep()

except Exception as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd.module_exit()

exit()
