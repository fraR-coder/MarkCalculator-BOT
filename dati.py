class Dati:
    giusta = 0
    sbagliata = 0
    bianca = 0
    N = 0
    soglia =0

    def __init__(self, N, giusta,  sbagliata,  bianca,  soglia) :
        self.giusta = int(giusta)
        self.sbagliata = float(sbagliata)
        self.bianca = float(bianca)
        self.N = int(N)
        self.soglia = float(soglia)
        
