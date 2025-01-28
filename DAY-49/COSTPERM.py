import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        P = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Step 1: Detect cycles and their lengths
        visited = [False] * (N + 1)
        cycles = []
        
        for i in range(1, N + 1):
            if not visited[i]:
                cycle_length = 0
                current = i
                while not visited[current]:
                    visited[current] = True
                    cycle_length += 1
                    current = P[current - 1]
                cycles.append(cycle_length)
        
        # Step 2: If there's only one cycle, cost is 0
        if len(cycles) == 1:
            results.append(0)
            continue
        
        # Step 3: Use a min-heap to merge cycles optimally
        heapq.heapify(cycles)
        total_cost = 0
        
        while len(cycles) > 1:
            smallest = heapq.heappop(cycles)
            next_smallest = heapq.heappop(cycles)
            cost = smallest + next_smallest
            total_cost += cost
            heapq.heappush(cycles, cost)
        
        results.append(total_cost)
    
    # Step 4: Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()