#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0: number *= -1
    return number


def use_prefixes() -> List[str]:
    cannetons = []
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    for c in prefixes:
        cannetons.append(c + suffixe)
    return cannetons


def prime_integer_summation() -> int:
    primes = []
    n = 2
    while len(primes) < 100: 
        is_prime = True
        for i in range(2,n):
            if n % i == 0 : 
                is_prime = False
                break
        if is_prime == True: primes.append(n)
        n += 1
    return sum(primes)


def factorial(number: int) -> int:
    produit = 1
    for n in range(1,number+1,1):
        produit *= n
    return produit


def use_continue() -> None:
    for n in range(1,11):
        if n == 5: continue
        print (n)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    groupes_acceptes = []
    for groupe in groups:
        groupes_acceptes.append(True)
        
        if 10 < len(groupe) or len(groupe) < 3: groupes_acceptes[groups.index(groupe)]= False

        for a in groupe:
            if a == 25: continue
            if a < 18: groupes_acceptes[groups.index(groupe)]= False
            if a > 70:
                for b in groupe:
                    if b == 50: groupes_acceptes[groups.index(groupe)]= False
        
    return groupes_acceptes
#pourquoi les groupes 6 et 7 retournent faux dans la version prof 
# meme si ils correspondent au critere de taille et contiennent un membre de 25 ans??

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)} \nEt donc:")
    group_num = 1
    for g in (verify_ages(groups)):
        if g:
            acceptance = "Accepté"
        else: acceptance = "Refusé"
        print (f"    {group_num}. {acceptance}")
        group_num += 1

if __name__ == '__main__':
    main()
