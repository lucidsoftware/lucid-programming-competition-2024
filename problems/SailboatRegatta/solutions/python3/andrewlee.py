import heapq
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)


def solve_sailboat_regatta(
    width: int, length: int, wind_map: List[List[Tuple[int, int]]], K: int
) -> int:
    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < width and 0 <= y < length

    def get_neighbors(state):
        x, y, vx, vy, sail_status, sail_cooldown, time = state
        neighbors = []

        # Move with current velocity
        new_x, new_y = x + vx, y + vy

        # If past the finish line, early return
        if 0 <= new_x < width and new_y >= length:
            return [(new_x, new_y, 0, 0, sail_status, 0, time + 1)]
        if is_valid(new_x, new_y):
            wind_vx, wind_vy = wind_map[new_y][new_x]
            # Option 1: Keep sail raised/lowered
            new_vx, new_vy = vx + wind_vx * sail_status, vy + wind_vy * sail_status
            neighbors.append(
                (
                    new_x,
                    new_y,
                    new_vx,
                    new_vy,
                    sail_status,
                    max(sail_cooldown - 1, 0),
                    time + 1,
                )
            )

            # Option 2: Raise/Lower sail
            if sail_cooldown <= 0:
                new_sail_status = 1 - sail_status
                new_vx, new_vy = (
                    vx + wind_vx * new_sail_status,
                    vy + wind_vy * new_sail_status,
                )
                neighbors.append((new_x, new_y, new_vx, new_vy, new_sail_status, K, time + 1))

        return neighbors

    # Priority queue for Djikstra's algorithm
    pq = [(0, (x, -1, 0, 1, 1, 0, 0)) for x in range(width)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, state = heapq.heappop(pq)
        logger.info(state)
        x, y, vx, vy, sail_status, sail_cooldown, time = state

        if y >= length:  # Reached the finish line
            return time

        if (x, y, vx, vy, sail_status, sail_cooldown) in visited:
            continue
        visited.add((x, y, vx, vy, sail_status, sail_cooldown))

        neighbors = get_neighbors(state)
        logger.info(neighbors)
        for neighbor in neighbors:
            if neighbor[-1] <= length + 1:
                heapq.heappush(pq, (neighbor[-1], neighbor))  # Use time as priority

    return -1  # No solution found


if __name__ == "__main__":
    logger.propagate = False
    W, L, K = map(int, input().strip().split())
    wind_map = []
    for y in range(L):
        row = []
        for coord in input().strip().split():
            row.append(tuple(map(int, coord.split(","))))
        wind_map.append(row)
    result = solve_sailboat_regatta(W, L, wind_map, K)
    print(result)
