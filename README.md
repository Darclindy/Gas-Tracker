# GasTracker
**Read this in other languages: [English](README.en.md), [中文](README.md).**

GasTracker 是一个使用 Python 和 PyQt5 编写的以太坊Gas跟踪器。它会连接到最快的以太坊节点，并每10秒更新一次当前的Gas价格。价格以 Gwei（1 Gwei = 1e9 wei）为单位显示。

## 环境配置

首先，你需要安装 Python 和 pip。然后，你需要创建一个虚拟环境并激活它。你可以使用以下命令：

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

然后，你需要安装依赖项。你可以使用以下命令：

```bash
pip install -r requirements.txt
```

## 使用方法

在激活虚拟环境并安装了所有依赖项之后，你可以运行 `main.py` 来启动程序：

```bash
python main.py
```

程序会在你的系统托盘中显示一个图标，你可以通过这个图标查看当前的气体价格。价格会根据其值的大小以不同的颜色显示：

- 如果 Gas 价格小于 20 Gwei，价格会显示为深绿色。
- 如果 Gas 价格在 20 Gwei 到 40 Gwei 之间，价格会显示为深橙色。
- 如果 Gas 价格大于 40 Gwei，价格会显示为深红色。

## 注意事项

这个程序使用了以下以太坊 RPC 节点：

- https://rpc.ankr.com/eth
- https://eth-rpc.gateway.pokt.network
- https://gateway.tenderly.co/public/mainnet
- https://eth-mainnet.public.blastapi.io

这些节点是按照响应速度排序的，程序会自动选择最快的节点进行连接。如果你想使用其他的以太坊节点，你可以在 `main.py` 文件中修改 `rpc_nodes` 列表。