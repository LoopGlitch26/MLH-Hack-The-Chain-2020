import json
from web3 import Web3
from abi import abi
from flask import Flask, request, render_template

app = Flask(__name__)

infura_url="https://mainnet.infura.io/v3/9ed572719f7d4dc28a1e376ef55eb9d3"
web3 = Web3(Web3.HTTPProvider(infura_url))


def getData(abi, address):
    """

    """
    try:
        contract = web3.eth.contract(address=address, abi=abi)

        totalSupply = contract.functions.totalSupply().call()

        # balance = contract.functions.balanceOf(balanceAddress).call()
        return contract.functions.name().call(), web3.fromWei(totalSupply, 'ether'), contract.functions.symbol().call()
    except:
        pass

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tokenName, supply, symbol = getData(request.form.get("abi"), request.form.get("address"))
        return render_template("results.html", name=tokenName, supply=supply, symbol=symbol)
    else:
        return render_template("index.html")