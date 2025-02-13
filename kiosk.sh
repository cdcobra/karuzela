#!/bin/bash

unclutter -idle 0.1 -root &
firefox --private-window --kiosk=http://192.168.32.177 &