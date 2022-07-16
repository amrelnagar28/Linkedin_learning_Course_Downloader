import os
import pandas as pd
import shutil

DF = pd.read_csv("course_list.csv")

try:
    for ind in DF.index :

        course_link = str(DF['link'][ind])
        course_slug = str(course_link[course_link.index("/") + 28: course_link.index("?")])

        
        if not os.path.exists(course_slug + ".zip"):

            print(f" +++ downloading course        : {course_slug} +++")
            
            os.system(f"llvd -c {course_slug} --cookies --caption -r 720")
            shutil.make_archive(course_slug, 'zip', course_slug)
            print(f" +++ course folder compressed  : {course_slug} +++")

            if os.path.exists(course_slug + ".zip"):
                shutil.rmtree(f'{course_slug}', ignore_errors=True)  # for read only files
                print(f" +++ course folder deleted     : {course_slug} +++ ")
            
            else:
                pass

        elif os.path.exists(course_slug + ".zip"):
            print(f" +++ course already downloaded : {course_slug} +++ ")
            

            try:
                shutil.rmtree(f'{course_slug}', ignore_errors=True)
                print(f" +++ course folder deleted     : {course_slug} +++ ")
                
            except:
                print(" --- course {} folder does not exist.")

        else:
            pass

finally:
    pass

