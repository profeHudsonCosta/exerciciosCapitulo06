class Cliente:
    entrada = ""
    principal = ""
    sobremesa = ""
    bebidas = []

    def setEntrada(self, entrada):
        self.entrada = entrada
    
    def getEntrada(self):
        return(self.entrada)
    
    def setPrincipal(self, principal):
        self.principal = principal

    def getPrincipal(self):
        return(self.principal)
    
    def setSobremesa(self, sobremesa):
        self.sobremesa = sobremesa

    def getSobremesa(self):
        return(self.sobremesa)
    
    def setBebidas(self, novaBebida):
        self.bebidas.append(novaBebida)

    def getBebidas(self):
        return(self.bebidas)
    
    def setMenu(self):
        self.setEntrada("Sopa")
        self.setPrincipal("Massa")
        self.setSobremesa("Sorvete")
        self.setBebidas("Vinho")
    
    def listaPedido(self):
        pedido = {"Entrada":self.getEntrada(), 
                "Principal":self.getPrincipal(),
                "Sobremesa":self.getSobremesa(),
                "Bebidas":self.getBebidas()}
        
        return(pedido)

joaquim = Cliente()
joaquim.setMenu()
print(joaquim.listaPedido())
