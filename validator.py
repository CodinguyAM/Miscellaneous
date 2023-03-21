print("Hello this is the PPV(Python Particle Validator)")
print("Enter Quarks as udsctb")
print("Press X for no more quarks")
class Particle:
    def __init__(self, qs):
        self.qlist= qs
    def valid(self):
        try:
            dootdeedootdoot = 1/(self.qlist % 1)
            booly = "It's Invalid"
        except:
            booly = "Your particle is Valid"
        return booly
klist = 0.0
third = 1/3
while True:
    print(klist)
    nest = input("Quark(Q) Or AntiQuark(A)?: ")
    if nest == "Q":
        klist = klist + third
    elif nest == "A":
        klist = klist - third
    elif nest == "X":
        break
print(Particle(klist).valid())
        
        

