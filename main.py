from scrape import scrape_info
from database import connect_database, insert_data, create_table, get_all_data

# main function
if __name__ == "__main__":
    
    # URL of the video
    url ="https://www.youtube.com/watch?v=Yw4rkaTc0f8"

    # create table if not exists
    create_table()

    # calling the function to scrape data 
    data_info = scrape_info(url)

    # insert data into database 
    insert_data(data_info)

    # get all data (displaying data)
    get_all_data()

