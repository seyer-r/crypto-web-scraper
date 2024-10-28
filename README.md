What is a web scraper?
A web scraper is a program which automatically extracts/scrapes data from a website

What did I build?
I built a web scraper which would automatically scrape the data off of a website which stored information about cryptocurrencies e.g. their name, price, their market value, their volume over a 24hr period. I then transferred this data and put it into a database using MySQL as the database management system. 

Why did you build this?
I built this because I wanted to explore automation and how programs can interact with HTML websites and extract data from them. I was interested in that process. I also gained a lot of skills with this project, including how to how to parse through HTML and how to transfer data to a database using drivers. 

How did you build it?
Firstly I set up a Python environment and installed the necessary libraries. I used Playwright which is a good tool for automating interactions with dynamic websites which rely on JS to render content. Then, I created code to perform actions like automatically scrolling down to load the data. I then extracted the relevant data by using XPath expressions and I also formatted the data (changing them into floats or int) so they could be manipulated when I put them through the database. To store the data I used MySQL connector to connect to the database and insert the scraped data. 

XPath is a query language used to locate and extract data from a specific part of a web page's HTML structure, so like you can target elements based on their classes, attributes etc. you can filter elements. Provides advanced functionality, so it's used for more complex queries. 
