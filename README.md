# Linkedin Learning Course Downloader

### Requirements:
 - Access to Linkedin Learning (Linkedin Premium Membership - Used to fill data in cookies.txt)
 - Course Link which you want to download (Example: https://www.linkedin.com/learning/sql-essential-training-3?u=74415068)
 - Python with llvd(pip install llvd) packege.
  
### Process
 - Use [course_list.csv](https://github.com/papercodeIN/Linkedin_learning_Course_Downloader/blob/main/course_list.csv) file and fill it with the course link (course you want to download) and save it.
 - Use [cookies.txt](https://github.com/papercodeIN/Linkedin_learning_Course_Downloader/blob/main/cookies.txt) file and fill two perameter "li_at" & "JSESSIONID" and save this file.
 - use [linkedin_course_downloader_r2.py](https://github.com/papercodeIN/Linkedin_learning_Course_Downloader/blob/main/linkedin_course_downloader_r2.py) python code, it will download each course from "[course_list.csv](https://github.com/papercodeIN/Linkedin_learning_Course_Downloader/blob/main/course_list.csv)", It will automatically zip downloaded course and delete course folder from current path.

### Beinfits
 - Code will resume course download from last interrupt.
