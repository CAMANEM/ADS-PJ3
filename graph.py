class Vertex:
    def __init__(self, i):
        self.id = i
        self.neighbor = []
        self.visited = False
        self.dad = None
        self.distance = float('inf')

    def add_neighbor(self, v, p):
        if v not in self.neighbor:
            self.neighbor.append([v, p])


class Graph:
    def __init__(self):
        self.apex = {}

    def add_apex(self, idf):
        if id not in self.apex:
            self.apex[idf] = Vertex(idf)

    def add_edge(self, a, b, p):
        if a in self.apex and b in self.apex:
            self.apex[a].add_neighbor(b, p)
            # self.apex[b].add_neighbor(a, p)

    def path(self, a, b):
        path = []
        actual = b

        while actual is not None:
            path.insert(0, actual)
            actual = self.apex[actual].dad
        return [path, self.apex[b].distance]

    def minimum(self, array):
        if len(array) > 0:
            m = self.apex[array[0]].distance
            v = array[0]

            for i in array:
                if m > self.apex[i].distance:
                    m = self.apex[i].distance
                    v = i
            return v

    def maximum(self, array):
        if len(array) > 0:
            m = self.apex[array[0]].distance
            v = array[0]
            for i in array:
                if m < self.apex[i].distance:
                    m = self.apex[i].distance
                    v = i
            return v

    def dijkstra_min(self, a):
        if a in self.apex:
            self.apex[a].distance = 0
            actual = a
            not_visited = []

            for v in self.apex:
                if v != a:
                    self.apex[v].distance = float('inf')
                self.apex[v].dad = None
                not_visited.append(v)

            while len(not_visited) > 0:
                for i in self.apex[actual].neighbor:
                    if not self.apex[i[0]].visited:
                        if self.apex[actual].distance + i[1] <= self.apex[i[0]].distance:
                            self.apex[i[0]].distance = (self.apex[actual].distance + i[1])
                            self.apex[i[0]].dad = actual

                self.apex[actual].visited = True
                not_visited.remove(actual)
                actual = self.minimum(not_visited)
        else:
            return False

    def dijkstra_max(self, a):
        if a in self.apex:

            self.apex[a].distance = 0
            actual = a
            not_visited = []

            for v in self.apex:
                if v != a:
                    self.apex[v].distance = 0
                self.apex[v].dad = None
                not_visited.append(v)

            while len(not_visited) > 0:
                for i in self.apex[actual].neighbor:
                    if not self.apex[i[0]].visited:
                        if self.apex[actual].distance + i[1] > self.apex[i[0]].distance:
                            self.apex[i[0]].distance = (self.apex[actual].distance + i[1])
                            self.apex[i[0]].dad = actual

                self.apex[actual].visited = True
                not_visited.remove(actual)
                actual = self.maximum(not_visited)
        else:
            return False

    def reset_visited(self):
        for i in self.apex:
            self.apex[i].visited = False

    def get_ways(self, a, b):
        if a != b:
            self.dijkstra_min(a)
            print(self.path(a, b))

            self.reset_visited()

            self.dijkstra_max(a)
            print(self.path(a, b))

        else:
            print("Same node")


def main():
    hp = Graph()

    hp.add_apex(1)
    hp.add_apex(2)
    hp.add_apex(3)
    hp.add_apex(4)
    hp.add_apex(9)

    hp.add_edge(1, 2, 3)
    hp.add_edge(1, 4, 8)
    hp.add_edge(1, 3, 15)

    hp.add_edge(2, 4, 3)
    hp.add_edge(3, 4, 8)

    hp.add_edge(4, 9, 3)

    hp.get_ways(1, 4)


main()
