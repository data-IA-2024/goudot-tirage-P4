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
 pip install -r requirements.txt
```

# Execution du programme
```bash
 source myvenv/bin/activate # linux
 python3 prog.py 3
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
