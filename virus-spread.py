#Infection radius
INFECTDIST = 1

#Recovery time
#MEAN is average recovery time
#STDDEV is roughly 'variance in time taken to recover'
MEAN = 10
STDDEV = 0.4

#Infection probabilty (probability that infection spreads within INFECTDIST)
PINFECT = 1

#PVACC is probability of vaccination if healthy
#VACCREC is the advantage in recovery given by vaccination
#VACCEXP is vaccine expiration time(if exceeded, person loses immunity)
#VACCINF is the chance of vaccination if infected
PVACC = 0.25
VACCREC = 5
VACCEXP = 10
VACCINF = 0.0


#Probability of Quarantine
PQUAR = 0.0

#Hospital capacity (set to anything more than number of people to remove death)
HCAPACITY = 50

#Number of People
N = 100

#Max position x and y
MAXPX = 25
MAXPY = 25

#Max velocity x and y
MAXVX = 3
MAXVY = 3

#Controls values of pi and e (for recovery time)
E = 2.718281828459045
PI = 3.14159265358979323

#Vaccine mean recovery time
VACCMEAN = MEAN - VACCREC


















import pandas as pd
#import seaborn
import random
import math
import matplotlib.pyplot as plot
import tkinter as tk
import turtle

track = [[], [], [], [], [], []]

main = turtle.Screen()
main.setup(width=25, height=25)
#Note: Column order is:
#x-pos   y-pos  vx    vy   status  infectiontime  quarantined

def generate(number=N, maxx=MAXPX, maxy=MAXPY, maxvx=MAXVX, maxvy=MAXVY, probq=PQUAR, probv=PVACC):
    data = []
    for x in range(number):
        ta =        [maxx * random.random(),
                     maxy * random.random(),
                     maxvx * (random.random() - 0.5) * 2,
                     maxvy * (random.random() - 0.5) * 2,
                     'H',
                     math.inf,
                     int(random.random() < probq and x != 0),
                     int(random.random() < probv),
                     -1 * math.inf]
        if ta[7] == 1:
            ta[8] = 0
        data.append(ta)
    data[0][4] = 'I'
    data[0][5] = 0
    return data

def evolve(current, maxx=MAXPX, maxy=MAXPY, maxvx=MAXVX, maxvy=MAXVY):
    global track, INFECTDIST, MEAN, STDDEV, PVACC, VACCMEAN, VACCINF, VACCEXP, PINFECT
    hh = 0
    hi = 0
    hr = 0
    hd = 0
    hv = 0
    ha = 0
    for person in current:
        ptype = person[4]
        pt = ptype
        if pt == 'H':
            hh = hh + 1
        elif pt == 'I':
            hi = hi + 1
        elif pt == 'R':
            hr = hr + 1
        elif pt == 'D':
            hd = hd + 1
        pv = person[7]
        if pv == 0:
            if random.random() < PVACC and pt == 'H':
                person[7] = 1
                hv = hv + 1
            elif random.random() < VACCINF and pt == 'I':
                person[7] = 1
                hv = hv + 1
            else:
                ha = ha + 1
        elif pv == 1:
            person[8] = person[8] + 1
            if person[8] >= VACCEXP:
                person[8] = -1 * math.inf
                person[7] = 0
                ha = ha + 1
            else:
                hv = hv + 1
        if person[6] == 0:
            person[0] = abs(person[0] + person[2]) % maxx
            person[1] = abs(person[1] + person[3]) % maxy

        #print('I5S: ', person[5], person[5] == 3)
        if person[4] == 'I' and hi > HCAPACITY:
            person[4] = 'D'
            person[5] = math.inf
        if pv == 0:
            if (random.random() < ((E**(((person[5] - MEAN)**2)/(-2*((STDDEV)**2))))/(STDDEV*((2 * PI) ** 0.5)))) and person[4]  == 'I':
                #print('I5R')
                person[4] = 'R'
                person[5] = math.inf
        
        else:
            if (random.random() < ((E**(((person[5] - VACCMEAN)**2)/(-2*((STDDEV)**2))))/(STDDEV*((2 * PI) ** 0.5)))) and person[4]  == 'I':
                #print('I5R')
                person[4] = 'R'
                person[5] = math.inf
        #print(person[4])
        if person[4] == 'I':
            #print('I5A: ', person[5])
            person[5] = person[5] + 1
            #print('I5F: ', person[5])
            for person2 in current:
                #print(person2[4], ((person2[0] - person[0])**2 + (person2[1] - person[1])**2)**0.5)
                if random.random() < PINFECT and person2[4] == 'H' and ((person2[0] - person[0])**2 + (person2[1] - person[1])**2)**0.5 < INFECTDIST and person2 != person:
                    #print('infe')
                    person2[4] = 'I'
                    person2[5] = 0
                person2[2] = maxvx * (random.random() - 0.5) * 2
                person[2] = maxvx * (random.random() - 0.5) * 2
                person2[3] = maxvy * (random.random() - 0.5) * 2
                person[3] = maxvy * (random.random() - 0.5) * 2
    track[0].append(hh)
    track[1].append(hi)
    track[2].append(hr)
    track[3].append(hd)
    track[4].append(hv)
    track[5].append(ha)
def disp(scenario, screen=main):

    global track, MAXPX, MAXPY
    
    screen.clearscreen()
    drawer = turtle.RawTurtle(screen)
    drawer.ht()
    drawer.speed(0)
    drawer.pu()
    
    for person in scenario:
        drawer.goto((person[0] - (MAXPX/2))*15, (person[1] - (MAXPY/2))*15)
        drawer.pd()
        drawer.dot(7, {'H':'green', 'I':'orange', 'R':'blue', 'D':'black'}[person[4]])
        drawer.pu()

    plotd = {'Dead': track[3],
             'Infected': track[1],
             'Healthy': track[0],
             'Recovered': track[2]}
    pdd = pd.DataFrame(plotd, index=list(range(1, len(track[0]) + 1)))
    plotd2 = {'Vaccinated': track[4],
              'Unvaccinated': track[5]}
    pdd2 = pd.DataFrame(plotd2, index=list(range(1, len(track[0]) + 1)))
    plot.clf()
    pdd.plot(kind='bar', stacked=True, color=['black', 'orange', 'green', 'blue'])
    pdd2.plot(kind='bar', stacked=True, color=['green', 'red'])
    plot.show()
    #plot.clf()
    #seaborn.scatterplot(pd.DataFrame(scenario), x=0, y=1, hue=4, style=5, legend=False)
    #plot.show()


sc = generate()
count = 0
def evevha():
    global sc, count
    evolve(sc)
    print(count)
    count = count + 1
    disp(sc)
def rev(n):
    def f():
        for x in range(n):
            evevha()
    return f
root = tk.Tk()
(tk.Button(root, text='Evolve', command=evevha)).grid(row=0, column=0)
        

    
