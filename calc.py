from dati import Dati
class TestApp :
    punti = 0.0
    K = 3
    pos = 0
    start = 0
    count = 0
    N=0
    giusta=0
    sbagliata=0
    bianca=0
    soglia=0
    val = None
    sol = None
    dati= None

    def  getN(self) :
        return self.N
    def  getK(self) :
        return self.K
    def setK(self, k) :
        self.K = k
    def __init__(self, dati,  K) :
        self.dati= dati
        self.giusta=dati.giusta
        self.sbagliata=dati.sbagliata
        self.bianca=dati.bianca
        self.N=dati.N
        self.soglia=dati.soglia

        self.K = K
        self.val = [0.0] * (K)
        self.val[0] = self.giusta
        self.val[1] = self.sbagliata
        self.val[2] = self.bianca
        self.sol = [0.0] * (self.N)
        
    def  getPos(self) :
       return self.pos
    def setPos(self, pos) :
        self.pos = pos
    def  getStart(self) :
        return self.start
    def setStart(self, start) :
        self.start = start
    def  getCount(self) :
        return self.count
    def setCount(self, count) :
        self.count = count
    def  getVal(self) :
        return self.val
    def setVal(self, val) :
        self.val = val
    def  getSol(self) :
        return self.sol
    def setSol(self, sol) :
        self.sol = sol
    def setN(self, n) :
        self.N = n
    def  getSoglia(self) :
        return self.soglia
    def setSoglia(self, soglia) :
        self.soglia = soglia
    def  getGiusta(self) :
        return self.giusta
    def setGiusta(self, giusta) :
        self.giusta = giusta
    def  getSbagliata(self) :
        return self.sbagliata
    def setSbagliata(self, sbagliata) :
        self.sbagliata = sbagliata
    def  getBianca(self) :
        return self.bianca
    def setBianca(self, bianca) :
        self.bianca = bianca
    def  calcola_punti(self, numero_giuste,  numero_sbagliate,  numero_bianche) :
        return ((numero_bianche * self.bianca) + (numero_giuste * self.giusta) + (numero_sbagliate * self.sbagliata))
    def stampa_punteggi(self, numero_giuste,  numero_sbagliate,  numero_bianche,  punti,update) :
        if (punti >= self.soglia) :
            #print(str(numero_giuste) + "              " + str(numero_sbagliate) + "                   " + str(numero_bianche) + "                       (" + str(punti) + ")")
            update.message.reply_text(f'{numero_giuste}                 {numero_sbagliate}                  {numero_bianche}                    {punti}\n')
    
    def  comb_ripet(self, pos,  val,  sol,  n,  start,  count,update) :
        i = 0
        if (pos >= n) :
            a = 0
            b = 0
            c = 0
            i = 0
            while (i < n) :
                if (sol[i] == self.giusta) :
                    a += 1
                if (sol[i] == self.sbagliata) :
                    b += 1
                if (sol[i] == self.bianca) :
                    c += 1
                i += 1
            self.punti = self.calcola_punti(a, b, c)
            self.stampa_punteggi(a, b, c, self.punti,update)
            return count + 1
        i = start
        while (i < self.K) :
            sol[pos] = val[i]
            count = self.comb_ripet(pos + 1, val, sol, n, start, count,update)
            start += 1
            i += 1
        return count
    def prova(self,update) :
        #print("giuste\t    sbagliate\t     bianche\t   punteggio totale\n------------------------------------------------------------------\n")
        
        update.message.reply_text(f"giuste\t    sbagliate\t     bianche\t   punteggio totale\n------------------------------------------------------------------\n")
        self.comb_ripet(self.pos, self.val, self.sol, self.N, self.start, self.count,update)
