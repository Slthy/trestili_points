import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

def format_time(time: str) -> str:
    # Time too short, invalid (e.g. "dnf")
    if '*' in time: # remove '*' from entrytimes
        time = time.replace('*', '')
        
    if len(time) < 4:
        return "NT"
    
    if len(time) > 5:  # time with minutes, seconds, decimals
        return datetime.strptime(time, "%M:%S.%f").strftime("%H:%M:%S.%f")[:-4]

url_club = "https://www.finveneto.org/schedasocieta.php?id_societa=2321"

req_club_page = requests.get(url_club)
soup = BeautifulSoup(req_club_page.content, features="html.parser")
club_swimming_athletes_pages: list = soup.find_all('div', {'class': 'col-centro'})[2].find_all('a')

'''club = {
    'W': {
        'Esordienti (P)': [],
        'Giovanissimi': [],
        'Esordienti A': [],
        'Ragazzi': [],
        'Juniores': [],
        'Cadetti': [],
        'Senior': []
    },
    'M': {
        'Esordienti (P)': [],
        'Giovanissimi': [],
        'Esordienti A': [],
        'Ragazzi': [],
        'Juniores': [],
        'Cadetti': [],
        'Senior': []
    }
}'''

CATEGORIES_DICT: dict[str, str] = {
    ' Esordienti (P):': 'Esordienti (P)',
    ' Giovanissimi:': 'Giovanissimi',
    ' Esordienti B:': 'Esordienti B',
    ' Esordienti A:': 'Esordienti A',
    ' Ragazzi:': 'Ragazzi',
    ' Juniores:': 'Juniores',
    ' Cadetti:': 'Cadetti',
    ' Senior:': 'Senior'
    
}

GENDER_INDEX_DICT = {
    0: 'W',
    1: 'M'
}

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
        '50': [],
        '25': []
    },
    '50 DO': {
        '50': [],
        '25': []
    },
    '50 RA': {
        '50': [],
        '25': []
    },
    '50 FA': {
        '50': [],
        '25': []
    },
    '100 SL': {
        '50': [],
        '25': []
    },
    '100 DO': {
        '50': [],
        '25': []
    },
    '100 RA': {
        '50': [],
        '25': []
    },
    '100 FA': {
        '50': [],
        '25': []
    },
    '100 MI': {
        '50': [],
        '25': []
    },
    '200 SL': {
        '50': [],
        '25': []
    },
    '200 DO': {
        '50': [],
        '25': []
    },
    '200 RA': {
        '50': [],
        '25': []
    },
    '200 FA': {
        '50': [],
        '25': []
    },
    '200 MI': {
        '50': [],
        '25': []
    },
    '400 SL': {
        '50': [],
        '25': []
    },
    '400 MI': {
        '50': [],
        '25': []
    },
    '800 SL': {
        '50': [],
        '25': []
    },
    '1500 SL': {
        '50': [],
        '25': []
    }
}
    for t in tempi_migliori:
        try:
            data: list = t.find_all('td')
            if len(data) > 1:
                race = data[0].find('b').text
                course = data[1].text

                if race in athlete_document.keys() and course in ['25', '50']:
                    time = format_time(data[5].find('b').text)
                    athlete_document[race][course].append(time)
        except: #athlete has no records
            continue
            
    club[name] = athlete_document
    club_names.append(name)

with open('./club.json', 'w') as f:
    f.write(json.dumps(club))
    
with open('./club_names.json', 'w') as f:
    f.write(json.dumps(club_names))

