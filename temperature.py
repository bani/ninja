from ninja.api import NinjaAPI, Watcher
from ninja.devices import TemperatureSensor, HumiditySensor
from datetime import datetime
from universal import universal_analytics
import settings

api = NinjaAPI(settings.ACCESS_TOKEN)

temp = TemperatureSensor(api, settings.TEMP)
humi = HumiditySensor(api, settings.HUMI)

def sendTempCelsius(inst, temperature):
    universal_analytics(webproperty=settings.WEBPROPERTY, category='QuantifiedHome', action='Temperature', ln=str(int(temperature.c)), lv=int(temperature.c))

def sendRelHumidity(inst, humidity):
    universal_analytics(webproperty=settings.WEBPROPERTY, category='QuantifiedHome', action='Humidity', ln=str(int(humidity)), lv=int(humidity))

temp.onHeartbeat(sendTempCelsius)
humi.onHeartbeat(sendRelHumidity)

temp.heartbeat()
humi.heartbeat()
