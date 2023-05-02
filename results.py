import requests, datetime, math
from datetime import datetime
from bs4 import BeautifulSoup

time_to_timedelta = lambda t : datetime.strptime(t, "%H:%M:%S.%f") - datetime(1900,1,1)
algorithm = lambda x : (math.exp(-x/7)-1)*3.5

def format_time(time: str) -> str:
    # Time too short, invalid (e.g. "dnf")
    if '*' in time: # remove '*' from entrytimes
        time = time.replace('*', '')
        
    if len(time) < 4:
        return "NT"
    
    if len(time) > 5:  # time with minutes, seconds, decimals
        return datetime.strptime(time, "%M:%S.%f").strftime("%H:%M:%S.%f")[:-4]
    
    return datetime.strptime(time, "%S.%f").strftime("%H:%M:%S.%f")[:-4]

CATEGORY_CODES_FOR_HTML = [ "tbody_assoluta_f", "tbody_assoluta_m"]

GENDER_BY_INDEX_DICT: dict = {
    "tbody_assoluta_f" : "assoluti_f",
    "tbody_assoluta_m" : "assoluti_m",
    #"tbody_cat_1003_F" : "ragazzi_f",
    #"tbody_cat_1004_F" : "juniores_f",
    #"tbody_cat_1005_F" : "cadetti_f",
    #"tbody_cat_1006_F" : "senior_f",
    #"tbody_cat_3_M" : "ragazzi_m",
    #"tbody_cat_4_M" : "juniores_m",
    #"tbody_cat_5_M" : "cadetti_m",
    #"tbody_cat_6_M" : "senior_m",
}

CONVERT_RACE_FROM_RESULT_TO_STARTLIST: dict = {
    '50 SL': '50 Stile Libero',
    '50 DO': '50 Dorso',
    '50 RA': '50 Rana',
    '50 FA': '50 Farfalla',
    '100 SL': '100 Stile Libero',
    '100 DO': '100 Dorso',
    '100 RA': '100 Rana',
    '100 FA': '100 Farfalla',
    '100 MI': '100 Misti',
    '200 SL': '200 Stile Libero',
    '200 DO': '200 Dorso',
    '200 RA': '200 Rana',
    '200 FA': '200 Farfalla',
    '200 MI': '200 Misti',
    '400 SL': '400 Stile Libero',
    '400 MI': '400 Misti',
    '800 SL': '800 Stile Libero',
    '1500 SL': '1500 Stile Libero'
}

def get_results(id_manifestazione: str, clubs: dict) -> str:
    req_manifestazione = requests.get(f"http://finveneto.org/nuoto_migliori_prestazioni.php?id_manifestazione={id_manifestazione}")
    soup = BeautifulSoup(req_manifestazione.content, features="html.parser")
    best_performances = soup.find_all('div', {'class': 'col-centro'})
    
    for index, category_code in enumerate(CATEGORY_CODES_FOR_HTML):
        data = best_performances[index].find_all('tr')[1:] + soup.find('tbody', {'id': category_code}).find_all('tr')
        for tr in data:
            if len(data) > 1:
                td = tr.find_all('td')
                name = tr.find('a').find('b').text
                race = td[2].find('b').text
                team = td[1].find_all('a')[1].text
                final_time = td[2].text.split('  ')[-1].replace('\t', '')
                fina_points = td[3].find('b').text

                clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['final_time'] = final_time
                entry_time = clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['entry_time']
                clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['fina_points'] = fina_points
                delta_percentage = -1 * (1 - (time_to_timedelta(format_time(final_time)) / time_to_timedelta(format_time(entry_time))))*100
                clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['delta%'] = f'{round(delta_percentage, 2)}%'
                estimated_points = algorithm(delta_percentage)
                if estimated_points < 1.00 and estimated_points > -1.00:
                    clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['estimated_points'] = str(0.00)
                else:
                    clubs[team][name]['events'][CONVERT_RACE_FROM_RESULT_TO_STARTLIST[race]]['estimated_points'] = str(round(algorithm(delta_percentage), 0))


    return clubs