import requests, math
from bs4 import BeautifulSoup
import utils


algorithm = lambda x : (math.exp(-x/7)-1)*3.5

def get_results(id_manifestazione: str, clubs: dict) -> str:
    req_manifestazione = requests.get(f"http://finveneto.org/nuoto_migliori_prestazioni.php?id_manifestazione={id_manifestazione}")
    soup = BeautifulSoup(req_manifestazione.content, features="html.parser")
    best_performances = soup.find_all('div', {'class': 'col-centro'})
    
    for index, category_code in enumerate(utils.CATEGORY_CODES_FOR_HTML):
        data = best_performances[index].find_all('tr')[1:] + soup.find('tbody', {'id': category_code}).find_all('tr')
        for tr in data:
            if len(data) > 1:
                td = tr.find_all('td')
                name = tr.find('a').find('b').text
                race = td[2].find('b').text
                team = td[1].find_all('a')[1].text
                final_time = td[2].text.split('  ')[-1].replace('\t', '')
                fina_points = td[3].find('b').text

                clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['final_time'] = final_time
                entry_time = clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['entry_time']
                clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['fina_points'] = fina_points
                delta_percentage = -1 * (1 - (utils.time_to_timedelta(utils.format_time(final_time)) / utils.time_to_timedelta(utils.format_time(entry_time))))*100
                clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['delta%'] = f'{round(delta_percentage, 2)}%'
                estimated_points = algorithm(delta_percentage)
                if estimated_points < 1.00 and estimated_points > -1.00:
                    clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['estimated_points'] = str(0.00)
                else:
                    clubs[team][name]['events'][utils.RACE_FROM_RESULT_TO_STARTLIST_DICT[race]]['estimated_points'] = str(round(algorithm(delta_percentage), 0))


    return clubs