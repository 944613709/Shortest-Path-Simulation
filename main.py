import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QLineEdit, QLabel, QListWidget, QComboBox, QHBoxLayout)
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class RoutingSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.network_graph = nx.Graph()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Routing Simulator')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # 添加节点
        self.node_input = QLineEdit(self)
        self.node_input.setPlaceholderText('Enter node name')
        layout.addWidget(self.node_input)

        add_node_btn = QPushButton('Add Node', self)
        add_node_btn.clicked.connect(self.add_node)
        layout.addWidget(add_node_btn)

        # 添加边
        self.edge_input = QLineEdit(self)
        self.edge_input.setPlaceholderText('Enter edge as node1-node2')
        layout.addWidget(self.edge_input)

        add_edge_btn = QPushButton('Add Edge', self)
        add_edge_btn.clicked.connect(self.add_edge)
        layout.addWidget(add_edge_btn)

        # 选择起始和目的节点
        self.start_node_selector = QComboBox(self)
        self.end_node_selector = QComboBox(self)
        layout.addWidget(QLabel('Select Start Node:'))
        layout.addWidget(self.start_node_selector)
        layout.addWidget(QLabel('Select End Node:'))
        layout.addWidget(self.end_node_selector)

        # 选择算法
        self.algorithm_selector = QComboBox(self)
        self.algorithm_selector.addItems(['Dijkstra', 'Bellman-Ford'])
        layout.addWidget(QLabel('Select Algorithm:'))
        layout.addWidget(self.algorithm_selector)

        # 显示网络拓扑
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # 运行算法
        run_algorithm_btn = QPushButton('Run Algorithm', self)
        run_algorithm_btn.clicked.connect(self.run_algorithm)
        layout.addWidget(run_algorithm_btn)

        # 路径和转发表显示
        self.shortest_path_label = QLabel('Shortest Path: ')
        layout.addWidget(self.shortest_path_label)
        self.routing_table_list = QListWidget(self)
        layout.addWidget(self.routing_table_list)

        self.setCentralWidget(central_widget)

    def add_node(self):
        node_name = self.node_input.text()
        if node_name and node_name not in self.network_graph:
            self.network_graph.add_node(node_name)
            self.node_input.clear()
            self.start_node_selector.addItem(node_name)
            self.end_node_selector.addItem(node_name)
            self.update_graph()

    def add_edge(self):
        edge_data = self.edge_input.text()
        if '-' in edge_data:
            node1, node2 = edge_data.split('-')
            if node1.strip() in self.network_graph and node2.strip() in self.network_graph:
                self.network_graph.add_edge(node1.strip(), node2.strip())
                self.edge_input.clear()
                self.update_graph()

    def run_algorithm(self):
        start_node = self.start_node_selector.currentText()
        end_node = self.end_node_selector.currentText()
        selected_algorithm = self.algorithm_selector.currentText()

        if start_node and end_node:
            if selected_algorithm == 'Dijkstra':
                path = self.dijkstra_algorithm(start_node, end_node)
            elif selected_algorithm == 'Bellman-Ford':
                path = self.bellman_ford_algorithm(start_node, end_node)

            if path:
                self.show_routing_table(path)
                self.shortest_path_label.setText('Shortest Path: ' + ' -> '.join(path))
                self.highlight_path(path)
            else:
                self.routing_table_list.clear()
                self.shortest_path_label.setText('Shortest Path: No path found')
        else:
            self.routing_table_list.clear()
            self.shortest_path_label.setText('Shortest Path: Invalid nodes selected')

    def dijkstra_algorithm(self, start, end):

        # 手动实现的 Dijkstra 算法
        if start not in self.network_graph or end not in self.network_graph:
            return None
        # 创建距离字典和前驱节点字典
        distances = {node: float('infinity') for node in self.network_graph.nodes}
        predecessors = {node: None for node in self.network_graph.nodes}

        # 设置起始节点的距离为 0
        distances[start] = 0
        nodes = list(self.network_graph.nodes)

        while nodes:
            # 选择距离最小的节点
            current_node = min(nodes, key=lambda node: distances[node])
            nodes.remove(current_node)

            if distances[current_node] == float('infinity'):
                break

            for neighbor in self.network_graph.neighbors(current_node):
                # 确保正确处理了权重
                weight = self.network_graph[current_node][neighbor].get('weight', 1)
                tentative_value = distances[current_node] + weight
                if tentative_value < distances[neighbor]:
                    distances[neighbor] = tentative_value
                    predecessors[neighbor] = current_node

            if current_node == end:
                break

        # 重构最短路径
        path, current_node = [], end
        while predecessors[current_node] is not None:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, start)

        return path if distances[end] != float('infinity') else None

    def bellman_ford_algorithm(self, start, end):
        # 手动实现的 Bellman-Ford 算法
        # 创建距离字典和前驱节点字典
        # 确保起始和目的节点在图中
        if start not in self.network_graph or end not in self.network_graph:
            return None
        distances = {node: float('infinity') for node in self.network_graph.nodes}
        predecessors = {node: None for node in self.network_graph.nodes}

        # 设置起始节点的距离为 0
        distances[start] = 0

        # 对于每个节点，应用松弛技术
        for _ in range(len(self.network_graph.nodes) - 1):
            for u, v in self.network_graph.edges:
                weight = self.network_graph[u][v].get('weight', 1)
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        # 检查负权重循环
        for u, v in self.network_graph.edges:
            weight = self.network_graph[u][v].get('weight', 1)
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative weight cycle")
                return None

        # 重构最短路径
        path, current_node = [], end
        while predecessors[current_node] is not None:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        path.insert(0, start)

        return path if distances[end] != float('infinity') else None

    def update_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.network_graph)
        nx.draw(self.network_graph, pos, with_labels=True, ax=self.ax)
        self.canvas.draw()

    def highlight_path(self, path):
        self.ax.clear()
        pos = nx.spring_layout(self.network_graph)
        # 绘制所有节点和边
        nx.draw(self.network_graph, pos, with_labels=True, ax=self.ax, node_color='blue', edge_color='black')
        # 突出显示路径
        path_edges = list(zip(path, path[1:]))  # 将 zip 对象转换为列表
        nx.draw_networkx_nodes(self.network_graph, pos, nodelist=path, node_color='red', ax=self.ax)
        nx.draw_networkx_edges(self.network_graph, pos, edgelist=path_edges, edge_color='red', width=2, ax=self.ax)
        self.canvas.draw()

    def show_routing_table(self, path):
        self.routing_table_list.clear()
        for i in range(len(path)-1):
            self.routing_table_list.addItem(f"From {path[i]} to {path[i+1]}")
        self.routing_table_list.addItem("End of Path")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RoutingSimulator()
    ex.show()
    sys.exit(app.exec_())
