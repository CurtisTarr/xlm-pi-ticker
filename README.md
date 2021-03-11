# xlm-pi-ticker
Basic python script for Raspberry Pi.
Which pulls `GBP` price of `XLM` from Coinbase, and displays it on an e-Paper display.

## Hardware
* raspberry pi zero wh
* Waveshare 2.13 inch e-Paper Display HAT
* micro SD card

## Requirements
* Setup Raspberry Pi.
* Make sure `dtparam=spi=on` is uncommented in `boot/config.txt`
* Run `sudo curl https://raw.githubusercontent.com/tarrcurtis/xlm-pi-ticker/main/setup.sh | sudo bash`

Or if you prefer run these commands on your Raspberry Pi to setup the environment (the script does this):

### Setup Pi:
* `sudo apt-get update`
* `sudo apt-get install git`
* `sudo apt-get install python3-pip`
  
### Setup waveshare e-Paper drivers:
* `sudo apt-get install python3-pil`
* `sudo apt-get install python3-numpy`
* `sudo apt-get install python3-spidev`
* `sudo apt-get install libopenjp2-7`
* `sudo pip3 install RPi.GPIO`
* `git clone https://github.com/waveshare/e-Paper.git` feel free to delete this after
* `sudo python3 e-Paper/RaspberryPi_JetsonNano/python/setup.py install`

### Setup project
* `sudo pip3 install requests`
* `sudo pip3 install matplotlib`
* `git clone https://github.com/tarrcurtis/xlm-pi-ticker.git`

## Running
* `cd xlm-pi-ticker`
* `python3 xlm_pi_ticker.py`
