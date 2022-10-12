
from turtle import Turtle

FONT = ("Arial", 50, "bold")


class Wallet(Turtle):
    def __init__(self, address, balance):
        super().__init__()
        self.color("teal")
        self.penup()
        self.hideturtle()
        self.write(f"")
        self.address = address
        self.balance = balance
