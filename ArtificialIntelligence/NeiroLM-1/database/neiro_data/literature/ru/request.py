import requests, bs4, time
import fake_useragent as fua

maxbooknum = 10000
maxparts = 50

a = input("Нажмите, чтобы начать скачивание библиотеки.")

for i in range(1, maxbooknum):
    text = ''
    for j in range(1, maxparts):
        # Значения
        url = f'https://ilibrary.ru/text/{i}/p.{j}/index.html'

        #
        r = requests.get(url, headers={'User-Agent': fua.UserAgent().firefox})

        soup = bs4.BeautifulSoup(r.text, "html.parser")

        t = soup.find('div', class_='title')
        b = t.findChildren("h1")
        t = b[0]
        print(t)
        title = t.get_text()
        text.join(f"Title: {title}\n")

        a = soup.find('div', class_='author')
        author = a.get_text()
        text.join(f"Author: {author}\n\n")

        for p in soup.find_all('span', class_='p'):
            for k in range(1, maxparts):
                p.get_text()
                text.join(f"{k}.\n{p}")

    print(text)
    break