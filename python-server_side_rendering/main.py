#!/usr/bin/env python3
from task_00_intro import generate_invitations

# Leer el template desde template.txt
with open("template.txt", "r") as file:
    template_content = file.read()

# Definir lista de invitados
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Llamar a la función
generate_invitations(template_content, attendees)
