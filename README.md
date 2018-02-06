# Arris Events
Collects event logs from an Arris cable modem and prints them to stdout

By default consumer Arris consumer modems expose a web interface on `192.168.100.1`. This script pulls the events from that interface and outputs them to stdout so they can be monitored or processed by another system.

### Usage
##### Native
Install requirements

```pip install -r requirements.txt```

Run it

```python arris_events.py```

##### Docker

To use the version on Docker Hub:

```docker run -it --rm mjrsnyder/arris_events```

To build and run it locally:

```docker build -t arris_events .```

```docker run -it --rm arris_events```

### Contributing

Pull requests and suggestions welcome!
