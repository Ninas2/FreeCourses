import streamlit as st
import requests
from bs4 import BeautifulSoup
import json

st.title('Free Udemy Courses')

url = 'https://www.udemy.com/courses/free/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

course_divs = soup.find_all('div', {'class': 'course-card--main-content--3xEIw'})

courses = []
for course_div in course_divs:
    course_title = course_div.find('h4').text
    course_url = 'https://www.udemy.com' + course_div.find('a')['href']
    course_img_url = course_div.find('img')['src']
    course_description = course_div.find('p').text
    course = {
        'title': course_title,
        'url': course_url,
        'img_url': course_img_url,
        'description': course_description
    }
    courses.append(course)

st.write(json.dumps(courses))
