import main
import time

while True:
    j = main.run()
    print("The Current Temp: " + str(j["tempf"]) + "F")
    print("The Current Humidity: " + str(j["humidity"]) + "%")
    print("\n" * 2)
    time.sleep(4)