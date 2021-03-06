#!/usr/bin/env python3
from snipsowm.snipsowm import SnipsOWM
from hermes_python.hermes import Hermes
import datetime as dt
from dateutil.parser import parse

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def weather_temperature_handler(hermes, intentMessage):

      # Determine datetime
      datetime = None
      if snips.intent.forecast_start_datetime:
        datetime = snips.intent.forecast_start_datetime[0]

      if isinstance(datetime, snips.types.InstantTime):
        datetime = (datetime.datetime).replace(tzinfo=None)
      elif isinstance(datetime, snips.types.TimeInterval):
        datetime = (datetime.end).replace(tzinfo=None)

      # Determine granularity
      granularity = None
      if datetime:  # We have an information about the date.
        now = dt.datetime.now().replace(tzinfo=None)
        delta_days = abs((datetime - now).days)
        if delta_days > 10: # There a week difference between today and the date we want the forecast.
          granularity = 2 # Give the day of the forecast date, plus the number of the day in the month.
        elif delta_days > 5: # There a 10-day difference between today and the date we want the forecast.
          granularity = 1 # Give the full date
        else:
          granularity = 0 # Just give the day of the week
      else:
        granularity = 0

      locality = None
      try:
        locality = snips.intent.forecast_locality \
          or snips.intent.forecast_country \
          or snips.intent.forecast_region \
          or snips.intent.forecast_geographical_poi

        if locality:
          locality = locality[0]
      except Exception:
        pass

      snips.skill.speak_temperature(snips, locality, datetime, granularity)



def weather_condition_handler(hermes, intentMessage):

      # Determine datetime
      datetime = None

      if snips.intent.forecast_start_datetime:
        datetime = snips.intent.forecast_start_datetime[0]

      if isinstance(datetime, snips.types.InstantTime):
        datetime = (datetime.datetime).replace(tzinfo=None)
      elif isinstance(datetime, snips.types.TimeInterval):
        datetime = (datetime.end).replace(tzinfo=None)


      # Determine granularity
      granularity = None
      if datetime:  # We have an information about the date.
        now = dt.datetime.now().replace(tzinfo=None)
        delta_days = abs((datetime - now).days)
        if delta_days > 10: # There a week difference between today and the date we want the forecast.
          granularity = 2 # Give the day of the forecast date, plus the number of the day in the month.
        elif delta_days > 5: # There a 10-day difference between today and the date we want the forecast.
          granularity = 1 # Give the full date
        else:
          granularity = 0 # Just give the day of the week
      else:
        granularity = 0

      # Determine condition
      condition_name = None
      try:
        condition_name = snips.intent.forecast_condition_name[0] if snips.intent.forecast_condition_name else None
      except Exception:
        pass

      snips.intent.forecast_locality = snips.intent.forecast_locality[0] if snips.intent.forecast_locality else None
      snips.intent.forecast_region = snips.intent.forecast_region[0] if snips.intent.forecast_region else None
      snips.intent.forecast_country = snips.intent.forecast_country[0] if snips.intent.forecast_country else None
      snips.intent.forecast_geographical_poi = snips.intent.forecast_geographical_poi[0] if snips.intent.forecast_geographical_poi else None

      print "cond: {}, datetime: {}, Locality: {}, granularity: {}".format(condition_name, datetime, snips.intent.forecast_locality, granularity)
      snips.skill.speak_condition(snips, condition_name, datetime, granularity=granularity, Locality=snips.intent.forecast_locality, Region=snips.intent.forecast_region, Country=snips.intent.forecast_country, POI=snips.intent.forecast_geographical_poi)

def weather_forecast_handler(hermes, intentMessage):

      # Determine datetime
      datetime = None

      if snips.intent.forecast_start_datetime:
        datetime = snips.intent.forecast_start_datetime[0]

      if isinstance(datetime, snips.types.InstantTime):
        datetime = (datetime.datetime).replace(tzinfo=None)
      elif isinstance(datetime, snips.types.TimeInterval):
        datetime = (datetime.end).replace(tzinfo=None)

      # Determine granularity
      granularity = None
      if datetime:  # We have an information about the date.
        now = dt.datetime.now().replace(tzinfo=None)
        delta_days = abs((datetime - now).days)
        if delta_days > 10: # There a week difference between today and the date we want the forecast.
          granularity = 2 # Give the day of the forecast date, plus the number of the day in the month.
        elif delta_days > 5: # There a 10-day difference between today and the date we want the forecast.
          granularity = 1 # Give the full date
        else:
          granularity = 0 # Just give the day of the week
      else:
        granularity = 0

      # No condition in this intent so initialized to None
      condition_name = None

      snips.intent.forecast_locality = snips.intent.forecast_locality[0] if snips.intent.forecast_locality else None
      snips.intent.forecast_region = snips.intent.forecast_region[0] if snips.intent.forecast_region else None
      snips.intent.forecast_country = snips.intent.forecast_country[0] if snips.intent.forecast_country else None
      snips.intent.forecast_geographical_poi = snips.intent.forecast_geographical_poi[0] if snips.intent.forecast_geographical_poi else None

      print "cond: {}, datetime: {}, Locality: {}, granularity: {}".format(condition_name, datetime, snips.intent.forecast_locality, granularity)
      snips.skill.speak_condition(snips, condition_name, datetime, granularity=granularity, Locality=snips.intent.forecast_locality, Region=snips.intent.forecast_region, Country=snips.intent.forecast_country, POI=snips.intent.forecast_geographical_poi)

def weather_item_handler(hermes, intentMessage):

      # Determine datetime
      datetime = None

      if snips.intent.forecast_start_datetime:
        datetime = snips.intent.forecast_start_datetime[0]

      if isinstance(datetime, snips.types.InstantTime):
        datetime = (datetime.datetime).replace(tzinfo=None)
      elif isinstance(datetime, snips.types.TimeInterval):
        datetime = (datetime.end).replace(tzinfo=None)

      # Determine granularity
      granularity = None
      if datetime:  # We have an information about the date.
        now = dt.datetime.now().replace(tzinfo=None)
        delta_days = abs((datetime - now).days)
        if delta_days > 10: # There a week difference between today and the date we want the forecast.
          granularity = 2 # Give the day of the forecast date, plus the number of the day in the month.
        elif delta_days > 5: # There a 10-day difference between today and the date we want the forecast.
          granularity = 1 # Give the full date
        else:
          granularity = 0 # Just give the day of the week
      else:
        granularity = 0

      # Determine item
      try:
        item_name = snips.intent.forecast_item[0] if snips.intent.forecast_item else None
      except Exception:
         pass

      snips.intent.forecast_locality = snips.intent.forecast_locality[0] if snips.intent.forecast_locality else None
      snips.intent.forecast_region = snips.intent.forecast_region[0] if snips.intent.forecast_region else None
      snips.intent.forecast_country = snips.intent.forecast_country[0] if snips.intent.forecast_country else None
      snips.intent.forecast_geographical_poi = snips.intent.forecast_geographical_poi[0] if snips.intent.forecast_geographical_poi else None

      print "cond: {}, datetime: {}, Locality: {}, granularity: {}".format(item_name, datetime, snips.intent.forecast_locality, granularity)
      snips.skill.speak_item(snips, item_name, datetime, granularity=granularity, Locality=snips.intent.forecast_locality, Region=snips.intent.forecast_region, Country=snips.intent.forecast_country, POI=snips.intent.forecast_geographical_poi)

      
if __name__ == "__main__":
     with Hermes(MQTT_ADDR) as h:
        h.subscribe_intent("searchWeatherForecastTemperature", weather_temperature_handler)\
        h.subscribe_intent("searchWeatherForecastCondition", weather_condition_handler)\
        h.subscribe_intent("searchWeatherForecastItem", weather_item_handler)\
        h.subscribe_intent("searchWeatherForecast", weather_forecast_handler)\
         .start()
