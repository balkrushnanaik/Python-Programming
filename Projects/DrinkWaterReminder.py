import time
from plyer import notification

while True:
    print("It's time to drink some water")
    notification.notify(title="Drink some water",message="You need to drink some water")
    time.sleep(3600)
