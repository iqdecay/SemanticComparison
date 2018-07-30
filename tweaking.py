from nltk.corpus import stopwords
# The useless words are based on the empirical analysis of the vocabulary built by word2Vec algorithm, and I chose
# the ones that seemed the less useful amongst the most currents
useless_words = ['pouvez', 'merci', 'retour', 'bonjour', 'bonsoir', 'cordialement', 'les', 'current', 'partition',
                 'referrer', 'please', 'si', 'may', '_blank', 'vous', 'bien', "car", "cela", "donc", 'janvier',
                 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'décembre',
                 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', 'mois', 'oui', "cette", "ce",
                 "cet", "ces", "ça", "https", 'url','class', 'contract','colibriwithus','aspx','peux','madame','monsieur',
                 "client", "href", "blank", "this", "voip", "ubfb", "target",'plus', 'to', 'm', 'fr', 're', 's',
                 "httpsopmanagerxelyaioapiclientemberindexjspinventorysnapshotmonitoringdevice",
                 "httpskbxelyaioinfratroubleshootingopmanagepertedestunnels",
                 "httpskbxelyaioinfratroubleshootingopmanagepertededevice",
                 "bs", "pec", ]


stop_words = useless_words + list(stopwords.words("french")) + list(stopwords.words("english"))

replacement = {
    "pb": "problème",
    "probleme": "problème",
    "problèmes": "problème",
    "probléme": "problème",
    "soucis": "souci",
    "intervenante": "intervenant",
    "intervenantes": "intervenant",
    "intervenants": "intervenant",
    "interventions": "intervention",
    "bugs": "bug",
    "plannings": 'planning',
    'pbl': "problème",
    "problemes": "problèmes",
    "salaires": "salaire",
    "disfonctionnement": "dysfonctionnement",
    'sallire': "salaire",
    "cp": 'copie',
    "planing": 'planning',
    "plannification": "planification",
    "evenement": "évènement",
    "mail": "email"
}


banned_ids = ['418778', '418782', '418780', '418777']
