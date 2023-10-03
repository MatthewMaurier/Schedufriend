import csv
import requests
import time
from bs4 import BeautifulSoup

catalogue_url = "https://apps.ualberta.ca/catalogue"
departmenturls = []

# # # # COMMENT OUT IF DEPARTMENTURLS.CSV already exists # # #  
# # commented out the part of the code that generates a CSV file containing all department URLs, waste of time if that file already exists, uncomment to regenerate 
# response = requests.get(catalogue_url)
# faculty_urls = []
# # Ensure the request was successful
# if response.status_code == 200:
#     main_page_soup = BeautifulSoup(response.text, 'html.parser')
#     ul_tags = main_page_soup.find_all('ul')
#     for i in ul_tags:
#         if "Faculty of" in i.get_text():
#                 faculty_links = i
#                 break
#     for li in faculty_links.find_all('li'):
#          a_tag = li.find('a')
#          if a_tag and a_tag.has_attr('href'):
#               faculty_urls.append((requests.compat.urljoin(catalogue_url, a_tag['href'])))
    

# else:
#     print("Failed to retrieve the webpage")
#     exit()




# for faculties in faculty_urls:
#     AH_soup = BeautifulSoup((requests.get(faculties)).text,'html.parser')
#     ul_tags = AH_soup.find_all('ul')
#     departmentlinks = ul_tags[-1]
    
#     for li in departmentlinks.find_all('li'):
#             a_tag = li.find('a')
#             if a_tag and a_tag.has_attr('href'):
#                 departmenturls.append((requests.compat.urljoin(catalogue_url, a_tag['href'])))

# filename = "coursedatafinder/departmenturls.csv"
# with open(filename, 'w', newline='') as file:
#     # Create a writer object from csv module
#     csv_writer = csv.writer(file)
    
#     # Write links to the csv file, each link in a new row
#     for link in departmenturls:
#         csv_writer.writerow([link])
# # # # COMMENT OUT IF DEPARTMENTURLS.CSV already exists # # #  
#



# # # # comment section out if departmenturls.csv was just created # # #
# #opens departmenturls.csv and creates an array containing each url
# with open('coursedatafinder/departmenturls.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # Assuming each row has one column, which contains the URL
#         url = row[0]  # Extract the URL from the row
#         departmenturls.append(url)
# # # # comment section out if departmenturls.csv was just created # # #


# # # # comment out section if classcodes.csv already exists # # #
# i = 0
# href_deconstructed = []
# for department in departmenturls:
    
#     coursesoup = BeautifulSoup(requests.get(department).text,'html.parser') 
#     content = coursesoup.find('div', class_ = 'content')
#     cards = content.find_all('div', class_ = 'card-body border-bottom') 
   

#     for card in cards:
#         href_deconstructed.append(0)
#         a_tag = card.find('a')
#         p_tag = card.find('p')
#         print(a_tag)
#         #print(p_tag)
#         if a_tag.has_attr('href'): 
#             href_deconstructed[i] = a_tag['href'].split('/')
#             href_deconstructed[i].append(a_tag['href'])
#             i = i+1

# with open('coursedatafinder/classcodes.csv', 'w', newline = '') as file:
#    csv_writer = csv.writer(file)
#    for course in href_deconstructed:
#        csv_writer.writerow([course[3],course[4],requests.compat.urljoin(catalogue_url, course[5])])

# # # # comment out section if classcodes.csv already exists # # #

# # comment section out if departmenturls.csv was just created # # #
#opens departmenturls.csv and creates an array containing each url

coursedata = []
with open('coursedatafinder/classcodes.csv', 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        coursedata.append(0)
        # Assuming each row has one column, which contains the URL
        coursedata[i] = row  # Extract the URL from the row
        i = i+1
# # # comment section out if departmenturls.csv was just created # # #
#print(coursedata[10557])

for i in range(11215):
    courseid = i
    coursesoup = BeautifulSoup((requests.get(coursedata[courseid][2])).text,'html.parser')
    content = coursesoup.find('div', class_ = 'content')
    description_container = content.find('div', class_ = 'container')
    lectureslabsseminars_container = content.find_all('div', class_ = 'container')[1]
    terms_container = content.find('div', class_ ='row m-0')
    course_name = content.find('h1').get_text(strip=True)
    course_load = content.find('h5').get_text(strip=True).replace('★','*')
    course_faculty = (description_container.find_all('p'))[0].get_text(strip=True)
    try:
        course_description = (description_container.find_all('p'))[1].get_text(strip=True)
    except IndexError:
           course_description = "" 
    course_term = []
    for term in terms_container.find_all('a'):
        course_term.append(term['href'])

    lectures_fall = []
    lectures_winter = []
    lectures_spring = []
    lectures_summer = []
    termcounter=0
    caseifnolectures = 0
    if "Lectures" in lectureslabsseminars_container.get_text(strip = True):
        caseifnolectures = 1
        if ("#1850" in course_term or "#1846" in course_term) and "Lectures" in lectureslabsseminars_container.find_all('div', class_ = "card")[0].find('div', class_ = "card-body").get_text(strip = True):
            print("DSADHASGDKASDASD")
            i = 0
            for lecture in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find('tbody').find_all('tr'):
                lectures_fall.append(lecture.find('div'))
                i = i+1
            lectures_fall = [lecture.get_text(strip=True) for lecture in lectures_fall if lecture is not None]
            termcounter+=1
        else:
            pass


        if "#1860" in course_term or "#1848" in course_term:
            i = 0
            for lecture in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find('tbody').find_all('tr'):
                lectures_winter.append(lecture.find('div'))
                i = i+1
            lectures_winter = [lecture.get_text(strip=True) for lecture in lectures_winter if lecture is not None]
            termcounter+=1
        else:
            pass


        if "#1870" in course_term:
            i = 0
            for lecture in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find('tbody').find_all('tr'):
                lectures_spring.append(lecture.find('div'))
                i = i+1
            lectures_spring = [lecture.get_text(strip=True) for lecture in lectures_spring if lecture is not None]
            termcounter+=1
        else:
            pass


        if "#1880" in course_term:
            i = 0
            for lecture in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find('tbody').find_all('tr'):
                lectures_summer.append(lecture.find('div'))
                i = i+1
            lectures_summer = [lecture.get_text(strip=True) for lecture in lectures_summer if lecture is not None]
            termcounter+=1
        else:
            pass
    else:
        pass
    labs_fall = []
    labs_winter = []
    labs_spring = []
    labs_summer = []
    if "Labs" in lectureslabsseminars_container.get_text(strip = True):
        termcounter = 0
        
        if "#1850" in course_term and "Labs" in lectureslabsseminars_container.find_all('div', class_ = "card")[0].get_text(strip = True):
            i = 0
            for lab in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                labs_fall.append(lab.find('div'))
                i = i+1
            labs_fall = [lab.get_text(strip=True) for lab in labs_fall if lab is not None]
            termcounter+=1
        elif "#1850" in course_term and "Labs" not in lectureslabsseminars_container.find_all('div', class_ = "card")[0].get_text(strip = True):    
            termcounter+=1
        else:
            pass

        try:
            if "#1860" in course_term and "Labs" in lectureslabsseminars_container.find_all('div', class_ = "card")[1].get_text(strip = True):
                i = 0
                for lab in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                    labs_winter.append(lab.find('div'))
                    i = i+1
                labs_winter = [lab.get_text(strip=True) for lab in labs_winter if lab is not None]
                termcounter+=1
            else:
                pass
        except IndexError:
            if "#1860" in course_term:
                i = 0
                for lab in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                    labs_winter.append(lab.find('div'))
                    i = i+1
                labs_winter = [lab.get_text(strip=True) for lab in labs_winter if lab is not None]
                termcounter+=1
            else:
                pass

        
        if "#1870" in course_term:
            i = 0
            for lab in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                labs_spring.append(lab.find('div'))
                i = i+1
            labs_spring = [lab.get_text(strip=True) for lab in labs_spring if lab is not None]
            termcounter+=1
        else:
            pass

        
        if "#1880" in course_term:
            i = 0
            for lab in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                labs_summer.append(lab.find('div'))
                i = i+1
            labs_summer = [lab.get_text(strip=True) for lab in labs_summer if lab is not None]
            termcounter+=1
        else:
            pass
        caseifnolectures += 1    
    else:
        pass

    sems_fall = []
    sems_winter = []
    sems_spring = []
    sems_summer = []
    if "Seminars" in lectureslabsseminars_container.get_text(strip = True):
        termcounter = 0
        
        if "#1850" in course_term and "Seminars" in lectureslabsseminars_container.find_all('div', class_ = "card")[0].get_text(strip = True):
            i = 0
            try:
                for sem in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                    sems_fall.append(sem.find('div'))
                    i = i+1
                sems_fall = [sem.get_text(strip=True) for sem in sems_fall if sem is not None]
                termcounter+=1
            except IndexError:
                for sem in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[0].find_all('tr'):
                    sems_fall.append(sem.find('div'))
                    i = i+1
                sems_fall = [sem.get_text(strip=True) for sem in sems_fall if sem is not None]
                termcounter+=1
        elif "#1850" in course_term and "Seminars" not in lectureslabsseminars_container.find_all('div', class_ = "card")[0]:
            termcounter+=1
        else:
            pass

        
        if "#1860" in course_term:
            i = 0
            try:
                for sem in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                    sems_winter.append(sem.find('div'))
                    i = i+1
                sems_winter = [sem.get_text(strip=True) for sem in sems_winter if sem is not None]
                termcounter+=1
            except IndexError:
                termcounter+=1
        else:
            pass

        
        if "#1870" in course_term:
            i = 0
            for sem in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                sems_spring.append(sem.find('div'))
                i = i+1
            sems_spring = [sem.get_text(strip=True) for sem in sems_spring if sem is not None]
            termcounter+=1
        else:
            pass

        
        if "#1880" in course_term:
            i = 0
            for sem in (lectureslabsseminars_container.find_all('div', class_ = 'card-body')[termcounter]).find_all('tbody')[caseifnolectures].find_all('tr'):
                sems_summer.append(sem.find('div'))
                i = i+1
            sems_summer = [sem.get_text(strip=True) for sem in sems_summer if sem is not None]
            termcounter+=1
        else:
            pass
    else:
        pass


    coursedata[courseid].append(course_name)
    coursedata[courseid].append(course_load)
    coursedata[courseid].append(course_faculty)
    coursedata[courseid].append(course_description)
    coursedata[courseid].append(course_term)
    coursedata[courseid].append(lectures_fall)
    coursedata[courseid].append(lectures_winter)
    coursedata[courseid].append(lectures_spring)
    coursedata[courseid].append(lectures_summer)
    coursedata[courseid].append(labs_fall)
    coursedata[courseid].append(labs_winter)
    coursedata[courseid].append(labs_spring)
    coursedata[courseid].append(labs_summer)
    coursedata[courseid].append(sems_fall)
    coursedata[courseid].append(sems_winter)
    coursedata[courseid].append(sems_spring)
    coursedata[courseid].append(sems_summer)

    print(coursedata[courseid][2])


with open('coursedatafinder/coursedata.csv', 'w', newline = '') as file:
    csv_writer = csv.writer(file)
    header = ["department", "course_code", "url", "course_name","course_load","course_faculty","course_description","course_term","lectures_fall","lectures_winter","lectures_spring","lectures_summer","labs_fall","labs_winter","labs_spring","labs_summer","sems_fall","sems_winter","sems_spring","sems_summer"]
    csv_writer.writerow(header)
    for course in coursedata:
        csv_writer.writerow(course)

