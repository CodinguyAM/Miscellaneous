print("This is the Particle Calcifier(Just kidding, it's actually the Particle Classifier)  Please note that this only contains U, D and S Quarks")
Q = input("Enter Quark Content: ")
translator = {"uds":"Neutral Sigma or Lambda", "dds":"Negative Sigma", "uus":"Positive Sigma", "uss":"Neutral Xi", "dss":"Charged Xi", "ddd":"Negative Delta", "udd":"Neutral Delta or Neutron", "uud":"Positive Delta or Proton", "uuu":"Doubly Positive Delta", "sss":"Omega Minus"}
print(translator[Q])
