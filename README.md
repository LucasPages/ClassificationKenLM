Le script train_model.sh permet d'entraîner des modèles n-grams avec KenLM.
Usage : ./train_model ordre corpus


Le script classify.py permet ensuite d'obtenir une classification du corpus fourni en paramètre.
Ouput : une liste python contenant les résultats de la classification, dumpé dans un fichier .out .
Usage : python3 classify.py --n ordre

Il faut avoir entraîné les trois modèles de l'odre utilisé pour que le script fonctionne.
Le script train_model.sh n'en entraîne qu'un seul à la fois.

