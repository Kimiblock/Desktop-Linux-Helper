#!/bin/bash
if [ ! ${cardNumber} ]; then
    export ${cardNumber}=1
fi
while true; do
    sleep 4s
    status=`cat /sys/class/drm/card${cardNumber}/device/power_state`
    if [[ ${status} = 'D3cold' ]]; then
        sleep 1s
    else
        notify-send -u low -i /usr/share/icons/breeze/devices/64/audio-card.svg -c GPU -t 3000 '独立GPU已唤醒' "状态: ${status}"
        while [[ `cat /sys/class/drm/card${cardNumber}/device/power_state` = D0 ]]; do
            sleep 10s
        done
        notify-send -u low -i /usr/share/icons/breeze/devices/64/audio-card.svg -c GPU -t 3000 '独立GPU已关闭' "状态: `cat /sys/class/drm/card${cardNumber}/device/power_state`"
    fi
done
