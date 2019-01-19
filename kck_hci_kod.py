import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("sub1trial4.csv", names=['numer','kanal1','kanal2','kanal3','kanal4','wartosc'])

kanal1 = dane['kanal1']
wartosc = dane['wartosc']
probkowanie=200

popasmowozaporowy= ag.pasmowozaporowy(kanal1, probkowanie, 49, 51)
popasmowoprzepustowy= ag.pasmowoprzepustowy(popasmowozaporowy, probkowanie, 1, 50)

wartoscpoprzednia=0
for i in range(len(popasmowoprzepustowy)):
    if popasmowoprzepustowy[i]>=0.1:
        if wartoscpoprzednia<0.1:
            print(wartosc[i])
    wartoscpoprzednia=popasmowoprzepustowy[i]
