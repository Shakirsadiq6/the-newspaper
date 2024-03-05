import requests
from bs4 import BeautifulSoup

def get_main_news_title_image():
    url = 'https://www.trtworld.com/'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    main_news = soup.find('div', class_='Card Card-First-News layoutFourScope')
    main_news_link_tag = main_news.find_all('a', href=True)
    main_news_link = [link['href'] for link in main_news_link_tag][0]

    main_news_image_tag = main_news.find_all('img', src=True)
    main_news_image = [img['src'] for img in main_news_image_tag][0]

    main_news_title = main_news.find_all('div', class_='card-col card-end justify-top')
    for news_title in main_news_title:
        news_title = (news_title.text).strip()
    return news_title, main_news_link, main_news_image

def get_main_news_content():
    _, main_news_link, _ = get_main_news_title_image()

    response = requests.get('https://www.trtworld.com'+main_news_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_content = soup.find_all('div', class_='Article Article-Paragraph')
    total_paragraph = []
    for div in news_content:
        paragraphs = div.find_all('p')
        for paragraph in paragraphs:
            paragraph_text = (paragraph.text).split(' GMT — ')
            total_paragraph.append(paragraph_text[-1])
    return total_paragraph
