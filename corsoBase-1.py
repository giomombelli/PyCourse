# Carico PACCHETTO
from turtle import end_fill
from unittest import result
import numpy as np

# eseguo FUNZIONE
np.log(10)

# Alternativa
from numpy import * # importa tutte le funzioni nel pacchetto - molto SCONSIGLIATA
log(10)

###################
##### MATRICI #####

# Creo una matrice A
A=np.matrix([[10,-4,5],[7,-2,1]])
A # per vedere la matrice

np.matrix('10,-5,5;7,-2,1') # scrittura alternativa

# NB: il primo elemento di una matrix è in posizione 0
A[0,0] 
A[:,1] # tutte le righe, prima colonna
A[1,:] # tutte le colonne, prima riga
A[0:2,0:2] # tutte le righe da 0 a 2, tutte le colonne da 0 a 2 - NB Esclude estremo destro! (è una 2x2)

B=A[0:2,0:2]
B

# Trasposta
A.T

# Inversa
B.I
np.linalg.inv(B)

# Prodotto tra una matrice e la sua inversa (matrice IDENTITà)
B.I*B

# Determinante
np.linalg.det(B)

# Prodotto (colonne della prima = righe della seconda)
B*A

# Inserimento di due vettori
x=np.matrix('1;3;5')
y=np.matrix('-1;0;4')
# Prodotto matriciale
x.T*y
# Prodotto elemento per elemento (.* di Matlab)
np.multiply(x,y)

# Creare numeri casuali
np.random.normal(0,1,10) # 10 numeri casuali da una normale standard ~N(0,1)

X=np.random.normal(0,1,10000)
X

# MEDIA
np.mean(X)

# Deviazione standard
np.std(X)

# Quantili
np.quantile(X,[0,0.5,1]) # 3 quantili che isolano alla propria sinistra una probabilità pari ai tre valori inseriti

np.max(X) # deve corrispondere al 1-quantile 

##################
#### FUNZIONI ####

# ES: Creare una funzione che simula il lancio dei dadi
def lancioDadi(numeroDadi,numeroFacce):
    D = np.random.random_integers(1,numeroFacce,numeroDadi)
    S=np.sum(result)
    return D, S

lancioDadi(2,6)

D,S=lancioDadi(2,6)

#Array degli esiti di ogni dado
lancioDadi(4,8)[0]

#Somma dei dadi che ho lanciato
lancioDadi(4,8)[1]

# nuova funzione con set base
def dadi(n=1,f=6):
    return np.random.random_integers(1,f,n)

dadi()
dadi(12)
dadi(f=12,n=2)
dadi(n=2,f=12) # l'ordine non influenza la funzione SE indico il nome delle variabili

# Ciclo FOR
for i in [1,2,3]:
    print(i**2) # i**2 ELEVAMENTO A POTENZA i^2

#####################
#### RANDOM WALK ####

# Definisco il vettore W
n=10 # numero di simulazioni
W=np.zeros((n,1)) #vettore colonna di n zeri
W

# +1,-1 con p=0.5 come (2*binomiale)-1
for i in range(1,n):
    W[i]=W[i-1]+2*np.random.binomial(1,0.5)-1
W
