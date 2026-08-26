class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        moveCount = 0
        for i in range(len(students)):
            moveCount += abs(seats[i] - students[i])
        
        return moveCount


