import os
from io import TextIOWrapper
import zipfile
import csv

def get_courses():

    courses = []
    print("Directory")
    print(os.path.abspath(os.getcwd()))

    with zipfile.ZipFile('custom_worlds\\manual_walkabout_musicblox.apworld') as apworld:
        with apworld.open('manual_walkabout_musicblox/data/meta/courses.csv', 'r') as courseFile:
            reader = csv.reader(TextIOWrapper(courseFile, 'utf-8'))

            for course in reader:
                courses.append(course)

    return courses