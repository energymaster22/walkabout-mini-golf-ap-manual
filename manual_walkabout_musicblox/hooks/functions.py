import os
from io import TextIOWrapper
import zipfile
import csv
from sys import platform

def get_courses():

    courses = []

    userplatform = 'custom_worlds\\manual_walkabout_musicblox.apworld' if platform == "win32" else 'Archipelago/worlds/manual_walkabout_musicblox.apworld'


    with zipfile.ZipFile(userplatform) as apworld:
        with apworld.open('manual_walkabout_musicblox/data/meta/courses.csv', 'r') as courseFile:
            reader = csv.reader(TextIOWrapper(courseFile, 'utf-8'))

            for course in reader:
                courses.append(course)

    return courses


def check_course_active(subj, coursesActive): #Check if the course is selected within the yaml options. Always returns true as a placeholder.
    
    if subj.get('category'):
        if isinstance(subj.get('category')[0], str):
            if len(subj.get('category')[0]) == 2:    
                if subj.get('category')[0] in coursesActive:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return True
    else:
        return True