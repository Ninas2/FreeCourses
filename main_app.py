import requests
import json
import pandas as pd
import streamlit as st

st.title('Udemy Free Courses')

url = 'https://www.udemy.com/courses/free/'

response = requests.get(url)
 # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the free course titles and links on the page
        course_titles = []
        course_links = []
        for course in soup.find_all('div', {'class': 'course-list--container--3zXPS'}):
            title = course.find('div', {'class': 'course-list--course-title--2f7tE'}).text.strip()
            link = 'https://www.udemy.com' + course.find('a')['href']
            course_titles.append(title)
            course_links.append(link)

 # Create a pandas dataframe to store the course titles and links
        df = pd.DataFrame({'Course Title': course_titles, 'Course Link': course_links})
        
        # Return the dataframe
        return st.write(df)
    
    else:
        # If the request was unsuccessful, print an error message
        print('Error: Could not retrieve data from Udemy.')
        return None
# json_data = json.loads(response.text)

# courses = []

# for course in json_data['results']:
#     title = course['title']
#     url = course['url']
#     rating = course['rating']
#     num_ratings = course['num_ratings']
#     courses.append({'title': title, 'url': url, 'rating': rating, 'num_ratings': num_ratings})

# df = pd.DataFrame(courses)




# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import streamlit as st

# # Scraping function
# def scrape_udemy_free_courses():
#     # Udemy free courses URL
#     url = 'https://www.udemy.com/courses/free/'
    
#     # Send a GET request to the URL
#     response = requests.get(url)
    
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Find all the free course titles and links on the page
#         course_titles = []
#         course_links = []
#         for course in soup.find_all('div', {'class': 'course-list--container--3zXPS'}):
#             title = course.find('div', {'class': 'course-list--course-title--2f7tE'}).text.strip()
#             link = 'https://www.udemy.com' + course.find('a')['href']
#             course_titles.append(title)
#             course_links.append(link)
        
#         # Create a pandas dataframe to store the course titles and links
#         df = pd.DataFrame({'Course Title': course_titles, 'Course Link': course_links})
        
#         # Return the dataframe
#         return df
    
#     else:
#         # If the request was unsuccessful, print an error message
#         print('Error: Could not retrieve data from Udemy.')
#         return None

# # Streamlit app code
# def app():
#     st.title('Free Courses on Udemy')
#     st.write('This app scrapes all the free courses on Udemy.')
    
#     # Scrape the free courses data
#     df = scrape_udemy_free_courses()
    
#     # Check if the data was successfully retrieved
#     if df is not None:
#         st.write('Total Courses:', len(df))
#         st.table(df)
#     else:
#         st.write('Error: Could not retrieve data from Udemy.')
        
# if __name__ == '__main__':
#     app()
