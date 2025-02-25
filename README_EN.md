# Shortest Path Simulation

English | [简体中文](README.md)

## Introduction

A Python-based network topology shortest path simulation tool that visually demonstrates and analyzes shortest path problems in networks. This tool supports multiple classic routing algorithms and provides a graphical interface for interaction.

## Features

- 💡 Intuitive graphical user interface
- 🔨 Flexible network topology creation and editing
- 🚀 Support for multiple classic routing algorithms:
  - Dijkstra's algorithm
  - Bellman-Ford algorithm
- 📊 Real-time graphical visualization of shortest paths
- 🎯 Interactive node and edge operations
- 📝 Detailed routing table display

## System Requirements

- Python 3.x
- Operating System: Windows/Linux/MacOS

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Shortest-Path-Simulation.git
cd Shortest-Path-Simulation
```

### 2. Install Dependencies

Ensure your system has the following dependencies installed:

```bash
pip install -r requirements.txt
```

Main dependencies:
- PyQt5 - GUI framework
- NetworkX - Graph network processing
- Matplotlib - Graphical visualization
- OpenCV-Python - Image processing support

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Basic operations:
   - Add node: Enter node name in the input box, click "Add Node"
   - Add edge: Enter in format "node1-node2", click "Add Edge"
   - Select algorithm: Choose from the dropdown menu
   - Select start and end nodes: Use respective dropdown menus
   - Run algorithm: Click "Run Algorithm" to view results

## Feature Demonstration

### 1. Initial Interface
![Initial Interface](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202312261229617.png)

### 2. Running Effect
![Running Effect](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202312261230442.png)

## Technical Implementation

- Built with PyQt5 for the graphical user interface
- Uses NetworkX for graph data structure management
- Implements visualization using Matplotlib
- Features both Dijkstra and Bellman-Ford classic shortest path algorithms

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details 