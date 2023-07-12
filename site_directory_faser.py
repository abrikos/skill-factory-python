import requests


def main():
    url = 'https://ysn.ru'
    links = []
    with open('check.txt', 'rt') as f:
        links = f.readlines()
    if len(links) == 0:
        print('No links')
    for link in links:
        link.replace('\n', '')
        print(link)
        full_link = ''.join((url, link))
        response = requests.get(full_link)
        if response.status_code != 404:
            print(f'{full_link} exists')


main()
