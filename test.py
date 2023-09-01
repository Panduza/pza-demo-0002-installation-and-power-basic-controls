from panduza import Client, Bpc


power_channel = Bpc(addr="192.168.1.4", port=1883)

power_channel.voltage.value.set(2.3)
