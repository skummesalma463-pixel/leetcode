class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        from collections import deque
        
        m, n = len(classroom), len(classroom[0])
        sx = sy = -1
        litters = []
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sx, sy = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        k = len(litters)
        full_mask = (1 << k) - 1
        
        # Find index of each litter
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        # State: (x, y, mask, current_energy) -> stored as best_energy[x][y][mask] = max_energy
        # Using a 3D list or dictionary for pruning
        best = {}
        
        # Queue stores: (x, y, mask, e, steps)
        # But since edge weights are 1, BFS guarantees minimum steps!
        queue = deque([(sx, sy, 0, energy, 0)])
        best[(sx, sy, 0)] = energy
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y, mask, e, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
                
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                        
                    nmask = mask
                    if classroom[nx][ny] == 'L':
                        idx = litter_map[(nx, ny)]
                        nmask |= (1 << idx)
                        
                    nrg = ne
                    if classroom[nx][ny] == 'R':
                        nrg = energy
                        
                    # Check if we found a strictly better or equal energy state
                    state_key = (nx, ny, nmask)
                    if state_key in best and best[state_key] >= nrg:
                        continue
                        
                    best[state_key] = nrg
                    queue.append((nx, ny, nmask, nrg, steps + 1))
                    
        return -1