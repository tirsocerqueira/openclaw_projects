---
name: "morning-briefing"
description: "Generates a daily morning briefing with calendar events, a song recommendation, and reminders."
---

# Morning Briefing

This skill ensures the user starts their day with a clear agenda, a boost of energy, and a reminder of their commitments.

## Workflow

Every morning at 9:00 AM, execute the following steps:

### 1. Agenda Fetching

- Use the `gog` (Google Workspace) tool to retrieve all calendar events for the current date.
- If events exist, list them with their start times.
- If no events are found, use the phrase "Sin eventos hoy 🎉".

### 2. Energy Boost (Music)

- Select **one** energetic or motivating song.
- **Genre Rotation**: Rotate between Rock, Hip-Hop, Electronic, and Pop to maintain variety.
- **Motivation**: Provide the [Artist – Song Title] and a single sentence explaining why this song is perfect for starting the work day.

### 3. Reminder Extraction

- Search `MEMORY.md` and the most recent daily logs in `memory/YYYY-MM-DD.md` for keywords like "reminder", "task", "todo", "remember to", or "pendiente".
- Extract a concise list of pending items.
- If nothing is found, use "Sin recordatorios pendientes".

### 4. Delivery

- Format the final message exactly as follows:

🌅 *Buenos días! Aquí tu resumen del día:*

📅 *Agenda de hoy:*

- [Event 1 at Time]
- [Event 2 at Time]

(or "Sin eventos hoy 🎉")

🎵 *Canción para arrancar:*

- [Artist – Song Title]
- [One sentence on why it's energizing]

✅ *Recordatorios:*

- [Reminder 1]
- [Reminder 2]

(or "Sin recordatorios pendientes")

¡Que tengas un gran día! 💪

- Send the result via the `message` tool to the `telegram` channel.
