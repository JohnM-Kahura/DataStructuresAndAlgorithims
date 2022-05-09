from typing import List


class Solution:
    def destCity(self,paths:List[List[str]])-> str:
        length=len(paths)
        destination=paths[length-1][1]
        
