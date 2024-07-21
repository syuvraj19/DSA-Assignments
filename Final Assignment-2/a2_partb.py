#    Main Author(s): Yuvraj Singh
#    Main Reviewer(s): Ravneet Kaur and Avreet Kaur

# uncomment the following lines of code if you wish to make use of the linked list or hash table
# in your solution as appropriate
# from a1_partb import DoublyLinked
# from a2_parta import HashTable

class Graph:
    def __init__(self, number_of_verts):
        self.number_of_verts = number_of_verts
        self.vertices = [[] for _ in range(number_of_verts)]

    def add_vertex(self):
        self.number_of_verts += 1
        self.vertices.append([])

    def add_edge(self, from_idx, to_idx, weight=1):
        if not (0 <= from_idx < self.number_of_verts) or not (0 <= to_idx < self.number_of_verts):
            return False

        for to, w in self.vertices[from_idx]:
            if to == to_idx:
                return False  # Edge already exists

        self.vertices[from_idx].append((to_idx, weight))
        return True

    def num_edges(self):
        return sum(len(adj_list) for adj_list in self.vertices)

    def num_verts(self):
        return self.number_of_verts

    def has_edge(self, from_idx, to_idx):
        if 0 <= from_idx < self.number_of_verts and 0 <= to_idx < self.number_of_verts:
            return any(to == to_idx for to, _ in self.vertices[from_idx])
        return False

    def edge_weight(self, from_idx, to_idx):
        if 0 <= from_idx < self.number_of_verts and 0 <= to_idx < self.number_of_verts:
            for edge in self.vertices[from_idx]:
                if edge[0] == to_idx:
                    return edge[1]
        return None

    def get_connected(self, vert):
        if 0 <= vert < self.number_of_verts:
            return self.vertices[vert]
        return []


class LabelGraph:
    def __init__(self, vertex_list):
        self.vertices = {vertex: {} for vertex in vertex_list}

    def add_vertex(self, vertex_name):
        if vertex_name in self.vertices:
            return False  # Vertex already exists
        self.vertices[vertex_name] = {}
        return True

    def add_edge(self, from_vertex, to_vertex, weight=1):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            if to_vertex not in self.vertices[from_vertex]:
                self.vertices[from_vertex][to_vertex] = weight
                return True
        return False

    def num_edges(self):
        return sum(len(adj_list) for adj_list in self.vertices.values())

    def num_verts(self):
        return len(self.vertices)

    def get_verts(self):
        return list(self.vertices.keys())

    def has_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices:
            return to_vertex in self.vertices[from_vertex]
        return False

    def edge_weight(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices[from_vertex]:
            return self.vertices[from_vertex][to_vertex]
        return None

    def get_connected(self, from_vertex):
        if from_vertex in self.vertices:
            connected = self.vertices[from_vertex]
            return [(vertex, weight) for vertex, weight in connected.items()]
        return []
