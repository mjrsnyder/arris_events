import pandas
from datetime import datetime

url = "http://192.168.100.1/cgi-bin/event_cgi"

latest_event_id = 0
latest_event_time = datetime.utcfromtimestamp(0)
last_event_index = 0

pandas.set_option('display.max_colwidth', -1)

while True:
  logs = pandas.read_html(io=url, header=0)[1]

  logs['Date Time'] = pandas.to_datetime(logs['Date Time'], format="%m/%d/%Y %H:%M")

  try:
    last_event_index = logs.loc[
      (logs['Date Time'] == latest_event_time) & 
      (logs['Event ID'] == latest_event_id)].index[0]
  except:
    last_event_index = 0

  latest_event_time = logs.tail(1).values[0][0]
  latest_event_id = logs.tail(1).values[0][1]

  new_logs = logs[logs.index > last_event_index]

  if new_logs.shape[0] > 0:
    print(new_logs.to_string(header=False, index=False))

