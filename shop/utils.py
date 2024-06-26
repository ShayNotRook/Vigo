import json
import os
from django.conf import settings

def load_about_us():
    file_path = os.path.join(settings.BASE_DIR, 'static', 'about_us.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get('about')