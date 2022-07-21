from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas

career_salary_web_endpoint = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'

data_list = []
counter = 1

def page_scraping(row):
    table_row = row
    for tag in table_row:
        table_data_tags = tag.find_all('span', class_='data-table__value')
        row_container = [tag_data.getText() for tag_data in table_data_tags]
        data_list.append(row_container)
    print(data_list)
    time.sleep(1)


while counter != 35:

    time.sleep(3)
    print(counter)
    page_endpoint = f'/page/{counter}'
    print(page_endpoint)
    response = requests.get(url=career_salary_web_endpoint + page_endpoint)
    print(response.raise_for_status)

    salary_data_page = response.text

    # Soup obj to go through the data:
    soup = BeautifulSoup(salary_data_page, 'html.parser') 

    table_row = soup.find_all('tr',class_='data-table__row')
    print('\n')

    page_scraping(table_row)
    counter += 1
    
    #Pandas Method to save data as a DataFrame:
    data_df = pandas.DataFrame(data_list, columns=['Rank', 'Major', 'Degree Type', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning'])
    data_df.to_csv('./data/college_data.csv', index=False)

  

    

