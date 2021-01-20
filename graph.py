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

        while actual != None:
            path.insert(0, actual) #a por 0
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

    def dijkstra1(self, a):
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
                    if self.apex[i[0]].visited == False:
                        if self.apex[actual].distance + i[1] <= self.apex[i[0]].distance: # el signo original es "<"
                            self.apex[i[0]].distance = (self.apex[actual].distance + i[1])
                            self.apex[i[0]].dad = actual

                self.apex[actual].visited = True
                not_visited.remove(actual)
                actual = self.minimum(not_visited) # esta es la original
                #actual = self.maximum(not_visited)
        else:
            return False

    def dijkstra2(self, a):
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
                    if self.apex[i[0]].visited == False:
                        if (self.apex[actual].distance + i[1] < self.apex[i[0]].distance): # el signo original es "<"
                            self.apex[i[0]].distance = (self.apex[actual].distance + i[1])
                            self.apex[i[0]].dad = actual

                self.apex[actual].visited = True
                not_visited.remove(actual)
                #actual = self.minimum(not_visited) # esta es la original
                actual = self.maximum(not_visited)
        else:
            return False

    def reset_visited(self):
         for i in self.apex:
             self.apex[i].visited = False



def main():
    hp = Graph()

    # hp.add_apex(0)
    # hp.add_apex(1)
    # hp.add_apex(2)
    # hp.add_apex(3)
    # hp.add_apex(4)
    #
    # hp.add_edge(0, 1, 3)
    # hp.add_edge(0, 3, 7)
    # hp.add_edge(0, 4, 8)
    #
    # hp.add_edge(1, 2, 1)
    # hp.add_edge(1, 3, 4)
    #
    # hp.add_edge(3, 2, 2)
    #
    # hp.add_edge(4, 3, 3)

    hp.add_apex(1)
    hp.add_apex(2)
    hp.add_apex(3)
    hp.add_apex(4)

    hp.add_edge(1, 2, 3)
    hp.add_edge(1, 4, 8)
    hp.add_edge(1, 3, 15)

    hp.add_edge(2, 4, 3)
    hp.add_edge(3, 4, 8)

    print("\nThe faster way for dijkstra with the cost is: ")

    hp.dijkstra2(1)
    print(hp.path(1, 4))

    hp.reset_visited()

    hp.dijkstra1(1)
    print(hp.path(1, 4))




    #
    #
    #
    # hp.add_edge(0, 2, 1)
    # hp.add_edge(2, 4, 1)
    #
    # hp.dijkstra(0)
    # print(hp.path(0, 4))


    #print("\n The final graph values are: ")
    #hp.print_graph()




main()
