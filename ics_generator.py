from pelican import readers
from pelican.settings import DEFAULT_CONFIG
import glob

import ics

from pelicanconf import OUTPUT_PATH, PATH

EVENTS_PATH = f"{PATH}/pages/events"
OUTPUT_ICS = f"{OUTPUT_PATH}/hpcmaths_seminars.ics"

reader = readers.RstReader(settings=DEFAULT_CONFIG.copy())

calendar = ics.Calendar()

for event_file in glob.glob(f"{EVENTS_PATH}/*.rst"):
    content, metadata = reader.read(event_file)

    event = ics.Event()
    if 'speaker' in metadata:
        event.description = f"{metadata['title']} - {metadata['speaker']}"
    else:
        event.description = f"{metadata['title']}"
    # event.description = metadata['shortdescription']
    event.begin = metadata['date']
    event.location = metadata['place']
    event.duration = dict({"hours": 1})

    calendar.events.add(event)

with open(OUTPUT_ICS, "w", newline='') as f:
    f.write(calendar.serialize())
