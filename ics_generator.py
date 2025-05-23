from pelican import readers
from pelican.settings import DEFAULT_CONFIG
import glob
import os
import datetime

import ics
from dateutil import tz

from pelicanconf import OUTPUT_PATH, PATH

EVENTS_PATH = f"{PATH}/pages/events"
OUTPUT_ICS = f"{OUTPUT_PATH}/hpcmaths_seminars.ics"

reader = readers.RstReader(settings=DEFAULT_CONFIG.copy())

calendar = ics.Calendar(creator="HPC@Maths")

for event_file in glob.glob(f"{EVENTS_PATH}/*.rst"):
    content, metadata = reader.read(event_file)

    event = ics.Event()
    # event.replace_timezone(tzinfo=tz.gettz("Europe/Paris"))
    if 'speaker' in metadata:
        event.summary = f"{metadata['title']} - {metadata['speaker']}"
    else:
        event.summary = f"{metadata['title']}"
    event.description = f"More information: https://initiative-hpc-maths.gitlab.labos.polytechnique.fr/site/pages/{os.path.splitext(os.path.basename(event_file))[0]}.html"
    d = datetime.datetime(
        year=metadata['date'].year,
        month=metadata['date'].month,
        day=metadata['date'].day,
        hour=metadata['date'].hour,
        minute=metadata['date'].minute,
        second=metadata['date'].second,
        tzinfo=tz.gettz("Europe/Paris")
    )
    event.begin = d
    event.end = d + datetime.timedelta(hours=1)
    event.location = metadata['place']

    calendar.events.append(event)

with open(OUTPUT_ICS, "w", newline='') as f:
    f.write("\n".join([line.replace('/ics.py/2020.1/', '')
            for line in calendar.serialize().split(r"\n")]))
