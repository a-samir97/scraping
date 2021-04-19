from bs4 import BeautifulSoup
import requests

def scrape_info(url):
      
    # getting the request from url
    r = requests.get(url)
      
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
    vedio_url = original_image = s.select('link[itemprop="url"]')[0]['href']
    thumbnail_image = s.select_one('link[itemprop="thumbnailUrl"]')['href'] # get thumbnail url 
    original_image = s.select('link[itemprop="url"]')[2]['href'] # get original image 
    views = s.select_one('meta[itemprop="interactionCount"][content]')['content'] # to get views 
    title = s.select_one('meta[itemprop="name"][content]')['content'] # title
    duration = s.select_one('meta[itemprop="duration"][content]')['content'] # duration

    info_data = {
        'thumbnail_image': thumbnail_image,
        'original_image': original_image,
        'views': views,
        'title': title,
        'duration': duration,
        'vedio_url': vedio_url
    }
    return info_data