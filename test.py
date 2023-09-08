from panduza import Client, Bpc, Core


# Core.EnableLogging()

# client = Client(url="localhost", port=1883)
# client = Client(url="192.168.1.4", port=1883)
# client.connect()
# interfaces = client.scan_interfaces()

# print(interfaces)



power_channel = Bpc(addr="192.168.1.4", port=1883, topic="pza/default/Hanmatek_Hm310t/bpc")



# power_channel.voltage.value.set(2.3)
# power_channel.voltage.value.set(1)
# power_channel.voltage.value.set(2)
# power_channel.voltage.value.set(3)


import time
import numpy as np

def set_voltage(power_channel, start_voltage, end_voltage, increment):
    for voltage in np.arange(start_voltage, end_voltage + increment, increment):
        voltage = round(voltage, 2)
        print(voltage)

        try:
            power_channel.voltage.value.set(voltage)
            time.sleep(1)
        except:
            print("error !", voltage)

start_voltage = 0
end_voltage = 3
increment = 0.01

set_voltage(power_channel, start_voltage, end_voltage, increment)
