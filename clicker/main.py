import time
# import keyboard
from turtle import Screen
from scoreboard import Scoreboard
from web3 import Web3
from wallet import Wallet

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d7ba549ef43b443d8ddb7f1fb9d10d9f'))
balance = web3.eth.get_balance('0xC5A66758501De57Cd39EC8087dc4b4BEB8Cbb117')
print(balance)
print(web3.eth.blockNumber)
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(scoreboard.increase_score, 'space')
# screen.onkey(keyboard, "Right")
# screen.onkey("Right")
game_is_on = True

wallet = Wallet('0xC5A66758501De57Cd39EC8087dc4b4BEB8Cbb117', round(web3.fromWei(balance, "ether"), 4))

while game_is_on:
    screen.update()
    wallet.goto(300, 300)
    wallet.write(f"Balance: {wallet.balance} ETH", align='right', font="20")
    # scoreboard.write(f"Address {wallet.address}")
    wallet.goto(50, 300)
    wallet.write(f"Address: {wallet.address}", align='right', font="20", )
    time.sleep(0.1)

    # if screen.onkey(keyboard) == 1:
    #     scoreboard.increase_score()
