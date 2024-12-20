# goudot-tirage-P4

tirage au sort des P4
Utilisation du CSV crée sur le drive

#Installation
##Creation d'un environnement virtuel
'''bash
 python3 -m venv myvenv
'''

##Activation de l'environnement
'''bash
 source myvenv/bin/activate
'''

##Installation des librairies requises (definies dans requirements.txt) 
'''bash
 pip3 install -r requirements.txt 
'''

#Utilisation de dotenv
1. Creer un fichier '.env' dans le repertoire d'execution qui contient
'''text
 FILEDATA=/chemin/file
2. Installer la lib [python-dotenv] en l'incluant dans requirements.txt
3. Utiliser load_dotenv() et os.getenv()

