import requests
from bs4 import BeautifulSoup

def get_startlists(id_manifestazione: str) -> dict:
    req_manifestazione = requests.get(f"http://finveneto.org/nuoto_schedamanifestazione.php?id_manifestazione={id_manifestazione}")
    soup = BeautifulSoup(req_manifestazione.content, features="html.parser")
    startlists_tags = soup.find('table', {'summary': "Programma manifestazione"}).find('tbody', {'class': 'tab'}).find_all('tr')

    events = []
    for tr in startlists_tags[1:]:
        data = tr.find_all('td')
        event = {
            'time': data[0].text,
            'race': data[2].find('a').text,
            'url': f"http://finveneto.org/{data[4].find('a')['href'][2:]}"
        }
        events.append(event)

    clubs: dict[str, list[dict[str, list]]] = {}
    
    for event in events:
        soup = BeautifulSoup(requests.get(event['url']).content, features="html.parser")
        event_tags = soup.find('table', {'summary': "Start List Definitiva"}).find('tbody', {'class': 'tab'}).find_all('tr')
        
        
        for tr in event_tags:
            data = tr.find_all('td')
            if len(data) > 1:
                name = data[1].find('b').text
                race = event['race']
                team = data[3].find('a').text
                entry_time = data[4].text.replace(u'\xa0', u'').replace(u'\t', u'')
                
                if data[3].find('a').text not in clubs.keys():
                    clubs[team] = {name: {'events': {race: {'entry_time': entry_time}}}}
                else:
                    if name in clubs[team].keys():
                        clubs[team][name]['events'][race] = {'entry_time': entry_time}
                    else:
                        clubs[team][name] = {'events': {race: {'entry_time': entry_time}}}


    return clubs
