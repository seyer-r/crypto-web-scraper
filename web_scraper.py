# Import necessary libraries
from playwright.sync_api import sync_playwright
import mysql.connector

def main():
    with sync_playwright() as p:

    ### SCRAPE DATA
    
        # Launch the browser, headless means the browser will be visible
        browser = p.chromium.launch(headless = False)
        # Open a new page
        page = browser.new_page()
        # Navigate to a website
        page.goto('https://coinmarketcap.com/')

        # Scrolling down to load data
        for i in range(5):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(1000)

        trs_xpath = "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr"
        trs_list = page.query_selector_all(trs_xpath)

        master_list = []

        for tr in trs_list:

            coin_dict = {}

            tds = tr.query_selector_all('//td')
            
            coin_dict['id'] = tds[1].inner_text()
            coin_dict['Name'] = tds[2].query_selector("//p[contains(@class, 'coin-item-name')]").inner_text()
            coin_dict['Symbol'] = tds[2].query_selector("//p[contains(@class, 'coin-item-symbol')]").inner_text()
            # save in float for calculations later when passing it through database
            coin_dict['Price'] = float(tds[3].inner_text().replace('$', '').replace(',', ''))
            coin_dict['Market_cap_usd'] = int(tds[7].inner_text().replace('$', '').replace(',', ''))
            coin_dict['Volume_24h_usd'] = int(tds[8].query_selector("//p[@color='text']").inner_text().replace('$', '').replace(',', ''))

            master_list.append(coin_dict)

        # convert to tuples to bulk insert into database
        list_of_tuples = [tuple(dic.values()) for dic in master_list]


    ### SAVE DATA

        # connect to database
        connection = mysql.connector.connect(
            host="localhost",
            database = 'crypto',
            user = 'root',
            password = 'password'
        )

        # create a cursor - channel that runs code for queries

        cursor = connection.cursor()
        sql = "INSERT INTO crypto (ID, NAME, SYMBOL, PRICE_USD, MARKET_CAP_USD, VOLUME_24H_USD) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql, list_of_tuples)

        # commit changes to database
        connection.commit()

        # close the cursor and connection
        cursor.close()
        connection.close()

        # Close the browser
        browser.close()






if __name__ == '__main__':
    main()