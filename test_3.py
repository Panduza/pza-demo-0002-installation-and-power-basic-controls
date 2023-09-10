from panduza import Client, Bpc, Core

ADDR="localhost"
PORT=1883

power_channel = Bpc(addr=ADDR, port=PORT, topic="pza/default/Hanmatek_Hm310t/bpc")

power_channel.current.value.set(0)

Max = 30
i = Max 
while True:

    if i < 0:
        i = Max 

    power_channel.voltage.value.set(i)
    i -= 1
    
