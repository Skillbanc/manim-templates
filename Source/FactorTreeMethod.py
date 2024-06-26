from manim import *
from AbstractAnim import AbstractAnim
import cvo 

class AbstractAnim(Scene):
    def construct(self):
        pass

def find_factors(n):
    """Return the smallest factor of n other than 1"""
    if n <= 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i, n // i]
    return [n]

def create_factor_tree(n):
    """Generate the factor tree and return the nodes and edges"""
    nodes = []
    edges = []
    node_counter = {}  # To keep track of unique nodes

    def factor_tree(n, parent=None):
        if n in node_counter:
            node_counter[n] += 1
            current_n = f"{n}_{node_counter[n]}"
        else:
            node_counter[n] = 0
            current_n = str(n)
        nodes.append(current_n)
        if parent is not None:
            edges.append((parent, current_n))
        factors = find_factors(n)
        if len(factors) > 1:
            for factor in factors:
                factor_tree(factor, current_n)

    factor_tree(n)
    return nodes, edges

class FactorTreeMethod(AbstractAnim):
    def construct(self):
        self.number = 60  # Example number
        nodes, edges = create_factor_tree(self.number)
        positions = self.calculate_positions(nodes, edges)
        node_mobjects = self.create_node_mobjects(nodes, positions)
        edge_mobjects = self.create_edge_mobjects(edges, positions)

        # Create nodes with labels
        for node in node_mobjects:
            self.play(Create(node))

        # Create edges with arrowheads
        for edge in edge_mobjects:
            self.play(Create(edge))

    def calculate_positions(self, nodes, edges):
        positions = {nodes[0]: np.array([0, 3.25, 0])}  # Root node position shifted upwards

        def set_positions(n, depth, x_offset=0):
            children = [e[1] for e in edges if e[0] == n]
            if children:
                width = len(children) * 2
                for i, child in enumerate(children):
                    if "60" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2, -depth * 2 + 3.5, 0])
                    elif "2_1" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 + 1.5 , -depth * 2 + 3.33, 0])
                    elif "30" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 + 1.5, -depth * 2 + 3.33, 0])
                    elif "2_2" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 - 1, -depth * 2 + 3, 0])
                    elif "15" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 + 1, -depth * 2 + 3, 0])
                    elif "3" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 - 0.5, -depth * 2 + 2.7, 0])
                    elif "5" in child:
                        positions[child] = np.array([x_offset - width / 2 + i * 2 + 2, -depth * 2 + 2.7, 0])
                    else:
                        positions[child] = np.array([x_offset - width / 2 + i * 2, -depth * 2 + 2, 0])
                    set_positions(child, depth + 1, x_offset - width / 2 + i * 2)

        set_positions(nodes[0], 1)
        return positions

    def create_node_mobjects(self, nodes, positions):
        node_mobjects = []
        for node in nodes:
            circle = Circle(radius=0.6, color=WHITE).move_to(positions[node])
            label = Text(node.split('_')[0]).move_to(circle.get_center())
            node_mobjects.append(VGroup(circle, label))
        return node_mobjects

    def create_edge_mobjects(self, edges, positions):
        edge_mobjects = []
        for edge in edges:
            start_pos = positions[edge[0]]
            end_pos = positions[edge[1]]
            line = self.create_arrow(start_pos, end_pos)
            edge_mobjects.append(line)
        return edge_mobjects

    def create_arrow(self, start_pos, end_pos):
        arrow = Arrow(start=start_pos, end=end_pos, buff=0.1, color=WHITE)
        return arrow

if __name__ == "__main__": 
    number = 60  # Example number
    scene = FactorTreeMethod()
    scene.render()