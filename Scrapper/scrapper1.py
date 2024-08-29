import requests
from bs4 import BeautifulSoup as bs

url = "https://chartable.com/charts/spotify/us"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

if response.status_code == 200:
    print("Success")
else:
    print(f"Failed: {response.status_code}")
    print(response)
    exit()  

soup = bs(response.content, 'html.parser')


category_links = []
categories = soup.find_all('a', class_='link blue')
for category in categories:
    category_links.append(category['href'])


category_links = category_links[:-6]

def scrap_each_link(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs(response.content, 'html.parser')
    
    try:
        category_name = soup.find_all('div', class_='f2')
        if category_name:
            category_title = category_name[0].text
            print(category_title)
        else:
            print("No podcast name found")
    except Exception as e:
        print(f"Error while extracting podcast name: {e}")

    try:
        rows = soup.find_all('tr', class_='striped--near-white')
        if not rows:
            print("No rows found")
        
        for row in rows:
            link_tag = row.find('a', class_='link blue')

            if link_tag:
                # print(link_tag['href'])
                print(link_tag.text)
            else:
                print("No link tag found in row")
            link_elements=row.find_all('a', class_='link')
            for element in link_elements:
                img_tags=element.find_all('img')
                for img_tag in img_tags:
                    img_src=img_tag.get('src')
            podcast_name=link_tag.text
            podcast_link=link_tag['href']
            podcast_img=img_src

            print(f"Podcast Name: {podcast_name} \nPodcast Link: {podcast_link} \nPodcast Image: {podcast_img}")

        


      
    except Exception as e:
        print(f"Error while extracting links: {e}")

scrap_each_link("https://chartable.com/charts/spotify/united-states-of-america-arts-entertainment")
