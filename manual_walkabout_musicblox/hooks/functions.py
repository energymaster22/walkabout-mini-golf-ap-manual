import os
import csv

def get_courses():

    courses = []
    data = os.path.join(os.path.dirname(os.getcwd()), "data\\meta\\courses.csv")

    with open(data) as courseFile:
        reader = csv.reader(courseFile)

        for course in reader:
            courses.append(course)

    return courses
