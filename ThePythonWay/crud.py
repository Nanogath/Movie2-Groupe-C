import utils
import csv
import psycopg2


def ouvrir_connection(bdd, user, psw):
    try:
        conn = psycopg2.connect(database=bdd,
                                user=user,
                                host="localhost",
                                password=psw,
                                port="5432")
    except psycopg2.Error as e:
        print("Erreur lors de la connexion à la base de donnée")
        print(e)
        return None
    conn.set_session(autocommit=True)
    return conn


def create_and_insert(conn, table_query, insert_query, filename):
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        try:
            cur.execute(table_query)

            for row in reader:
                cur.execute(insert_query, row)
            conn.commit()
        
        except psycopg2.Error as e:
            print(e)
            
def lire_donnees(conn, sql_requete):
    try:
        cursor = conn.cursor()
        cursor.execute(sql_requete)
        #conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la lecture des données")
        print(e)
        return None
    
    print("Les données ont été lues avec succès")
    data = []
    for row in cursor:
        data.append(row)

    cursor.close()
    
    return data


def update_database(conn, var, column_name, column_type):
    try:
        cursor = conn.cursor()

        # Requête qui permet d'ajouter une colonne en fontion des paramètres column_name & column-type
        cursor.execute(f"ALTER TABLE movies ADD COLUMN IF NOT EXISTS {column_name} {column_type}")

        # On sélectionne tous les movieId pour les intégrer dans une liste data
        cursor.execute('SELECT movieId FROM movies ORDER BY movieId ASC')
        data = cursor.fetchall()

        """La liste data reçois des tuples, ex pour movieId = 1 -> (1, )
        Il faut donc récupérer l'id uniquement pour l'étape suivante 
        -> On crée une nouvelle liste à laquelle on ajoute l'élément 0 de chaque tuple
        """
        data_clean = list()
        for i in data:
            data_clean.append(i[0])

        """On peux alors utiliser la méthode zip qui agrège nos deux liste data_clean & var,
        var étant un paramètre de la fonction qui contient les valeurs que l'on souhaite ajouté 
        dans la BDD
        On a une liste imbriquée -> results = [[1,'Toy Story],[2,'Jumanji],...]
        """
        results = zip(data_clean, var)

        # Pour chaque couple de valeur x,y [x =1, y='Toy Story'] on execute la requete suivante
        for x, y in results:
            #print(x,y)
            cursor.execute(f"UPDATE movies SET {column_name} = %s WHERE movieId = %s", (y, x))

    except psycopg2.Error as e:
        print("Erreur lors de la modification des données")
        print(e)
        return None

    print("Les données ont étés modifiées")

    cursor.close()