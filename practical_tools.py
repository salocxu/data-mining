from itertools import combinations

def generate_combinations(lst):
    result = []
    last_element =[]
    n = len(lst)
    length = range(n)
    # Générer toutes les combinaisons de taille n-1
    
    for combination in combinations(length, n-1):
        result.append([lst[i] for i in combination])
        last_element.append([lst[i] for i in range(n) if i not in combination][0])
    
    return result, last_element

# Exemple d'utilisation
