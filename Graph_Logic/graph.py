class Vertex:
    def __init__(self, i):
        self.id = i
        self.neighbor = []
        self.visited = False
        self.dad = None
        self.distance = float('inf')
        self.x = None
        self.y = None
        self.Left_Right = None

    def add_neighbor(self, v, p, s1, s2):
        if v not in self.neighbor:
            self.neighbor.append([v, p, s1, s2])


class Graph:
    def __init__(self):
        self.apex = {}
        self.connections = []

    def add_apex(self, idf, x, y):
        if id not in self.apex:
            self.apex[idf] = Vertex(idf)
            self.apex[idf].x = x
            self.apex[idf].y = y

    def add_edge(self, a, b, p, s1, s2):
        if a in self.apex and b in self.apex:
            self.connections += [[a, b, p]]
            self.apex[a].add_neighbor(b, p, s1, s2)
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

    def get_connections(self):
        return self.connections