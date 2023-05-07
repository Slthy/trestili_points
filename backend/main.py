import results, startlists, json



def main():
    #test_url: http://finveneto.org/nuoto_schedamanifestazione.php?id_manifestazione=6810
    id_manifestazione = input("Inserisci link alla manifestazione: ").split('e=')[1]
    competition_startlists = startlists.get_startlists(id_manifestazione)

    with open('./new_startlists.json', 'w') as f:
        f.write(json.dumps(competition_startlists))
    
    with open('./results.json', 'w') as f:
        f.write(json.dumps(results.get_results(id_manifestazione, competition_startlists)))
    

    
if __name__ == "__main__":
    main()
    