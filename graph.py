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

    def add_apex (self, id):
        if id not in self.apex:
            self.apex[id] = Vertex(id)

    def add_edge (self, a, b, p):
        if a in self.apex and b in self.apex:
            self.apex[a].add_neighbor(b, p)
            #self.apex[b].add_neighbor(a, p)

    def print_graph(self):
        for i in self.apex:
            print("The distance from de vertex " + str(i) + " es " + str(self.apex[i].distance) + " from " + str(self.apex[i].dad))

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

    def dijkstra(self, a):
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
                        if (self.apex[actual].distance + i[1]) < self.apex[i[0]].distance:
                            self.apex[i[0]].distance = (self.apex[actual].distance + i[1])
                            self.apex[i[0]].dad = actual
                self.apex[actual].visited = True
                not_visited.remove(actual)
                actual = self.minimum(not_visited)

        else:
            return False




def main():
    hp = Graph()

    hp.add_apex(1)
    hp.add_apex(2)
    hp.add_apex(3)
    hp.add_apex(4)
    hp.add_apex(5)
    hp.add_apex(6)

    hp.add_edge(1, 6, 14)
    hp.add_edge(1, 2, 7)
    hp.add_edge(1, 3, 9)
    hp.add_edge(2, 3, 10)
    hp.add_edge(2, 4, 15)
    hp.add_edge(3, 4, 11)
    hp.add_edge(3, 6, 2)
    hp.add_edge(4, 5, 6)
    hp.add_edge(5, 6, 9)

    print("\nThe faster way for dijkstra with the cost is: ")
    hp.dijkstra(1)
    print(hp.path(1, 6))
    #print("\n The final graph values are: ")
    #hp.print_graph()




main()
