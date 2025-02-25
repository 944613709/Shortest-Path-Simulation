# 网络拓扑图最短路径模拟 | Shortest Path Simulation

[English](README_EN.md) | 简体中文

## 项目简介

这是一个基于 Python 的网络拓扑图最短路径模拟工具，可以直观地展示和分析网络中的最短路径问题。该工具支持多种经典路由算法，并提供图形化界面进行交互。

## 功能特点

- 💡 直观的图形用户界面
- 🔨 灵活的网络拓扑图创建和编辑功能
- 🚀 支持多种经典路由算法：
  - Dijkstra 算法
  - Bellman-Ford 算法
- 📊 实时图形化展示最短路径
- 🎯 交互式节点和边的操作
- 📝 详细的路由表显示

## 系统要求

- Python 3.x
- 操作系统：Windows/Linux/MacOS

## 安装指南

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/Shortest-Path-Simulation.git
cd Shortest-Path-Simulation
```

### 2. 安装依赖

确保您的系统已经安装了以下依赖库：

```bash
pip install -r requirements.txt
```

主要依赖：
- PyQt5 - GUI框架
- NetworkX - 图形网络处理
- Matplotlib - 图形可视化
- OpenCV-Python - 图像处理支持

## 使用说明

1. 运行程序：
   ```bash
   python main.py
   ```

2. 基本操作：
   - 添加节点：在输入框中输入节点名称，点击"Add Node"
   - 添加边：输入格式为"node1-node2"，点击"Add Edge"
   - 选择算法：从下拉菜单中选择所需算法
   - 选择起始和目标节点：使用相应的下拉菜单
   - 运行算法：点击"Run Algorithm"查看结果

## 功能展示

### 1. 初始界面
![初始界面](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202312261229617.png)

### 2. 运行效果
![运行效果](https://farsblog.oss-cn-beijing.aliyuncs.com/PicGo/202312261230442.png)

## 技术实现

- 使用 PyQt5 构建图形用户界面
- 采用 NetworkX 进行图形数据结构管理
- 使用 Matplotlib 实现图形可视化
- 实现了 Dijkstra 和 Bellman-Ford 两种经典最短路径算法

## 贡献指南

欢迎提交问题和改进建议！如果您想贡献代码：

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的改动
4. 推送到您的分支
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情
