import requests
from bs4 import BeautifulSoup

# Make a request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Albert_Einstein'
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the sections on the page
sections = soup.find_all('span', class_='mw-headline')

# Create a list to store the extracted data
wiki_data = []

# Iterate over the sections and extract the headings and content
for section in sections:
    heading = section.text

    # Find the next <p> tag following the section
    content = section.find_next_sibling('p')

    # Check if the <p> tag exists and extract its text
    if content:
        content_text = content.text
    else:
        content_text = ''

    # Create a dictionary for each section
    section_data = {'heading': heading, 'content': content_text}

    # Append the dictionary to the list
    wiki_data.append(section_data)

# Display the extracted data
for section in wiki_data:
    print('Heading:', section['heading'])
    print('Content:', section['content'])
    print('---')
