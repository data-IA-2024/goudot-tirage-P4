

def teamatize(liste_base, taille_equipe):
    result = [liste_base[i:i + taille_equipe] for i in range(0, len(liste_base), taille_equipe)]
    return result

tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

print(teamatize(tableau, n))