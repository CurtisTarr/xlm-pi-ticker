#!/bin/sh

echo "----------------------------"
echo "Installing System Requirements"
echo "----------------------------"
apt-get update
apt-get install git -y
apt-get install python3-pip -y

echo "----------------------------"
echo "Installing waveshare e-Paper drivers"
echo "----------------------------"
apt-get install python3-pil -y
apt-get install python3-numpy -y
apt-get install python3-spidev -y
apt-get install libopenjp2-7 -y
pip3 install RPi.GPIO
git clone https://github.com/waveshare/e-Paper.git
python3 e-Paper/RaspberryPi_JetsonNano/python/setup.py install
rm -r e-Paper/

echo "----------------------------"
echo "Installing project requirements"
echo "----------------------------"
pip3 install requests
pip3 install matplotlib

echo "----------------------------"
echo "Cloning project"
echo "----------------------------"
git clone https://github.com/tarrcurtis/xlm-pi-ticker.git

echo "----------------------------"
echo "Project setup :)"
echo "----------------------------"
