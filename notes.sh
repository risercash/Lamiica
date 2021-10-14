#!/usr/bin/env bash
#Installation for 16.04
-1- SmsNumber
ssh -i c:\Users\Alice\Downloads\tlgam.pem ubuntu@3.21.234.180
-3- tlgam
ssh -i c:\Users\Alice\Downloads\tlgam.pem ubuntu@13.59.200.113
-2- tstmoney
ssh ubuntu@18.221.47.136 -i tstmoney.pem
-3- Goosebot
ssh ubuntu@13.58.2.39 -i NewKey.pem

sudo rm -r tlgam
git clone 'https://dbogak@mail.ru@github.com/dbogak/tlgam.git'
cd tlgam
nano .env
docker-compose up --build
sudo sh docker_install.sh

cd /home/ubuntu/tlgamcd
cntr+c stop bot

