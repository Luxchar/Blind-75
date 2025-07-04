"""
Problème : Trouver la longueur minimale d'un sous-tableau CONTIGU
dont la somme >= target

Technique : Fenêtre glissante (sliding window)
- Deux pointeurs : left et right
- Étendre la fenêtre avec right
- Rétrécir la fenêtre avec left quand somme >= target
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0                    # Pointeur gauche de la fenêtre
        min_length = float('inf')   # Longueur minimale trouvée
        current_sum = 0             # Somme de la fenêtre courante
        
        for right in range(len(nums)):  # Pointeur droit parcourt le tableau
            current_sum += nums[right]   # Étend la fenêtre vers la droite
            
            # Tant que la somme est suffisante, rétrécit la fenêtre
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]  # Rétrécit depuis la gauche
                left += 1
        
        return min_length if min_length != float('inf') else 0