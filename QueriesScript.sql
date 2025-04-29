USE bookstoscrape;     -- Setting the active database context to 'bookstoscrape'

-- After the data is inserted into the tables its evident that the database design follows normalization up to Third Normal Form 3NF (detailed explanation given in the documentation)

-- Top 3 categories with highest average rating and lowest price
SELECT c.category_name AS category,        
       AVG(b.rating) AS avg_rating,                -- using average funtion and alias
       AVG(b.price) AS avg_lower_price              
FROM books b
JOIN categories c ON b.category_id = c.category_id  -- using inner join to fetch the data from both table with category_id as the key
GROUP BY c.category_name                           -- group data by category
ORDER BY avg_rating DESC, avg_lower_price ASC    -- Sort by highest average rating first and average lowest price
LIMIT 3;                                         -- Returns only the top 3 categories

-- Top 5 books by rating
SELECT book_name, rating
FROM books
ORDER BY rating DESC            -- sort by highest rating
LIMIT 5;                        -- return top 5 books