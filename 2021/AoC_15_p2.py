import collections
import math, heapq
from collections import deque
# dijkstra's algorithm
def dijkstra(grid):
    ROWS, COLS = len(grid), len(grid[0])
    dijkstra_dp = [ [ float("inf") ] * COLS for _ in range(ROWS) ]
    dijkstra_dp[0][0] = 0
    h = [(0, 0, 0)]
    while h:
        total_risk, r, c = heapq.heappop(h)
        if dijkstra_dp[r][c] < total_risk:
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                new_risk = total_risk + grid[nr][nc]
                if new_risk < dijkstra_dp[nr][nc]:
                    dijkstra_dp[nr][nc] = new_risk
                    heapq.heappush(h, (dijkstra_dp[nr][nc], nr, nc))

        # if r + 1 < ROWS: heapq.heappush(h, (dijkstra_dp[r + 1][c], r + 1, c))
        # if c + 1 < COLS: heapq.heappush(h, (dijkstra_dp[r][c + 1], r, c + 1))
        # if r - 1 >= 0: heapq.heappush(h, (dijkstra_dp[r - 1][c], r - 1, c))
        # if r - 1 >= 0: heapq.heappush(h, (dijkstra_dp[r - 1][c], r - 1, c))
    return dijkstra_dp[-1][-1]

# get input as grid
if __name__ == "__main__":
    # grid = []
    # with open("AoC_15_input.txt") as f:
    #     for line in f:
    #         grid.append( [ int(num) for num in line[:-1] ] )
    # print(dijkstra(grid))

    gridx5 = []
    # with open("AoC_15_input_sample2.txt") as f:
    with open("AoC_15_input.txt") as f:
        for i in range(5):
            f.seek(0)
            for line in f:
                gridx5.append([])
                for j in range(5):
                    gridx5[-1].extend( [ (int(num) + j + i - 1)%9 + 1 for num in line[:-1] ] )
    print(dijkstra(gridx5))


