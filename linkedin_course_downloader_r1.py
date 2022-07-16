import os
import pandas as pd


DF = pd.read_csv("course_list.csv")

try:
    for ind in DF.index :

        course_link = str(DF['link'][ind])
        course_slug = str(course_link[course_link.index("/") + 28: course_link.index("?")])
        
        os.system(f"llvd -c {course_slug} --cookies --caption -r 720")


finally:
    pass

