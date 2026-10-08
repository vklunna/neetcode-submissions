class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            list1=[]
            for col in range(9):
                value = board[row][col]
                if value=='.':
                    continue
                if value in list1:
                    return False
                list1.append(value)

        for col in range(9):
            list2=[]
            for row in range(9):
                value2 = board[row][col]
                if value2=='.':
                    continue
                if value2 in list2:
                    return False
                list2.append(value2)

        for i in range(0,9,3):
            for j in range(0,9,3):
                list3=[]
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        value3=board[row][col]
                        if value3=='.':
                            continue
                        if value3 in list3:
                            return False
                        list3.append(value3)

        return True

                
