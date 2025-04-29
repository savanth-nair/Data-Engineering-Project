#!/usr/bin/env python
# coding: utf-8

# # Web Scraping

# ### Installing the package

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install pandas')


# ### Importing the package

# In[53]:


from bs4 import BeautifulSoup # for parsing HTML content
import requests               # for sending HTTP requests to the website
import pandas as pd           # for tabular data management 
import csv                    # to convert and export as csv
import time                   # for measuring scraping performance.
import re                     # for extracting numerical values from text.


# ### Load the URL

# In[30]:


url = 'https://books.toscrape.com/'


# ### Sending Get Request

# In[31]:


response = requests.get(url)

if response.status_code == 200:
    print("Request Successfull!!")
else:
    print("Request Failed!!")


# ### Parse the HTML Content

# In[32]:


# Creating soup object which contains all data
soup = BeautifulSoup(response.content,"html.parser")


# In[33]:


print(soup)


# ### Extracting Categories From 1st page

# In[73]:


categories_data = []   # Initializing an empty list to store category variables
categories = soup.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')  # Locating all <li> elements under the 'nav nav-list' class which contains category links

categories_start_time = time.time()   # Start time while extracting categories
categories_extracted = 0    # initializing categories to 0 to find out total number of categories extracted
# Loop through categories
for category in categories: 
    category_name = category.find('a').text.strip() # finding the 'a' tag to extract category and using text.strip to extract only the category name
    categories_data.append(category_name) # appending each category to the empty list one after the other
    
    categories_extracted += 1  # incrementing categories after every loop
    
    categories_end_time = time.time()  # end time while extracting categories
    categories_total_time = (categories_end_time - categories_start_time)/60.0 #total time taken for extracting the categories

print(categories_data)


# In[74]:


print(f'Total Time taken for Extracting the Categories Data from 1st Page: {categories_total_time:.2f} minutes')
print(f'Total Number of Categories Extracted from 1st Page: {categories_extracted}')


# ### Creating Dataframe for Categories

# In[84]:


df_categories_scraped = pd.DataFrame(categories_data, columns = ['Categories'])
df_categories_scraped


# ### Extracting Book details From 1st page

# In[75]:


# Find all book titles and their links
books = soup.find_all('h3')   # Find all <h3> tags on the page, each containing a book title and link

books_start_time = time.time() # start time while extracting the categories
books_extracted = 0 # initializing the books to 0 to find out total books extracted

books_data = []  #creating an empty list to append the books data into this list

# Iterate through the books and get required information from page 1
for book in books:
    book_url = book.find('a')['href']   # Get the relative URL for the book details page
    book_response = requests.get(url + book_url)    # Send a GET request to fetch the book’s detail page
    book_soup = BeautifulSoup(book_response.content,"html.parser")    # Parse the HTML content of the book detail page
    
    Name = book_soup.find('h1').text  # finding 'h1' tag to extract name of the book
    Category = book_soup.find('ul', class_="breadcrumb").find_all('a')[2].text.strip()     # Extract the book's category from the breadcrumb class and 'a' tag
    Price = book_soup.find('p',class_='price_color').text.strip()     # finding 'p' tag to extract name of the book
    Stock_Amount = re.search(r'\((\d+)\s+available\)', book_soup.find('p', class_='availability').text.strip()).group(1)  # Use regular expression to extract the number of available stock from the text
    Rating = book_soup.find('p', class_='star-rating')['class'][1]   # Extract the book's rating from the class attribute under class and slicing 1
    
    books_extracted += 1 # incrementing books_extracted after every loop by 1
    
    books_end_time = time.time() #end time after all books extracted
    books_total_time = (books_end_time - books_start_time)/60.0 # total time taken for all books extracted
    
    books_data.append([Name, Category, Price, Stock_Amount, Rating]) # appending the columns one by one to the empty list
    
    
print(books_data)


# In[77]:


print(f'Total Time taken for Extracting the Books Data from 1st Page: {books_total_time:.2f} minutes')
print(f'Total Number of Books Extracted from 1st Page: {books_extracted}')


# ### Creating the dataframe for Book's Details

# In[78]:


df_books_scraped = pd.DataFrame(books_data, columns = ['Name','Category','Price','Stock Amount','Rating'])
df_books_scraped


# ### Simple Data Transformation

# In[81]:


df_books_scraped = pd.DataFrame(books_data, columns=['Name', 'Category', 'Price(£)', 'Stock Amount', 'Rating'])

# Remove the pound symbol from the 'Price' column and convert to float
df_books_scraped['Price(£)'] = df_books_scraped['Price(£)'].str.replace('£', '').astype(float)

# Convert 'Rating' column from words to numbers
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df_books_scraped['Rating'] = df_books_scraped['Rating'].map(rating_map)

# Convert 'Stock Amount' to int
df_books_scraped['Stock Amount'] = df_books_scraped['Stock Amount'].astype(int)


# In[82]:


df_books_scraped


# ### Converting both categories df and books df into CSV and saving it in local

# In[83]:


df_books_scraped.to_csv('books_data.csv', index=False)  # index=false so that no indexing is done


# In[85]:


df_categories_scraped.to_csv('categories.csv', index=False)

