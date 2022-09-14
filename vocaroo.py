from requests import get
from sys import argv


url = argv[1]
url = url.split("/") #['https:', '', 'boards.4channel.org', 'g', 'thread', '111111']
board = url[3]
thread_id = url[-1]

random_with_links = []
links_new = []



def thread():
    url2 = 'https://voca.ro'
    r = get(f'https://a.4cdn.org/{board}/thread/{thread_id}.json')
    r = r.json()
    for x in r['posts']:
        if url2 in x['com']:
            random_with_links.append(x['com'])
    if len(random_with_links) == 0:
        print("No vocaroo links found.")
    else:
        for y in random_with_links:
            start = y.index(url2)
            end = start + len(url2) + 13
            links_new.append(y[start:end])


def vocaroo():
    length = len(links_new)
    counter = 0
    for link in links_new:
        counter+=1
        split = link.split('/')  # ['https:', '', 'voca.ro', '1203192398123']
        id = split[-1]
        name = f'{id}.mp3'
        url = f"https://media1.vocaroo.com/mp3/{id}"
        session = get(url, headers={'referer': f"https://vocaroo.com/{id}"})
        print(f'Downloading {counter}/{length}')
        with open(name, 'wb') as f:
            f.write(session.content)
thread()
vocaroo()
