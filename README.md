# anavis
Projet d'analyse et visualisation de données
Veuillez décompresser le fichier clean.zip avant de lancer les scripts

## Cleaning
    
Fichier Cleaning.ipynb (le résultat de l'exécution de ce fichier est le répertoire clean, donc on n'a pas à ré-exécuter ce script)

## Connecting to ElasticSearch and Launching Kibana

https://www.elastic.co/fr/start?&ultron=[EL]-[B]-[EMEA]-FR-Exact&blade=adwords-s&Device=c&thor=elasticsearch&gclid=EAIaIQobChMIuM-64teh5wIVihnTCh2UHAllEAAYASAAEgLlF_D_BwE

    1.1 Télécharger le package Elasticsearch 
    1.2 Télécharger le package Kibana
    1.3 Lancer les éxecutables bin/elasticsearch et bin/kibana se trouvant dans les packages téléchargés.
    1.4 Exécuter le script Elasticsearch.ipynb (l'exécution de la fonction load_2016_data dure 25 minutes)
    1.5 Lancer Kibana (http://localhost:5601)
    1.6 Cliquer sur "Connect to your Elasticsearch index", 
        Step1: Tapez "velos" dans la barre de recherche,  
        Step2: Choisir "timestamp" comme index de nos données

P.S. : Nos données sont celles de l'année 2016. Chercher dans ce range pour voir apparaitre nos données. 

## Visualisations des données

(à faire)
