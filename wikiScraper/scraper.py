
import requests
import random
from bs4 import BeautifulSoup
import webbrowser

def scrapeWiki(url):
     
     while True:
          response = requests.get(url=url)

          soup = BeautifulSoup(response.content, 'html.parser')

          title = soup.find(id='firstHeading').text

          all_links = soup.find(id='bodyContent').find_all('a')
          random.shuffle(all_links)

          link_to_scrape = 0

          for link in all_links:
               if link.find('/wiki/') == False:
                    continue

               link_to_scrape = link

          print(f'{title}: Do you want to view it? (Y/N)')
          ans = input().lower()

          if ans == 'y':
               link = f'https://en.wikipedia.org/wiki/{title}'
               webbrowser.open_new_tab(link)
          elif ans == 'n':
               scrapeWiki('https://en.wikipedia.org' + link_to_scrape['href'])
          else:
               break

          

scrapeWiki('https://en.wikipedia.org/wiki/Methamphetamine')