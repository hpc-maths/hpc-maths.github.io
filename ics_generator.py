from pelican import readers
from pelican.settings import DEFAULT_CONFIG
import glob
import os

import ics

from pelicanconf import OUTPUT_PATH, PATH

EVENTS_PATH = f"{PATH}/pages/events"
OUTPUT_ICS = f"{OUTPUT_PATH}/hpcmaths_seminars.ics"

reader = readers.RstReader(settings=DEFAULT_CONFIG.copy())

calendar = ics.Calendar(creator="HPC@Maths")

for event_file in glob.glob(f"{EVENTS_PATH}/*.rst"):
    content, metadata = reader.read(event_file)

    event = ics.Event()
    event.replace_timezone("Europe/Paris")
    if 'speaker' in metadata:
        event.name = f"{metadata['title']} - {metadata['speaker']}"
    else:
        event.name = f"{metadata['title']}"
    event.description = f"More information: https://initiative-hpc-maths.gitlab.labos.polytechnique.fr/site/pages/{os.path.splitext(os.path.basename(event_file))[0]}.html"
    event.begin = metadata['date']
    event.location = metadata['place']
    event.duration = dict({"hours": 1})

    calendar.events.append(event)

with open(OUTPUT_ICS, "w", newline='') as f:
    f.write(calendar.serialize())
