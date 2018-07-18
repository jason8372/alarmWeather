import time
import datetime
import pygame
import telegram
from weather import Weather, Unit


###########Function that sets time#####################
def inputnumbers():
    setalarm = input('Set alarm at: hr:min')
    sethour, setmin = setalarm.split(":")
#you have to turn string into integer, which is possible by using float to integer
    sethour = int(sethour)
    setmin = int(setmin)
    if  sethour<1 or sethour > 24 or 0 > setmin or 59 < setmin:
        print("Wrong input")
        inputnumbers()

    while True:
        time.sleep(1)

        now = datetime.datetime.now()
        if now.hour == sethour and now.minute == setmin:
            alarmring(now.hour,now.minute)
            break


def alarmring(a,b):
    if a<10:
        a = "0" + str(a)
    if b<10:
        b= "0" + str(b)
    print("it is ", a,":",b)
#########GET WEATHER##############
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('seongnam')
    condition = location.condition
    date=condition.date
    temp=condition.temp
    description=condition.text

###########SEND MESSAGE IN CHAT##################
    token = '493675434:AAE_8w9jiA5IzDR3GJ7squRwsmzocD7vwQE'
    bot = telegram.Bot(token=token)
    chatid = '651442323'
    bot.send_message(chat_id=chatid, text="TIME TO WAKE UP")
    bot.send_message(chat_id=chatid, text=date)
    bot.send_message(chat_id=chatid, text=temp+"도입니다")
    bot.send_message(chat_id=chatid, text=description)

    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load('C:\\Users\\SDC\\Downloads\\rightnow.ogg')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0)
#Clock tick in while loop is used to check if the music has finished
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        clock.tick(10)

inputnumbers()







