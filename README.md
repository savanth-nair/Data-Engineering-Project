# End-to-End Pipeline with Web Scraping, MySQL, and Power BI  

📌 **Introduction**  
This project demonstrates a complete data engineering pipeline scraping book data from a public website, storing it in a MySQL database, executing SQL queries for insights, and visualizing results in Power BI.  
It showcases hands-on skills in **web scraping (Python)**, **database design and SQL querying (MySQL)**, and **business intelligence reporting (Power BI)**.

---

📖 **Problem Statement**  
The objective of this project was to simulate a real-world data engineering task by extracting structured data from the website **books.toscrape.com**.  
The goal was to scrape book and category information, store it in a relational database, perform analytical SQL queries, and visualize insights through dashboards — demonstrating a complete data pipeline from extraction to reporting.

---

🏗️ **Data Architecture Overview**

| Step | Description |
|:-----|:------------|
| 1 | Web Scraping with Python (Requests, BeautifulSoup, pandas) |
| 2 | Storing extracted data in MySQL (normalized relational schema) |
| 3 | Analytical SQL queries |
| 4 | Visualization in Power BI |

---

🛠️ **Tools and Technologies**
- **Python** (Requests, BeautifulSoup, pandas, PyMySQL)
- **MySQL Community Server** (with MySQL Workbench)
- **Power BI Desktop**
- **MySQL ODBC 8.0 Driver**

---

📂 **Project Components**

| Component | Output |
|:----------|:-------|
| Web Scraping | `categories.csv`, `books_data.csv`, `Books_WebScraping_Notebook.py` |
| Database Setup | `Database_and_Table_Creation.sql` |
| Data Loading | `DataLoadingScript_Notebook.py` |
| SQL Queries | `QueriesScript.sql` |
| Power BI Dashboard | `PowerBIReport.pbix` |

---

🧹 **Data Preparation and Cleaning**
- Extracted **50 categories** and **20 books** from homepage.
- Cleaned category and book names.
- Converted price and stock fields to numeric formats.
- Ratings mapped from text (e.g., "Three") to integers (3).
- Duplicates handled during database insertion using `INSERT IGNORE`.

---

🗄️ **Database Design (MySQL)**

**Database:** `bookstoscrape`

| Table | Columns |
|:------|:--------|
| `categories` | `category_id` (PK), `category_name` |
| `books` | `book_id` (PK), `book_name`, `category_id` (FK), `price`, `stock`, `rating` |

- **Normalization Level:** 3NF (Third Normal Form)
- **Relationship:** `category_id` is a foreign key in `books` table.

---

🗃️ **Data Loading Approach**
- Loaded CSV data using Python (`pandas`, `PyMySQL`).
- Dynamic foreign key mapping using a Python dictionary.
- Fallback to "Default" category if mapping not found.
- Efficient inserts and referential integrity maintained.

---

📊 **SQL Business Insights**

| Query | Purpose |
|:------|:--------|
| Top 3 Categories by Rating and Price | Identify best-performing, cost-effective categories |
| Top 5 Books by Rating | Find highest-rated individual books |

**Output:**
- `category`, `avg_rating`, `avg_lower_price`
- `book_name`, `rating`

---

📈 **Power BI Dashboard**

| Visual | Description |
|:-------|:------------|
| Matrix 1 | Category-wise book details (price, stock, rating) |
| Matrix 2 | Top 3 categories (by avg rating & lowest avg price) |
| Matrix 3 | Top 5 books by rating |
| Slicers | Category filter and Stock amount filter |

- **Color Theme:** Blue, White, and Grey (aligned with FMCG Analytics branding)
- **Interactive Filtering:** Via slicers
- **Icons:** FMCG logo, Book icon

---

⚡ **Challenges Faced**
- MySQL-Python integration setup and handling foreign keys dynamically.
- Setting up Power BI ODBC connectivity with MySQL.
- Maintaining data insertion efficiency and avoiding duplicates.

---

📖 **Conclusion**  
The project successfully integrated **web data extraction**, **relational storage**, **analytical querying**, and **interactive visualization**.  
It highlights the ability to build a **real-world scalable data pipeline**, transforming raw online data into actionable business insights — demonstrating critical skills in data engineering and reporting.

---

📜 **License**  
This project is part of an academic Data Engineering assessment and follows university guidelines.

---

🚀 **Happy Engineering!**
