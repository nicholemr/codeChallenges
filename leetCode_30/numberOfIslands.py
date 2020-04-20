from pprint import pprint


class Solution:
    def numIslands(self, grid):
        islands = 0
        while self.checkIslands(grid):
            islands += 1

        return islands

    def checkIslands(self, grid):
        is_island = False
        # loop through grid items
        # find first item that == '1'
        current_row, current_col = self.find_one(grid)
        if current_col == None:
            return is_island
        # set is_island to True
        is_island = True
        queue = [(current_row, current_col)]
        while queue:
            # check top,bottom,left,right indeces:
            top = bottom = left = right = None
            if current_row > 0:
                top = (current_row-1, current_col)
            if current_row < len(grid)-1:
                bottom = (current_row+1, current_col)
            if current_col > 0:
                left = (current_row, current_col-1)
            if current_col < len(grid[0])-1:
                right = (current_row, current_col+1)

            to_check = [top, right, bottom, left]

            # add indeces to the queue
            for r_c in to_check:
                if r_c:
                    r, c = r_c
                    if grid[r][c] == '1':
                        queue.append(r_c)

            # set current item to '0'
            grid[current_row][current_col] = '0'
            # go to the next item listed in the queue
            current_row, current_col = queue.pop()

        return is_island

    def find_one(self, grid):
        current_row_col = [None, None]
        for current_row, current_row_arr in enumerate(grid):
            for col, element in enumerate(current_row_arr):
                if element == '1':
                    current_row_col = [current_row, col]
                    break
        return current_row_col


sol = Solution()
g = [[1, 1, 1, 1, 0],
     [1, 1, 0, 1, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]]
# g = [[1, 1, 0, 0, 0],
#      [1, 1, 0, 0, 0],
#      [0, 0, 1, 0, 0],
#      [0, 0, 0, 1, 1]]
g = [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]

g = [["0", "1", "0"],
     ["1", "0", "1"],
     ["0", "1", "0"]]

# g = [["1", "1", "1"],
#      ["1", "0", "1"],
#      ["1", "1", "1"]]

# g = [["1", "0", "1", "1", "1"],
#      ["1", "0", "1", "0", "1"],
#      ["1", "1", "1", "0", "1"]]
print('# of islands: ', sol.numIslands(g))
