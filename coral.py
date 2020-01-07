import random, pylab

class local:
    def __init__(self):
        self.condicao = 0
        self.limiteCorais = 100
        self.listaCorais = []
        self.lAlgasLivres = []
    

class coral:
    def __init__(self, LOCAL, FISIO):
        '''fisio E (-1 e 1) ou G(0)'''
        self.fisio = 0
        self.neutra = '0000000000'
        self.tempoGer =10
        self.limiteAlgas = 100
        self.lAlga = []
    
    
class alga:
    def __init__(self, CORAL, FISIO):
        '''fisio E (-1 e 1) ou G(0)'''
        self.fisio = 0
        self.neutra = '0000000000'
        self.tempoGer = 1
        self.coral = coral

    
def interacao(CORAL, ALGA):
    ''' Funcao da matriz de preferencias '''

    if CORAL.fisio!=0  and ALGA.fisio!=0:
        if CORAL.fisio==ALGA.fisio:
            return 2
        else: return 0
    else: return 1

    
def dinamica(TEMPO = 100, nCORAIS = 1, nALGAS = 10):
    lAlgasAux = []
    tiposAlgasCoral = [0,0,0]
    tiposAlgasTotal = [0,0,0]
    tiposCorais = [0,0,0]
    Alga00tempo = []
    Alga05tempo = []
    Alga10tempo = []
    tempo = range(TEMPO)
    
    l = local()
    c = coral( l, 0 ) 
    for i in xrange(nALGAS):
        c.lAlga.append( alga ( c, random.choice([-1,0,1]) ) )
        if c.lAlga[i].fisio == -1:
            tiposAlgasCoral[0]+=1
        if c.lAlga[i].fisio == 0:
            tiposAlgasCoral[0]+=1
        if c.lAlga[i].fisio == 1:
            tiposAlgasCoral[0]+=1
    
    l.listaCorais.append(c)
    Alga10tempo = []
    for t in tempo:
        for i in l.listaCorais:
            rC = 0
            lAlgasAux = i.lAlga
            for j in i.lAlga:
                rA = interacao( i , j )
                if rA !=1:
                    print rA
                rC += rA
                for a in xrange(rA):
                    if len(lAlgasAux) < i.limiteAlgas:
                        lAlgasAux.append(alga( j.coral , j.fisio ))
                        tiposAlgasCoral[j.fisio + 1]+=1
                        tiposAlgasTotal[j.fisio + 1]+=1
                    else:
                        l.lAlgasLivres.append(alga( j.coral, j.fisio ))
                        tiposAlgasTotal[j.fisio + 1]+=1
            i.lAlga = lAlgasAux
            if t%j.tempoGer==0:
                rC = rC/10
            total = float(len ( i.lAlga ))
            Alga00tempo.append(tiposAlgasCoral[0]/total)
            Alga05tempo.append(tiposAlgasCoral[1]/total)
            Alga10tempo.append(tiposAlgasCoral[0]/total)


##                for o in xrange(rC):
##                    l.listaCorais.append( coral ( l, j.fisio))
    print Alga00tempo, len( tempo)
    pylab.plot(tempo, Alga00tempo, 'b-', label = 'especialista -1')
    pylab.plot(tempo, Alga05tempo, 'k-', label = 'generalista')
    pylab.plot(tempo, Alga10tempo, 'g-', label = 'especialista 1')
    pylab.legend(loc=4)
    pylab.show()
    pylab.close()
if __name__=='__main__':
    dinamica()
