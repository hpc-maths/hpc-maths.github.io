from pelican import readers
from pelican.settings import DEFAULT_CONFIG
import glob
import os
import datetime

import ics
from dateutil import tz

from pelicanconf import OUTPUT_PATH, PATH, SITE_DOMAIN, SITEURL

EVENTS_PATH = f"{PATH}/pages/events"
OUTPUT_ICS = f"{OUTPUT_PATH}/hpcmaths_seminars.ics"

reader = readers.RstReader(settings=DEFAULT_CONFIG.copy())

calendar = ics.Calendar(creator="HPC@Maths")
# Sorted so that the output does not depend on the filesystem order.
for event_file in sorted(glob.glob(f"{EVENTS_PATH}/*.rst")):
    content, metadata = reader.read(event_file)

    event = ics.Event()
    # The UID must stay the same from one build to the next, otherwise
    # subscribed calendars treat every event as new at each refresh.
    slug = os.path.splitext(os.path.basename(event_file))[0]
    event.uid = f"{slug}@{SITE_DOMAIN.split('://')[-1]}"
    # event.replace_timezone(tzinfo=tz.gettz("Europe/Paris"))
    if 'speaker' in metadata:
        event.summary = f"{metadata['title']} - {metadata['speaker']}"
    else:
        event.summary = f"{metadata['title']}"
    event.description = f"More information: {SITE_DOMAIN}{SITEURL}/pages/{slug}.html"
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

# Hints for subscribed clients. Not all of them honour these (Google ignores
# them), but Apple Calendar and Outlook do. RFC 5545 wants calendar properties
# before the components, so they are inserted right after the header instead of
# going through calendar.extra, which ics writes at the end of the file.
SUBSCRIPTION_HINTS = [
    "X-WR-CALNAME:Séminaires HPC@Maths",
    "REFRESH-INTERVAL;VALUE=DURATION:PT6H",
    "X-PUBLISHED-TTL:PT6H",
]

lines = calendar.serialize().replace('/ics.py/2020.1/', '').splitlines()
header_end = lines.index("BEGIN:VTIMEZONE")
lines[header_end:header_end] = SUBSCRIPTION_HINTS

with open(OUTPUT_ICS, "w", newline='', encoding="utf-8") as f:
    f.write("\r\n".join(lines) + "\r\n")
