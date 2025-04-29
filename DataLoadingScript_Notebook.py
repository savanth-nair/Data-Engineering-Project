#!/usr/bin/env python
# coding: utf-8

# ## Data Loading into MYSQL 

# In[2]:


# importing the modules
get_ipython().system('pip install pymysql')
import pandas as pd
import pymysql     # used to connect with mysql


# ### Connecting to MySQL

# In[30]:


conn = pymysql.connect(host='localhost', user='root', password='0611', database='bookstoscrape') 
cursor = conn.cursor() # cursor is used to locate any data


# ### Load CSVs

# In[31]:


categories = pd.read_csv('categories.csv')
books = pd.read_csv('books_data.csv')


# In[6]:


categories


# In[10]:


books


# ### Checking the connection with mysql for category table

# In[26]:


# Query the table
cursor.execute("SELECT * FROM categories LIMIT 1")  

# Get column names
column_names = [desc[0] for desc in cursor.description]
print("Columns in 'categories' table:", column_names)


# ### Checking the connection with mysql for books table

# In[23]:


# Query the table
cursor.execute("SELECT * FROM books LIMIT 1")  # You can use any table name

# Get column names
column_names = [desc[0] for desc in cursor.description]
print("Columns in 'books' table:", column_names)


# ### Inserting the values into books and categories table

# In[32]:


# Inserting categories to category table
category_map = {}    # Dictionary to store category_name → category_id mapping

#looping through each category name
for name in categories['Categories']:
    name = name.strip() # Remove leading/trailing whitespace
    cursor.execute("INSERT IGNORE INTO categories (category_name) VALUES (%s)", (name,))  ## Insert the category into the table if it doesn't already exist
    conn.commit()      # commiting the insertion 
    cursor.execute("SELECT category_id FROM categories WHERE category_name=%s", (name,))  # Retrieving the corresponding category_id from the database
    category_map[name] = cursor.fetchone()[0]  # Storing in dictionary 

# Inserting books to books table

for _, row in books.iterrows():
    book_name = row['Name'].strip()   # Extracting and cleaning book details from the Df
    category = row['Category'].strip()
    price = float(row['Price(£)'])    # Extracting and converting to float
    stock = int(row['Stock Amount'])
    rating = int(row['Rating'])

    # Use category_map and fallback to 'Default' if category not found
    category_id = category_map.get(category, category_map.get("Default"))
    
    # book insertion
    cursor.execute("""
        INSERT INTO books (book_name, category_id, price, stock, rating)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        book_name,
        category_id,
        price,
        stock,
        rating
    ))
    conn.commit() # commiting the insertion


# In[ ]:


cursor.close() # closing the cursor
conn.close()  # closing the mysql connection

