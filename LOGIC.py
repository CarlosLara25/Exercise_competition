#define NoWinner False

import random as rd

class Participant:
    def __init__(self, name) -> None:
        self.Position = 0
        self.name = name
        self.lastPosition = 66
        self.status = False
    
    def play(self):
        #print(f'Participante {self.name} se encuentra actualmente en {self.Position} esta jugando')
        Move = self.lanzarDados()
        self.Position = self.Position + Move
        #print(f'Se movió {Move} positions y Ahora esta en {self.Position}')
        self.status = self.IsWinner()
        return Move

    def IsWinner(self):
        if self.Position >= self.lastPosition:
            return True
        else:
            return False    
    def lanzarDados(self):
        import random as rd

        posibilities = [ 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3]
        return posibilities[rd.randint(0,14)]
    
    def calculateAvance(self, level, repeticiones):
        avanzar = int(repeticiones/(7+3*level))
        self.Position = self.Position + avanzar

    def calculateRetroceso(self, level, time):    
        avanzar = 5-int(time/(7+5*level))
        if avanzar < 0:
                avanzar = 0
        self.Position = self.Position - avanzar


    
class BOARD:
    def __init__(self, N_participants, names) -> None:
        self.existeGanador = True
        self.noExisteGanador = False
        self.retos = ["Lagartijas", "Fondos", "Abdominales", "Desplantes", "Hombro"]
        self.resistencia = ["Cuerda", "Isometricos", "Plancha", "Sentadilla", "Jumping-Jacks"]       
        self.listActions = {'Nothing':[0, 1, 3, 4, 5, 6, 9, 12, 14, 16, 17, 18, 22, 23, 24,
                                        26, 29, 31, 32, 34, 35, 36, 38, 39, 43, 44, 45, 47, 49,
                                        52, 54, 55, 57, 59, 62, 63, 65 ], 'Water': [10, 20, 30, 40, 60],
                                        'Ladders':[2, 7, 11, 15, 21, 27, 33, 42, 46, 51, 53, 58],
                                        'Snakes':[8, 13, 19, 25, 28, 37, 41, 48, 50, 56, 61, 64]} 
        if (N_participants>1 and N_participants<5):
            self.N_participants = N_participants
            self.Participants = self.setParticipants(names)
            self.statusGame = self.noExisteGanador 
        else:
            print("El número de Participantes debe ser 2, 3 o 4. intenta de nuevo")
            return False
        
    def setParticipants(self, names):
        Participants = []
        for name in names:
            Participants.append(Participant(name))
        return Participants


    def Action(self, Position):
        if Position in self.listActions['Nothing']:
            leyend = "------------"
            accion = "Nothing"
            level = 0
            return accion, leyend, level
        elif Position in self.listActions['Water']:
            leyend = "Tomar un vaso de agua"
            accion = "Water"
            level = 0
            return accion, leyend, level
        elif Position in self.listActions['Ladders']:
            level = int(self.listActions['Ladders'].index(Position)/3)
            leyend = f'Reto para avanzar \n Nivel: {level} \n Reto: {self.retos[rd.randint(0, 4)]} \n Una posicion por cada: {7+3*level} repeticiones' 
            accion = "Reto"
            return accion, leyend, level
        else:
            level = int(self.listActions['Snakes'].index(Position)/3)
            leyend = f'Reto para no retroceder \n Nivel: {level} \n Reto: {self.resistencia[rd.randint(0, 4)]} \n Perderas 5 posiciones, pero puedes reducir una por cada: {7+5*level} segundos soportados'
            accion = "Resistencia"                        
            return accion, leyend, level

    def checkIfPositionIsTaken(self, part):
        for Part in self.Participants:
            if (Part.name != part.name and part.Position == Part.Position and part.Position != 0):
                Part.Position = Part.Position - 1
    
    

    def GAME(self):
        while(self.statusGame == self.noExisteGanador):
            for Part in self.Participants:
                Part.play()
                if Part.status == True:
                    print("Tenemos un ganador!")
                    self.statusGame = self.existeGanador
                    break
                self.checkIfPositionIsTaken(Part)    # Regresar una posicion a quien lo estaba ocupando
                Part.Position = Part.Position + self.Action(Part.Position)

