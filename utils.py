# utils.py
import csv
from datetime import datetime


def lire_csv_dict(nom_fichier):
    data = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def lire_csv_liste(nom_fichier):
    data = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        entete = next(reader)
        for row in reader:
            data.append(row)
    return data, entete


def renvoyer_annee_titre_film(title):
    """ 
    Fonction renvoyant l'année du film et son titre seul (sans année)
    
    Exemple: 
        utils.renvoyer_annee_titre_film('Toy Story (1995)')
    renvoie:
        (1995, 'Toy Story')
    """
    
    str_split = title.split("(")
    try:
        if len(str_split) > 2:
            title = f'{str_split[0]}({str_split[1]}'.strip()
        else:
            title = (str_split[0:-1])[0].strip()
        
        year = (str_split[-1]).replace(")", "").strip()
        return int(year), title
    except:
        return None, title

    
    
def renvoyer_datetime_iso(timestamp):
    """ 
    Fonction renvoyant la date & l'heure au format iso
    
    Exemple: 
        utils.renvoyer_datetime_iso(964982703)
    renvoie:
        '2000-07-30T20:45:03'
    """
    
    from datetime import datetime
    try:
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object.isoformat()
    except:
        return None