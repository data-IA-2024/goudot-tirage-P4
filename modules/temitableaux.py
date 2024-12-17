
def teamatize(liste_base, taille_equipe):
    """
    Cette fonction prend une liste et la divise en sous-listes de taille égale.
    :param liste_base: liste à diviser
    :param taille_equipe: taille des sous-listes
    :return: liste de sous-listes
    """
    result = [liste_base[i:i + taille_equipe] for i in range(0, len(liste_base), taille_equipe)]
    return result
    

