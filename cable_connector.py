import heapq


class CableConnector:
    def __init__(self, cables_sizes: list[int]):
        self.cables_sizes = cables_sizes

    def connect(self) -> int:
        if len(self.cables_sizes) <= 1:
            return 0

        heap = self.cables_sizes.copy()
        heapq.heapify(heap)
        total_cost = 0

        while len(heap) > 1:
            first_cable = heapq.heappop(heap)
            second_cable = heapq.heappop(heap)
            merged = first_cable + second_cable
            heapq.heappush(heap, merged)
            total_cost += merged

        return total_cost


if __name__ == "__main__":
    sizes = [7, 3, 12, 1, 6, 15, 4, 9, 5, 10]

    connector = CableConnector(sizes)
    result = connector.connect()

    print(f"Cable sizes: {sizes}")
    print(f"Minimum connection cost: {result}")
