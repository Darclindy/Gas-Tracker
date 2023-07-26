# GasTracker
**Read this in other languages: [English](README.en.md), [中文](README.md).**
GasTracker is an Ethereum gas price tracker written in Python and PyQt5. It connects to the fastest Ethereum node and updates the current gas price every 10 seconds. The price is displayed in Gwei (1 Gwei = 1e9 wei).

## Environment Setup

First, you need to install Python and pip. Then, you need to create a virtual environment and activate it. You can use the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

Then, you need to install the dependencies. You can use the following command:

```bash
pip install -r requirements.txt
```

## Usage

After activating the virtual environment and installing all the dependencies, you can run `main.py` to start the program:

```bash
python main.py
```

The program will display an icon in your system tray, through which you can view the current gas price. The price is displayed in different colors depending on its value:

- If the gas price is less than 20 Gwei, the price is displayed in dark green.
- If the gas price is between 20 Gwei and 40 Gwei, the price is displayed in dark orange.
- If the gas price is greater than 40 Gwei, the price is displayed in dark red.

## Note

This program uses the following Ethereum RPC nodes:

- https://rpc.ankr.com/eth
- https://eth-rpc.gateway.pokt.network
- https://gateway.tenderly.co/public/mainnet
- https://eth-mainnet.public.blastapi.io

These nodes are sorted by response speed, and the program automatically connects to the fastest node. If you want to use other Ethereum nodes, you can modify the `rpc_nodes` list in the `main.py` file.