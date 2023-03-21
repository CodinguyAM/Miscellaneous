print("Haloo! This is the Computerized Meson-Hadron Collider.")
def hadr(q1, q2, q3):
    print('''

%s|-------------|%s
\               /
 \             /
  \           /
   \         /
    \       /
     \     /
      \   /
       \ /
        %s 
       



'''% (q1, q2, q3))
q = input("Quark for the Meson: ")
aq = input("Antiquark for Meson: ")
Q = input("Quark One for the Hadron: ")
k = input("Quark Two for the Hadron: ")
h = input("Quark Three for the Hadron: ")
had = [Q, k, h]
toad = []
for K in had:
    if K == aq:
        for H in had:
            if H != K:
                toad.append(H)
        toad.append(q)
        print(type(toad))
        print("The result is: ")
        hadr(toad[0], toad[1], toad[2])
try:
    toad[2]
except:
    print("The CMHC is not capable of handling W and Z Interactions so these particles do not interact.")
