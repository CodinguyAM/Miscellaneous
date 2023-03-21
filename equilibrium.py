class Curve:
    def __init__(self, quantAtZero, quantAtOne):
        self.slope = quantAtOne - quantAtZero
        self.q0 = quantAtZero
    def quantAt(self, price):
        return self.slope*price + self.q0
    def priceAt(self, quant):
        return (quant - self.q0) / self.slope
def findeEq(supply, demand, rangePrice):
    for price in range(rangePrice * 100):
        if supply.quantAt(price) == demand.quantAt(price):
            return {"price":price, "quantity":supply.quantAt(price)}

print("Hello! This is my Equilibrium Engine!")
print("Follow intsruction that will show up(quite soon!) in the interface")

p0s = input("Quantity supplied at price $0.00: ")
p1s = input("Quantity supplied at price $1.00: ")
p0d = input("Quantity demanded at price $0.00: ")
p1d = input("Quantity demanded at price $1.00: ")

ran = input("Price range: ")

supply = Curve(p0s, p1s)
demand = Curve(p0d, p1d)

equil = findEq(supply, demand, ran)

print("Equilibrium Quantity is", equil["quantity"])
print("Equilibrium Price is", equil["price"])

