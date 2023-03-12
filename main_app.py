pip install streamlit requests json pandas

import requests
import json
import pandas as pd
import streamlit as st

st.title('Udemy Free Courses')

url = 'https://www.udemy.com/api-2.0/courses/?page_size=100&price=price-free'

response = requests.get(url)
json_data = json.loads(response.text)

courses = []

for course in json_data['results']:
    title = course['title']
    url = course['url']
    rating = course['rating']
    num_ratings = course['num_ratings']
    courses.append({'title': title, 'url': url, 'rating': rating, 'num_ratings': num_ratings})

df = pd.DataFrame(courses)

st.write(df)
