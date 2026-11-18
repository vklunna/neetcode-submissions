class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        ahead_time = 0
        position_time = sorted(zip(position,speed),reverse=True)
        for pos,spe in position_time:
            time = (target-pos)/spe
            if time>ahead_time:
                fleet+=1
                ahead_time = time
            else:
                continue
        return fleet
            