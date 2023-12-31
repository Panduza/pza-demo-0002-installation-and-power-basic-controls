import time
from panduza import Bpc

ADDR="localhost"
PORT=1883

power_channel = Bpc(addr=ADDR, port=PORT, topic="pza/default/Hanmatek_Hm310t/bpc")

power_channel.voltage.value.set(5)
power_channel.current.value.set(1.234)

power_channel.enable.value.set(True)
time.sleep(5)
power_channel.enable.value.set(False)
