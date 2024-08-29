def apple_podcasts_scrapper(link):
        try:        
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
                        podcast_artwork TEXT,
                        podcast_creator TEXT
                        )''')
                        conn.commit()

                def insert_data(category_title,podcast_name,podcast_link,podcast_artwork,podcast_creator):
                        table_name=category_title.replace(" ", "_").replace("-", "_").lower()
                        cursor.execute(f'''
                                INSERT INTO {table_name} (podcast_name,podcast_link,podcast_artwork,podcast_creator)
                                VALUES (?,?,?,?)
                        ''',(podcast_name,podcast_link,podcast_artwork,podcast_creator))
                        conn.commit()

                url=link

                try:
                        response=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
                        response.raise_for_status()
                        soup=bs(response.content, 'html.parser')
                except requests.RequestException as e:
                                print(f"Failed to retrieve page: {e}")


                soup=bs(response.content, 'html.parser')
                categories_links=[]
                try:
                        categories = soup.find_all('a', class_='link blue pl3')
                        for category in categories:
                                categories_links.append(category['href'])
                        categories_links = categories_links[:-2]
                except Exception as e:
                        print(f"Error while extracting category links: {e}")


                def scrap_each_link(link):
                        try:
                                response=requests.get(link,headers={'User-Agent': 'Mozilla/5.0'})
                                response.raise_for_status()
                                soup=bs(response.content, 'html.parser')
                        except requests.RequestException as e:
                                print(f"Failed to retrieve page: {e}")
                                return
                
                        try:
                                category_name = soup.find_all('div', class_='f2')
                                if category_name:
                                        category_title = category_name[0].text.strip()
                                        create_table_if_not_exists(category_title)
                                        print("Category Title:", category_title)
                                else:
                                        print("No category name found")
                                        return
                        except Exception as e:
                                print(f"Error while extracting category name: {e}")
                        

                        try:
                                rows=soup.find_all('tr',class_='striped--near-white')
                                if not rows:
                                        print("No rows found")
                                for row in rows:
                                        try:
                                                link_tag = row.find('a', class_='link blue')
                                                img_src=None
                                                if link_tag:
                                                        podcast_name = link_tag.text.strip()
                                                        podcast_link=link_tag['href']
                                                        link_with_creator_tag=row.find('a', class_='link no-underline silver mb1 db')
                                                        if link_with_creator_tag:
                                                                creator_name=link_with_creator_tag.text.strip()
                                                                link_elements=row.find_all('a', class_='link')
                                                        for element in link_elements:
                                                                img_tags=element.find_all('img')
                                                                for img_tag in img_tags:
                                                                        img_src=img_tag.get('src')
                                                podcast_creator=creator_name
                                                insert_data(category_title,podcast_name,podcast_link,img_src,creator_name)
                                                print(f"Inserted: {podcast_name} \n Creator:  {podcast_creator}Link: {podcast_link} \nImage: {img_src}")

                                        except Exception as e:
                                                print(f"Error While Processing Row: {e}")
                        except Exception as e:
                                print(f"Error while processing Rows: {e}")

                                        


                for link in categories_links:
                        scrap_each_link(link)
        except Exception as e:
                print(f"Error while extracting category links: {e}")                

links=['https://chartable.com/charts/itunes/us','https://chartable.com/charts/itunes/gb','https://chartable.com/charts/itunes/ca','https://chartable.com/charts/itunes/au','https://chartable.com/charts/itunes/fr','https://chartable.com/charts/itunes/de','https://chartable.com/charts/itunes/it']
for link in links:
        apple_podcasts_scrapper(link)




        # url = "https://chartable.com/charts/itunes/us"
        # try:
        #         response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        #         response.raise_for_status()
        # except requests.RequestException as e:
        #         print(f"Failed to retrieve page: {e}")
        #         exit()

        # soup = bs(response.content, 'html.parser')

        # categories_links=[]
        # try:
        #     categories = soup.find_all('a', class_='link blue')
        #     for category in categories:
        #         categories_links.append(category['href'])
        #     categories_links = categories_links[:-2]
        # except Exception as e:
        #       print(f"Error while extracting category links: {e}")

        # def scraap_each_link(url):
        #       try:
        #           response=requests.get(url)
        #           response.raise_for_status()
        #           soup=bs(response.content, 'html.parser')
        #       except requests.RequestException as e:
        #                 print(f"Failed to retrieve page: {e}")
        #                 return
        # response=requests.get("https://chartable.com/charts/itunes/us-arts-podcasts",headers={'User-Agent': 'Mozilla/5.0'})
        # print(response.status_code)
        # soup=bs(response.content, 'html.parser')

        # try:
                
        #         category_name = soup.find_all('div', class_='f2')
        #         if category_name:
        #                 category_title = category_name[0].text.strip()
        #                 print("Category Title:", category_title)
        #         else:
        #           print("No category name found")
        # except Exception as e:
        #         print(f"Error while extracting category name: {e}")

        # rows = soup.find_all('tr', class_='striped--near-white')
        # if not rows:
        #         print("No rows found")
        # for row in rows:
        #         try:
        #                 link_tag = row.find('a', class_='link blue')
        #                 if link_tag:
        #                         podcast_name = link_tag.text.strip()
        #                         podcast_link=link_tag['href']
        #                 link_with_creator_tag=row.find('a', class_='link no-underline silver mb1 db')
        #                 if link_with_creator_tag:
        #                        creator_name=link_with_creator_tag.text.strip()
        #                 link_elements=row.find_all('a', class_='link')
        #                 for element in link_elements:
        #                         img_tags=element.find_all('img')
        #                         for img_tag in img_tags:
        #                                 img_src=img_tag.get('src')
        #                 print(podcast_name)
        #                 print(podcast_link)
        #                 print(creator_name)
        #                 print(img_src)
        #         except Exception as e:
        #                 print(f"Error while extracting podcast name: {e}")
