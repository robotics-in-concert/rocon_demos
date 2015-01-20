#!/usr/bin/env sh

export CONCERT_AUTO_ENABLE_SERVICES="[admin, pickup_delivery]"
export CONCERT_AUTO_ENABLE_WORKFLOWS="--web --engine --workflow pickup_delivery_wf"
#export CONCERT_WEBSERVER_ADDRESS="webapp.robotconcert.org"
export CONCERT_WEBSERVER_ADDRESS="toyweb.cafe24.com:3008"

