function utf8_to_b64(str) {
  return window.btoa(unescape(encodeURIComponent(str)));
}

function event_to_ics( summary, t_start, t_end, place, abstract, url )
{
    return `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
CALSCALE:GREGORIAN
TIMEZONE-ID:Europe/Paris
X-WR-TIMEZONE:Europe/Paris
BEGIN:VEVENT
DTSTART:${t_start}
DTEND:${t_end}
URL;VALUE=URI:${url}
SUMMARY:${summary}
LOCATION:${place}
DESCRIPTION:${abstract}
END:VEVENT
END:VCALENDAR
`
}

function event_uri(summary, t_start, t_end, place, abstract, url)
{
    return "data:text/calendar;base64," + utf8_to_b64(event_to_ics(summary, t_start, t_end, place, abstract, url));
}

function add_ics_link(elm, summary, t_start, t_end, place, abstract, url)
{
    if ( t_end === t_start )
    {
        h_index = 9;
        hour = Number(t_end.substring(h_index, h_index + 2));
        t_end = t_end.substring(0, h_index) + (hour + 1).toString().padStart(2, "0") + t_end.substring(h_index + 2);
    }
    elm.href = event_uri(summary, t_start, t_end, place, abstract, url);
}

