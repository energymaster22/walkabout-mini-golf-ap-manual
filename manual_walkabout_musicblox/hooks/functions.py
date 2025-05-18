import os
import csv

def get_courses():

    courses = []
    data = os.path.abspath(os.path.join(os.getcwd(), "data\\meta\\courses.csv"))

    with open(data) as courseFile:
        reader = csv.reader(courseFile)

        for course in reader:
            courses.append(course)

    return courses