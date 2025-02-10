# goudot-tirage-P4

tirage au sort des P4
Utilisation du CSV crée sur le drive

# Installation
Environnement virtuel
```bash
 python3 -m venv myvenv
```
Activation Env virtuel (linux)
```bash
 source myvenv/bin/activate
```
Installation des librairies dans requirements:
```bash
 pip install pip-tools
 pip-compile requirements.in
 pip install -r requirements.txt
```

# Execution du programme
```bash
 source myvenv/bin/activate # linux
 python3 prog.py 3
```

Version Streamlit : 
```bash
 streamlit run appStreamlit.py
```

# Utilisation de dotenv

1) créer un fichier `.env` qui contiens
```text
DATAFILE=chemin d'accès vers le CSV
```
2) Installer [python-dotenv](https://pypi.org/project/python-dotenv/)
   inclure "python-dotenv" dans requirements.txt
3) installer (pip install...)
4) Utiliser load_dotenv() et os.getenv()


```bash
 git checkout -b B2 # création & checkout branche B2
 git status
 
 nano newfile.py
 git add newfile.py
 git commit -m "ajout fichier" # création de commit
 git push --set-upstream origin B2 # push local -> remote

 # sur B2
 git checkout -b B1 # création & checkout branche V1
 git status

 git fetch # récupère les modif remote de github
 git merge origin/B2 # merge les modif de B2 -> local

```

## Docker

Lister les images sur ma machine
```bash
 docker images
```
Créer l'image
```bash
 docker build -t tirage .
```
