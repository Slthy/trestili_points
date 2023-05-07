import requests, json
from bs4 import BeautifulSoup

import utils

url_club = "https://www.finveneto.org/schedasocieta.php?id_societa=2321"

req_club_page = requests.get(url_club)
soup = BeautifulSoup(req_club_page.content, features="html.parser")
club_swimming_athletes_pages: list = soup.find_all('div', {'class': 'col-centro'})[2].find_all('a')

club = {}
club_names = []
for athlete in club_swimming_athletes_pages:
    athlete_page = requests.get(f"https://www.finveneto.org/{athlete['href'][2:]}")
    soup = BeautifulSoup(athlete_page.content, features="html.parser")
    tempi_migliori = soup.find('table', {'summary': 'Tempi migliori'}).find('tbody').find_all('tr')
    
    name = soup.find('div', {'class': 'col-C'}).find('h1').text

    athlete_document = {
    'Name': name,
    '50 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '50 DO': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '50 RA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '50 FA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '100 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '100 DO': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '100 RA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '100 FA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '100 MI': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '200 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '200 DO': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '200 RA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '200 FA': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '200 MI': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '400 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '400 MI': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '800 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    },
    '1500 SL': {
        '50': "1:00:00.01",
        '25': "1:00:00.01"
    }
}
    for t in tempi_migliori:
        try:
            data: list = t.find_all('td')
            if len(data) > 1:
                
                race = data[0].find('b').text
                course = data[1].text
                gender = {'donna': 'F', 'uomo': 'M'}[soup.find('div', {'class': 'col-C'}).find('img')['src'][18:-4]]
                
                #'race_length', 'discipline', 'gender', and 'course'
                time = utils.format_time(data[5].find('b').text)
                

                if race in athlete_document.keys() and course in ['25', '50']:
                    fina_data = utils.FINVENETO_TO_FINA_DICT[race]
                    time = utils.format_time(data[5].find('b').text)
                    fina_points = utils.get_fina_points(time, fina_data[0], fina_data[1], gender, utils.FINVENETO_TO_FINA_COURSES_DICT[course])
                    old_fina_points = utils.get_fina_points(athlete_document[race][course], fina_data[0], fina_data[1], gender, utils.FINVENETO_TO_FINA_COURSES_DICT[course])
                    if fina_points > old_fina_points:
                        athlete_document[race][course] = time
        except: #athlete has no records
            continue
            
    club[name] = athlete_document
    club_names.append(name)

with open('./club.json', 'w') as f:
    f.write(json.dumps(club))
    
with open('./club_names.json', 'w') as f:
    f.write(json.dumps(club_names))

