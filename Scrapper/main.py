def scrapper(link):
    import requests
    from bs4 import BeautifulSoup as bs
    import sqlite3

    conn=sqlite3.connect('podcasts.db')
    cursor=conn.cursor()

    def create_table_if_not_exists(category_title):
        table_name=category_title.replace(" ", "_").replace("-", "_").lower()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                podcast_name TEXT NOT NULL,
                podcast_link TEXT NOT NULL,
                podcast_artwork TEXT
        )''')
        conn.commit()

    def insert_data(category_title,podcast_name,podcast_link,podcast_artwork,podcast_creator):
        table_name=category_title.replace(" ", "_").replace("-", "_").lower()
        cursor.execute(f'''
            INSERT INTO {table_name} (podcast_name,podcast_link,podcast_artwork,podcast_creator)
            VALUES (?,?,?,?)
        ''',(podcast_name,podcast_link,podcast_artwork,podcast_creator))
        conn.commit()









    url = link
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve page: {e}")
        exit()

    soup = bs(response.content, 'html.parser')

    category_links = []
    try:
        categories = soup.find_all('a', class_='link blue')
        for category in categories:
            category_links.append(category['href'])
        category_links = category_links[:-6]
    except Exception as e:
        print(f"Error while extracting category links: {e}")

    def scrap_each_link(url):
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            soup = bs(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Failed to retrieve page: {e}")
            return
        
        try:
            # Extract category title
            category_name = soup.find_all('div', class_='f2')
            if category_name:
                category_title = category_name[0].text.strip()
                print("Category Title:", category_title)
                create_table_if_not_exists(category_title)
            else:
                print("No category name found")
                return
        except Exception as e:
            print(f"Error while extracting category name: {e}")

        try:
            rows = soup.find_all('tr', class_='striped--near-white')
            if not rows:
                print("No rows found")
            
            for row in rows:
                try:
                    link_tag = row.find('a', class_='link blue')
                    if link_tag:
                        podcast_name = link_tag.text.strip()
                        podcast_link = link_tag['href']
                        img_src = None  # Default value if no image src is found

                        # Extract image sources
                        link_elements=row.find_all('a', class_='link')
                        for element in link_elements:
                            img_tags=element.find_all('img')
                            for img_tag in img_tags:
                                img_src=img_tag.get('src')
                                if img_src:
                                    break  # Stop after finding the first src
                        podcast_name=link_tag.text
                        podcast_link=link_tag['href']
                        podcast_img=img_src

                        insert_data(category_title, podcast_name, podcast_link, img_src)
                        print(f"Inserted: {podcast_name} \nLink: {podcast_link} \nImage: {img_src}")
                    else:
                        print("No link tag found in row")
                except Exception as e:
                    print(f"Error while processing row: {e}")
        except Exception as e:
            print(f"Error while extracting rows: {e}")

    for link in category_links:
        scrap_each_link(link)
        



    conn.close()
links=['https://chartable.com/charts/spotify/it','https://chartable.com/charts/spotify/pl','https://chartable.com/charts/spotify/se',]
for link in links:
    scrapper(link)