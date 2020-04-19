import turtle 
class Circuito():
    corredores=[] #Serán instancias de tipo turtle.Turtle() 
    __posStartY = (-30,-10,10,30)
    __colorTurtle = ("red", "blue", "green", "orange")
    
    #Estamos poniendo posStartY, en una tupla, por lo que será inmutable. Así que no haría falta simular que es privado, para hacerlo inaccesible.
    
    #Cuando concretamos una clase (que es la definición de un objeto)
    #Ejemplo c = Circuito(), barajas= Circuito() , c y barajas serán instancias, pero tienen la misma funcionalidad. 
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen() #pantalla --> El recuadro donde se van a mover los corredores. Va a ser un objeto de tipo turtle.Screen()
        self.__screen.setup (width, height)
        self.__screen.bgcolor ("lightgray")
        self.__startLine = -width /2 +20 #Linea de salida
        self.__finishLine = width /2 -20 #Línea de llegada
        
        self._createRunners() 
        
    def _createRunners (self):     
        for i in range (4):
            new_turtle = turtle.Turtle ()
            new_turtle.color (self.__colorTurtle [i])
            new_turtle.shape ("turtle") #Las tortugas que se creen, tendrán forma de "turtle"
            new_turtle.penup() #Levanta el boli, no se dibujan las líneas
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) 
                 
            
            self.corredores.append (new_turtle)

if __name__ == "__main__":
    circuito = Circuito (640, 480) 
        
        
        