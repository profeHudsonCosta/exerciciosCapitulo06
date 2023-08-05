class Som:
    frequencia = 0

    def setFreq(self, freq):
        self.frequencia = freq
    
    def getFreq(self):
        return(self.frequencia)

class NotaMusical(Som):
    nome = ""

    def __init__(self) -> None:
        super().__init__()
        print("Nota musical criada!")

    def setNome(self, nomeNota):
        self.nome = nomeNota
      
    def getNome(self):
        return(self.nome)


notaDo = NotaMusical()
notaDo.setFreq(132)
notaDo.setNome("Do")

notaRe = NotaMusical()
notaRe.setNome("Ré")
notaRe.setFreq(148)

notaMi = NotaMusical()
notaMi.setNome("Mi")
notaMi.setFreq(166.3)

notas = []

notas.append(notaDo)
notas.append(notaMi)
notas.append(notaRe)

for i in notas:
    print("Dados da nota: ")
    print("Nome: ", i.getNome())
    print("Frequencia: ", i.getFreq())
