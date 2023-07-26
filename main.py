from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSystemTrayIcon
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QIcon
from web3 import Web3
import requests
import operator

class GasTracker(QWidget):
    def __init__(self):
        super().__init__()

        # Load RPC nodes
        self.rpc_nodes = [
            "https://rpc.ankr.com/eth",
            "https://eth-rpc.gateway.pokt.network",
            "https://gateway.tenderly.co/public/mainnet",
            "https://eth-mainnet.public.blastapi.io"
        ]

        # Sort RPC nodes by speed
        self.rpc_nodes = self.sort_nodes_by_speed(self.rpc_nodes)

        self.setWindowIcon(QIcon("ether.ico"))

        self.tray_icon = QSystemTrayIcon(QIcon('ether.ico'), self)
        self.tray_icon.show()

        # Connect to fastest Ethereum node
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_nodes[0]))  # connect to the fastest node

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create a QLabel instance
        self.label = QLabel()
        self.label.setFont(QFont('Arial', 24))  # set font size to 24
        self.label.setAlignment(Qt.AlignCenter)  # center align text

        # Add label to the layout
        layout.addWidget(self.label)

        # Set the layout
        self.setLayout(layout)

        # Set window style
        self.setStyleSheet("""
            QWidget {
                background-color: #333;
            }
            QLabel {
                color: #FFF;
                padding: 20px;
                border-radius: 10px;
            }
        """)

        # Create a QTimer instance
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_gas_price)
        self.timer.start(10000)  # update every 10 seconds

        # Update gas price immediately
        self.update_gas_price()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def update_gas_price(self):
        gas_price = self.w3.eth.gas_price / 1e9  # convert from wei to gwei
        self.label.setText(f'{gas_price} Gwei')
        self.tray_icon.setToolTip(f'{gas_price} Gwei')

        # Change color based on gas price
        if gas_price < 20:
            self.label.setStyleSheet("color: darkgreen;")
        elif gas_price < 40:
            self.label.setStyleSheet("color: darkorange;")
        else:
            self.label.setStyleSheet("color: darkred;")

    def sort_nodes_by_speed(self, nodes):
        node_speeds = {}
        for node in nodes:
            try:
                response = requests.get(node, timeout=5)
                node_speeds[node] = response.elapsed.total_seconds()
            except requests.exceptions.RequestException:
                pass
        sorted_nodes = sorted(node_speeds.items(), key=operator.itemgetter(1))
        return [node[0] for node in sorted_nodes]

if __name__ == '__main__':
    app = QApplication([])
    window = GasTracker()
    window.show()
    app.exec_()