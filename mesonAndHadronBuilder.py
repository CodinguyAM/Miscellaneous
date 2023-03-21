print("Welcome to Advay's Meson and Hadron Builder!")
morb = input("Meson(m) or Hadron(h)?")
def meson(q, aq):
    print('''
                     _
    %s|--------------|%s
   '''% (q, aq))
def h(q1, q2, q3):
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
if morb == 'm':
    print("OK This is the Meson Builder")
    q = input("Quark: ")
    aq = input("AntiQuark: ")
    print("Your meson looks like:  ")
    meson(q, aq)
if morb == "h":
    print("OK This is the Hadron Builder")
    q1 = input("Quark One: ")
    q2 = input("Quark Two: ")
    q3 = input("Quark Three:")
    h(q1, q2, q3)
    
