

#importador
import pygame, sys
from pygame.locals import *
import random

#Definir valores de color (R,G,B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
PURPLE = (170, 0, 225)
colours = [GREEN, RED, LIGHTBLUE, YELLOW, PURPLE]

#declarando variables globales
leaderboard = {}

score = 0
highestScore = 0
levelNum = 0
difficulty = 0

replay = True
pressed = False
climbDone = False
introDone = False
startDone = False
startOutput = False
gameStart = False
throwBarrel = False
jumpLeft = False
jumpRight = False
jumpStill = False
hit = False
deathScene = False
gameDone = False
winGame = False
winLevel = False
scoreWin = False
winGameSceneOutput = False
winGameSceneDone = False

option = "top"
direction = "right"

platformsX = [55, 55, 51, 60, 56, 56, 56]
platformsY = [9, 10, 8, 9, 11, 9, 9, 11]
platNum = 0

dkClimb = 0
climbCount = 15
platNum = 0
dkJumpX = 378
dkJumpY = 172
dkJumpYNum = 0

marioX = 150
marioY = 720
addJump = -7
jumpCount = 0
jumpPoint = 0 
deathCount = 0
lives = 2

barrelX = []
barrelY = []
throwCountdown = 0
barrelDirection = []
fall = []
fallCount = []
barrelLeft = []
barrelRight = []

platInclineX = [100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720]
inclineCount = 0

ladderX1 = [295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315, 555, 555, 600, 440, 320]
ladderX2 = [305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325, 565, 565, 610, 450, 335]
ladderY1 = [710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309, 314, 417, 241, 154, 232]
ladderY2 = [720, 705, 657, 620, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329, 369, 432, 311, 232, 272]
fullLadderUp = [False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True]
fullLadderDown = [True, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False]

leftBoundariesY = [541, 341]
rightBoundariesY = [638, 438, 244]

barrelLadderX = [320, 610, 560, 280, 160, 250, 400, 610, 350, 160, 300, 610]
barrelLadderY1 = [243, 252, 326, 270, 350, 428, 437, 449, 535, 547, 627, 645]
barrelLadderY2 = [343, 322, 446, 344, 420, 538, 527, 519, 625, 617, 727, 715]
barrelAdjust = [-2, 1, -1, 4, 2, 3, 5, 1, 5, 1, 4, 1]

confettiX = []
confettiY = []
confettiRadius = []
confettiSpeed = []
confettiColour = []

#Define Imageness
title = pygame.image.load("TITULO.png")
start = pygame.image.load("START.png")
winScreen = pygame.image.load("WIN.png")
gameOverScreen = pygame.image.load("lose2.png")
selectIcon = pygame.image.load("selecticon.png")
life = pygame.image.load("alm-life.png")

withLadder = pygame.image.load("withLadder.png")
platform0 = pygame.image.load("platform0.png")
platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")
platform4 = pygame.image.load("platform4.png")
platform5 = pygame.image.load("platform5.png")
platform6 = pygame.image.load("platform6.png")
platforms = [platform0, platform1, platform2, platform3, platform4, platform5, platform6]
level = pygame.image.load("level.png")

blue0 = pygame.image.load("blue0.png")
blue1 = pygame.image.load("blue1.png")
blue2 = pygame.image.load("blue2.png")
blue3 = pygame.image.load("blue3.png")
blue4 = pygame.image.load("blue4.png")
blue5 = pygame.image.load("blue5.png")
blueNumbers = [blue0, blue1, blue2, blue3, blue4, blue5]
white0 = pygame.image.load("white0.png")
white1 = pygame.image.load("white1.png")
white2 = pygame.image.load("white2.png")
white3 = pygame.image.load("white3.png")
white4 = pygame.image.load("white4.png")
white5 = pygame.image.load("white5.png")
white6 = pygame.image.load("white6.png")
white7 = pygame.image.load("white7.png")
white8 = pygame.image.load("white8.png")
white9 = pygame.image.load("white9.png")
whiteNumbers = [white0, white1, white2, white3, white4, white5, white6, white7, white8, white9]

marioLeft = pygame.image.load("alm-left.png")
marioRight = pygame.image.load("alm-right.png")
runLeft = pygame.image.load("runl.png")
runRight = pygame.image.load("runr.png")
marioJumpLeft = pygame.image.load("jump-left.png")
marioJumpRight = pygame.image.load("jump-right.png")
marioClimb1 = pygame.image.load("almclimb1.png")
marioClimb2 = pygame.image.load("almclimb2.png")
dead = pygame.image.load("dead.png")
marioImage = marioRight

paulineHelp = pygame.image.load("HELP.png")
paulineStill = pygame.image.load("STILL.png")

dkUp1 = pygame.image.load("DKup1.png")
dkUp2 = pygame.image.load("DKup2.png")
dkEmptyClimb1 = pygame.image.load("DKclimb1.png")
dkEmptyClimb2 = pygame.image.load("DKclimb2.png")
dkForward = pygame.image.load("forward.png")
dkLeft = pygame.image.load("DKleft.png")
dkRight = pygame.image.load("DKright.png")
dkDefeat = pygame.image.load("DKdefeat.png")
dkImage = dkForward

barrelStack = pygame.image.load("barrel-stack.png")
barrelDown = pygame.image.load("barrel-down.png")
barrel1 = pygame.image.load("barrel1.png")
barrel2 = pygame.image.load("barrel2.png")
barrel3 = pygame.image.load("barrel3.png")
barrel4 = pygame.image.load("barrel4.png")
barrelSequence = [barrel1, barrel2, barrel3, barrel4]
barrelPic = []

brokenHeart = pygame.image.load("broken-heart.png")
fullHeart = pygame.image.load("full-heart.png")
clock = pygame.time.Clock()
#declara valores para 400 piezas de confettix
for i in range(0, 400):
    #elige el valor x aleatorio y lo agrega a la lista
    x = random.randint(0, 800)
    confettiX.append(x)
    
    #elige el valor y aleatorio, y lo agrega a la lista
    y = random.randint(-500, -100)
    confettiY.append(y)
    
    #elige un radio aleatorio y lo agrega a la lista
    r = random.randint(1, 4)
    confettiRadius.append(r)
    
    #elige velocidad aleatoria y la agrega a la lista
    s = random.randint(5, 20)
    confettiSpeed.append(s)
    
    #elige un color aleatorio y lo agrega a la lista
    colour = random.randint(0,4)
    confettiColour.append(colours[colour])


# instrucciones: genera las instrucciones en la consola
# @param: ninguno
# @retorno: ninguno
def instructions():
    print ("Donkey Kong has kidnapped Pauline!")
    print ("You must now help Mario save her by climbing all the way")
    print ("up the structure to the platform where she is being held.")
    print ("You will have three lives, and you get points by rescuing")
    print ("Pauline and jumping over barrels.")
    print ("To win, save her 5 times or get a score of 999999 or over.")
    print ("Use the arrow keys to move, and press the space to jump.")
    print ("In the menus, use the up and down keys to choose your option")
    print ("and the return key to select it.")
    print ("GOOD LUCK!")




# getName - el usuario ingresa el nombre
# @param: ninguno
# @return: nombre(cadena)
def getName():
    
  

    return 


# highScore: busca el puntaje más alto y agrega el puntaje del usuario actual a la tabla de clasificación
# @param: ninguno
# @return: puntuación más alta (int)
def highScore():
    
#añade la puntuación del usuario
    leaderboard["Player"] = score
    
    #ordenar las puntuaciones de menor a mayor
    scores = leaderboard.values()
    


#outputLeaderboard: ordena las puntuaciones de mayor a menor y las muestra
# @param: ninguno
# @retorno: ninguno
def outputLeaderboard():
    
    # declarar variables
    rank = 1
    scores = leaderboard.values()
    names = leaderboard.keys()
    sortedNames = []

    
    # #repasa todas las partituras
    # para i en el rango(0, len(puntuaciones)):
    # #repasa todos los nombres
    # para j en rango(0, len(nombres)):
            
    # #comprueba si el nombre ya ha sido ordenado
    # if (nombres[j] en nombres ordenados) == Falso:
    # #si la puntuación es la misma que el nombre asociado a la puntuación en la tabla de clasificación, agréguelo a los nombres ordenados
    # if puntuaciones[i] == tabla de clasificación[nombres[j]]:
    # nombres ordenados.append(nombres[j])
    
    # imprimir ("TABLA DE LÍDERES")
    # imprimir ("***********")
    
    # #repasa todas las partituras
    # para i en el rango (len (clasificación) -1, -1, -1):
        
    # #si no es la primera vez que se realiza el ciclo y la puntuación es diferente a la puntuación anterior, y 1 a los rangos
    # si i < len(clasificación)-1:
    # si puntuaciones[i] != puntuaciones[i+1]:
    # rango = rango + 1
        
    #     #producción
    # imprimir (clasificación, "|", nombres ordenados[i], ":", puntuaciones[i])

    # imprimir ("¡GRACIAS POR JUGAR! :)")


# colisionar: comprueba si mario ha chocado o no contra un barril.
# @param: ninguno
# @return: hit(booleano)
def collide() -> bool:
    global hit
    
    #pasa por todos los barriles
    for i in range(0, len(barrelX)):
        #si la imagen de mario toca la imagen del barril en cualquier lugar, el impacto es Verdadero
        if marioX+20 >= barrelX[i] and marioX <= barrelX[i]+26 and marioY+30 >= barrelY[i] and marioY <= barrelY[i]+20:
            hit = True
            
    return hit


# ladderCheck: comprueba si hay o no una escalera en la ubicación de mario
# @param: ninguno
# @return: upLadder(booleano), downLadder(booleano), moveSides(booleano)
def ladderCheck():
    global marioY
    
    #declara variables
    upLadder = False
    downLadder = False
    moveSides = True
    
   #pasa por todas las escaleras
    for i in range(0, len(ladderX1)):
       # si mario está dentro del alcance de una escalera, puede moverse hacia arriba, hacia abajo y hacia los lados
        if marioX >= ladderX1[i] and marioX <= ladderX2[i] and marioY >= ladderY1[i] and marioY <= ladderY2[i]:
            downLadder = True
            upLadder = True
            moveSides = False
            
            #si mario está en lo alto de una escalera, no puede subir más
            if marioY == ladderY1[i]:
                upLadder = False
                
                #si la escalera no se rompe al subir, puede moverse hacia los lados cuando esté arriba
                if fullLadderUp[i]:
                    moveSides = True      
            
           #si mario está al final de la escalera, no puede bajar más
            if marioY == ladderY2[i]:
                downLadder = False
                
                #si la escalera no se rompe al bajar, puede moverse hacia los lados cuando esté abajo
                if fullLadderDown[i]:
                    moveSides = True
        
        #salir del bucle para dejar de buscar qué escalera mario porque la computadora ya la encontró
        if upLadder or downLadder:
            break
            
    return upLadder, downLadder, moveSides


# inclinación: mueve a Mario hacia arriba para que pueda inclinarse al caminar o saltar sobre la plataforma.
# @param: y(int), x(int), dirección(cadena), objeto(cadena)
# @return: y(int) o mover(int)
def incline(y, x, direction, objectt):
    global inclineCount
    
    #Las líneas 344 a 371 verifican en qué plataforma se encuentra el objeto y luego declaran el rango donde se inclina el objeto y cuánto se mueve verticalmente cuando va hacia la derecha en una parte inclinada.
    
    #si el objeto está en la plataforma inferior
    if y <= 720 and y >= 657:
        startNum = 6
        endNum = len(platInclineX) - 1
        move = 3
        
    #si el objeto está en la segunda o cuarta plataforma
    elif (y <= 638 and y >= 553) or (y >= 353 and y <= 438):
        startNum = 0
        endNum = len(platInclineX) - 2
        move = -3
        
   #si el objeto está en la tercera o quinta plataforma
    elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):
        startNum = 1
        endNum = len(platInclineX) - 1
        move = 3
        
    #si el objeto está en la plataforma superior
    elif y <= 245 and y >= 149:
        startNum = 8
        endNum = len(platInclineX) - 2
        move = -3
    
    #si no está en una plataforma (en una escalera)
    else:
        startNum = 0
        endNum = 0
        move = 0
    
    #recorre la lista platIncline list, con un rango de números diferentes dependiendo de en qué plataforma se encuentre el objeto
    for i in range(startNum, endNum):
        
        #si el objeto tiene la misma x que uno de los puntos de inclinación x, el objeto se inclinará hacia arriba o hacia abajo
        if x == platInclineX[i]:
            
            #si el objeto es mario y está saltando hacia la izquierda o hacia la derecha, lleva la cuenta de cuántas pendientes ha pasado mientras salta
            if (jumpLeft or jumpRight) and objectt == "mario":
                inclineCount = inclineCount + 1    
            
            #más descubre en qué dirección se está moviendo
            else:
                #si es correcto, menos mover de y
                if direction == "right":
                    y = y - move
                #si queda a la izquierda, agrega mover a y                  
                elif direction == "left":
                    y = y + move
    
    #returns move si la función es para mario al saltar
    if (jumpLeft or jumpRight) and objectt == "mario":
        return move
    #else devuelve el nuevo valor de y
    else:
        return y


# límites: comprueba todos los límites de los barriles de Mario.
# @param: ninguno
# @return: izquierda (booleana), derecha (booleana)
def boundaries(x, y):
    # declarar variables
    left = True
    right = True
    
    #si x está en ese rango, mario ha alcanzado un posible límite a su izquierda
    if x <= 105 and x >= 96:
        #pasa por la coordenada y de los límites izquierdos
        for i in range(0, len(leftBoundariesY)):
            
            #si Mario también está en ese rango del límite y, la izquierda es falsa y Mario no puede moverse hacia la izquierda.
            if y <= leftBoundariesY[i] and y >= leftBoundariesY[i] - 49:
                left = False
                
    #si x está en ese rango, mario ha alcanzado un posible límite a su derecha            
    elif x >= 660 and x <= 669:
        #pasa por la coordenada y de los límites derechos
        for i in range(0, len(rightBoundariesY)):
            
            #si mario también está en ese rango del límite y, la derecha es falsa y mario no puede moverse hacia la derecha
            if y <= rightBoundariesY[i] and y >= rightBoundariesY[i] - 49:
                right = False
                     
    return left, right


# introScene: la escena de inicio del juego.
# @param: ninguno
# @retorno: ninguno
def introScene():
       #si DK ha subido menos de 390 píxeles, borra el fondo con la escalera
        if dkClimb <= 390:
            screen.blit(withLadder, (48, 0))
            
            #imágenes cambiarán para que parezca que DK se está moviendo
            #si dkClimb es divisible por 30, borra la primera imagen de ascenso
            if dkClimb % 30 == 0:
                screen.blit(dkUp2, (350, 660-dkClimb))
                
           #else borra la otra imagen de ascenso
            else:  
                screen.blit(dkUp1, (370, 660-dkClimb))
        
        #si DK ha subido entre 390 y 580 píxeles, borre la plataforma 0 y mantenga la imagen de dk como dkUp2    
        elif dkClimb > 390 and dkClimb <= 580:
            screen.blit(platform0, (55, 9))
            screen.blit(dkUp2, (350, 660-dkClimb))
        
        #si DK termina de escalar, bloquea las vigas de las plataformas que caen, Pauline y DK saltan (y popr si acaso pauline es Peach la princesa)
        if climbDone:
            screen.blit(platforms[platNum], (platformsX[platNum], platformsY[platNum]))
            pauline(paulineStill)
            screen.blit(dkForward, (dkJumpX, dkJumpY))


# startScreen: genera la pantalla de inicio
# @param: ninguno
# @retorno: ninguno
def startScreen():
    #imagen borrada
    screen.blit(start, (48, 0))


# backgroud - genera el nivel y la pila de barriles
# @param: ninguno
# @retorno: ninguno
def background():
    #imagen borrada
    screen.blit(level, (31, -14))
    screen.blit(barrelStack, (60, 188))


# dk - muestra DK en la pantalla
# @param: ninguno
# @retorno: ninguno
def dk():
    #imagen borrada
    screen.blit(dkImage, (130, 176))


# mario - outputs Mario onto screen
# @param: none
# @return: none
def mario():
    #imagen borrada
    screen.blit(marioImage, (marioX, marioY))
 
 
# pauline - muestra a pauline en la pantalla
# @param: paulinePic(imagen)
# @retorno: ninguno
def pauline(paulinePic):
    #imagen borrada
    screen.blit(paulinePic, (335, 133))


#barrels: coloca todos los barriles en la pantalla.
# @param: ninguno
# @retorno: ninguno
def barrel():
    #revisa todos los barriles para encontrar la información de cada barril y poder destruirlo
    for i in range(0, len(barrelPic)):
        screen.blit(barrelPic[i], (barrelX[i],barrelY[i]))


# vidas: representación visual de cuántas vidas le quedan a Mario
# @param: ninguno
# @retorno: ninguno
def marioLives():
    #recorre todas las vidas que te quedan
    for i in range(0, lives):
        #blit imágenes, sumando 20 a la y cada vez que ejecutas el bucle
        screen.blit(life, (60+i*20, 100))


#levelNumber - borra el número de nivel
# @param: ninguno
# @retorno: ninguno
def levelNumber():
    #pasa por todos los números azules
    for i in range(0, len(blueNumbers)):
       #si el dígito de las decenas es igual a i, borra la imagen del número
        if levelNum / 10 == i:
            screen.blit(blueNumbers[i], (611, 86))
        #si el dígito de las unidades es igual a i, borra la imagen del número
        if levelNum % 10 == i:
            screen.blit(blueNumbers[i], (635, 86))


# playerScores - borra las puntuaciones
# @param: puntuaciónType(int), puntuaciónX(int), puntuaciónY(int)
# @retorno: ninguno
def playersScores(scoreType, scoreX, scoreY):
    
    #declara variables
    tempScore = str(scoreType)
    numOfZero = 6-len(tempScore)
    
    #pasa para borrar todos los ceros necesarios delante del marcador
    for i in range(0, numOfZero):
        screen.blit(whiteNumbers[0], (scoreX, scoreY))
        
        #suma 24 para espaciar el número cada vez
        scoreX = scoreX + 24
    
    #recorre cada dígito/número de la cadena
    # para i en rango(0, len(tempScore)):
    # #recorre los números del 0 al 10
    # para j en el rango (0, 10):
            
    # #cambiar tempScore[i] a entero para compararlo con j
    # #si son iguales, genera la imagen del número correspondiente
    # si int(tempScore[i]) == j:
    # screen.blit(whiteNumbers[j], (puntuaciónX, puntuaciónY))
                
    # #suma 24 para espaciar el número cada vez
    # puntuaciónX = puntuaciónX + 24

# win: imágenes generadas cuando completas un nivel
# @param: ninguno
# @retorno: ninguno
def win():
    
    #imágenes borradas 
    background()
    screen.blit(marioLeft, (440, 150))
    
    #si DK ha subido menos de 30 píxeles, golpea a Pauline con todo el corazón
    if dkClimb <= 30:
        pauline(paulineStill)
        screen.blit(fullHeart, (386, 130))
    #si no, simplemente destruye un corazón roto
    else:
        screen.blit(brokenHeart, (387, 130))
    
    #si no se gana el juego, cambia entre dos imágenes para borrar
    if winGame == False:
        if dkClimb % 30 == 0:
            screen.blit(dkImage1, (240 - moveOver1, 160-dkClimb))
        else:  
            screen.blit(dkImage2, (240 - moveOver2, 160-dkClimb))
            
    #else simplemente borra DK     
    else:
        dk()


# end - muestra el final del juego
# @param: endScreen(imagen)
# @retorno: ninguno
def end(endScreen):
    
    #imagen borrada
    screen.blit(endScreen, (0, 30))
    
    #si se selecciona la opción inferior, borre el icono al lado de la opción inferior
    if option == "bottom":    
        screen.blit(selectIcon, (270, 640))
    
    #else bárralo junto a la opción superior
    else:
        screen.blit(selectIcon, (270, 575))
 

# confetti: genera confeti en la pantalla
# @param: ninguno
# @retorno: ninguno
def confetti():
    
    #pasa por las 400 piezas de confeti
    for i in range(0, 400):
        #blit imagen con la información correcta del confeti para cada pieza
        pygame.draw.circle(screen, confettiColour[i], (confettiX[i], confettiY[i]), confettiRadius[i], 0) 


        
# @redraw_screen - función que vuelve a dibujar la pantalla
def redraw_screen():
    
    #buscar variables globales
    global climbDone
    global gameStart
    global gameDone
    global winGameSceneDone
    global startDone
    global startOutput
    
    #color de relleno de la pantalla
    screen.fill(BLACK)
    
    #comandos de dibujo

    #si el juego finaliza, muestra la pantalla final, el usuario y la puntuación más alta
    if gameDone:
        #llamadas a funciones de dibujo
        end(gameOverScreen)
        playersScores(score, 388, 387)
        playersScores(highestScore, 485, 445)
    
    #si winGame es True, ve a las secuencias de juegos ganadores
    elif winGame:
        #si esto es cierto, borra las imágenes para mostrar el momento en que DK es derrotado.
        if winGameSceneOutput:
            #llamadas a funciones de dibujo
            win()
            marioLives()
                
            levelNumber()
            playersScores(score, 88, 40)
            playersScores(highestScore, 327, 40)
        
        #si esto es cierto, muestra el menú del juego ganador con confeti
        elif winGameSceneDone:
            #llamadas a funciones de dibujo
            end(winScreen)
            confetti()
            playersScores(score, 388, 387)
            playersScores(highestScore, 485, 445)
    
    #else el usuario no ha ganado o perdido el juego todavía
    else:
        #si se pressed es falso, la pantalla de título se está borrando
        if pressed == False:
            screen.blit(title, (54, 18))
        
        #si se pressed es verdadero y introDone, borra la secuencia de introducción
        elif pressed and introDone == False:
            #llamadas a funciones de dibujo
            introScene()
            marioLives()
        
        #si la introducción finaliza y el juego aún no ha comenzado, cierra la pantalla de inicio
        elif introDone == True and gameStart == False:
            #llamadas a funciones de dibujo
            startScreen()
            marioLives()
            
            #establecer el inicio se realiza restableciendo las variables
            startOutput = True
            startDone = True
        
        #Si el juego ha comenzado y no se gana el nivel o Mario ha muerto, borra las imágenes normales del juego.
        elif (gameStart and winLevel == False) or deathScene:
            #llamadas a funciones de dibujo
            background()
            dk()
            mario()
            pauline(paulineHelp)
            marioLives()
            
            #se borra el barril si scoreWin y deathScene son falsos
            if scoreWin == False and deathScene == False:
                barrel()
        
        #si el usuario gana la secuencia ganadora de salida de nivel
        elif winLevel:
            #llamada a funciones de dibujo
            win()
            marioLives()
        
        #calls drawing fucntions
        levelNumber()
        playersScores(score, 88, 40)
        playersScores(highestScore, 327, 40)
     
   #actualizando
    pygame.display.update()



#imprime instrucciones en la consola
instructions()

#bucle de todo el juego si el usuario quiere seguir reiniciando
pygame.init()
walk = pygame.mixer.Sound("walking\\walking.wav")
jump = pygame.mixer.Sound("jump\\jump.wav")
intro = pygame.mixer.Sound("intro1\\intro1.wav")
death = pygame.mixer.Sound("death\\death.wav")
bac = pygame.mixer.music.load("bacmusic\\bacmusic.wav")
death_cnt = 0
#comenzar a crear un programa gráfico
#Establecer dimensiones de pantalla
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#Nombre de la ventana abierta
pygame.display.set_caption('Donkey Kong')

#juego inicial
inPlay = True
pygame.mixer.music.play(-1)


while replay:

    #seguir ejecutando el bucle y manteniendo la interfaz gráfica mientras inPlay es verdadero
    while inPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        #si la escalada está sucediendo, verifique cuánto ha subido DK
        if pressed == True and climbDone == False:
            #si acaba de comenzar, agregue al número de nivel
            if dkClimb == 0:
                levelNum = levelNum + 1
            
            #si DK ha subido 390 píxeles, retrasar el programa
            if dkClimb == 390:
                pygame.time.delay(500)
            
            #si DK ha alcanzado los 560 píxeles o más, reinicie el número de ascensos más rápido para que parezca que está saltando
            if dkClimb >= 560:
                climbCount = -20
            
            #DK no ha vuelto a llegar a 510 al bajar de su salto, sigue agregando a dkClimb
            if dkClimb != 510 or climbCount != -20:
                dkClimb = dkClimb + climbCount
            
            #else DK ha terminado de subir y la variable se restablece
            else:
                climbDone = True
        
        #si DK ha terminado de escalar pero la introducción aún no ha terminado, continúa con DK saltando
        elif climbDone and introDone == False:
            #si el número de plataforma es menor o igual a 6, DK sigue saltando
            if platNum <= 6:
                #si dkJumpY es 152, restablece en qué dirección salta para comenzar a bajar
                if dkJumpY == 152:
                    dkJumpYNum = 10
                
                #si dkJumpY es 172, restablece en qué dirección salta para comenzar a subir
                if dkJumpY == 172:
                    dkJumpYNum = -10
                    
                    #cambia el platNum para cambiar la imagen de fondo para que "caiga" una plataforma
                    platNum = platNum + 1
                
                #mover DK a la izquierda 12 píxeles
                dkJumpX = dkJumpX - 12
                
                #si platNum no es 6, sigue saltando/cambiando las coordenadas y
                if platNum != 6:
                    dkJumpY = dkJumpY + dkJumpYNum
                
                else:
                    introDone = True
                    pygame.time.delay(1000)
            #de lo contrario, la introducción está lista y espera un segundo antes de continuar.
            #else:
                # introducciónHecho = Verdadero
                # pygame.time.delay(1000)
        
        #si gameStart es verdadero, el juego ha comenzado
        if gameStart:
            
            #si scoreWin y winLevel son falsos, verifique si hay colisiones
            if scoreWin == False and winLevel == False:
                hit = collide()
            
            #comprueba si mario ha alcanzado un límite a su izquierda o derecha    
            moveLeft, moveRight = boundaries(marioX, marioY)
            
            #si el golpe es fallido, mario no ha golpeado un barril y el juego continúa normalmente
            if hit == False:
                
                #comprueba si mario está en una escalera y si puede subir, bajar o ir a la izquierda y a la derecha
                upLadder, downLadder, moveSides = ladderCheck()
                
                #si mario alcanza un valor y menor o igual a 154, ha ganado el juego
                if marioY <= 154:
                    #restablecer variables
                    winLevel = True
                    dkClimb = -15
                    climbCount = 15
                    marioX = 150
                    marioY = 720
                    marioImage = marioRight
                
                #si mario está saltando, cambia los valores de x y/o y en consecuencia
                if jumpLeft or jumpRight or jumpStill:
                    
                    #lleva un registro de cuántos saltos
                    jumpCount = jumpCount + 1
                    
                    #cambios y coordenadas
                    marioY = marioY + addJump
                    
                    #cuando jumpCount sea 7, haz que Mario vuelva a bajar cambiando el número con el que sube/baja
                    if jumpCount == 7:
                        addJump = 7
                    
                    #si jumpCount es 14, mario ha vuelto a bajar
                    if jumpCount == 14:
                        
                        #si mario saltó sobre un barril, suma 100 a la puntuación
                        if jumpPoint == 1:
                            score = score + 100
                        
                        #si mario estaba mirando hacia la derecha, cambia la imagen nuevamente para que él mire hacia la derecha y cambia el valor Y de mario si había saltado algunas pendientes.
                        if direction == "right":
                            marioImage = marioRight
                            marioY = marioY - move*inclineCount
                        #else mario estaba mirando hacia la izquierda, cambia la imagen nuevamente para que él mire hacia la izquierda y cambia el valor Y de mario si había saltado algunas pendientes.
                        else:
                            marioImage = marioLeft
                            marioY = marioY + move*inclineCount
                            
                        #restablecer variables
                        addJump = -7
                        jumpCount = 0
                        jumpPoint = 0
                        inclineCount = 0
                        
                        jumpLeft = False
                        jumpRight = False
                        jumpStill = False
                        
                    #si mario ha alcanzado un límite en los lados, no sumes los valores de x
                    if marioX != 60 and marioX != 710 and (marioX != 320 or marioY >= 232):
                        #comprueba cuántas pendientes saltó mario y si debe moverse hacia arriba o hacia abajo cuando mario aterriza
                        move = incline(marioY, marioX, direction, "mario")
                        
                        #si mario salta hacia la izquierda y puede moverse hacia la izquierda, menos 5 a sus coordenadas x
                        if jumpLeft and moveLeft:
                            marioX = marioX - 5
                        #si mario salta hacia la derecha y puede moverse hacia la derecha, suma 5 a sus coordenadas x
                        elif jumpRight and moveRight:
                            marioX = marioX + 5
                    
                    #pasa por todos los barriles
                    for i in range(0, len(barrelX)):
                        #comprueba si mario ha saltado sobre un barril, si es así, se sumará un punto si completa el salto
                        if marioX >= barrelX[i] and marioX <= barrelX[i]+28 and marioY <= barrelY[i]-23 and marioY >= barrelY[i]-65:
                            jumpPoint = 1 
                            print(marioX)
                
                #scoreWin es falso, sigue rodando los barriles
                if scoreWin == False:
                    
                    #pasa por todos los barriles
                    for i in range(0, len(barrelPic)):
                       #si el barril llega al final de la estructura, haz que el barril desaparezca de la pantalla
                        if barrelX[i] <= 31:
                            barrelX[i] = -30
                            barrelY[i] = -30
                        
                        #si el barril no cae, verifique si está cayendo
                        if fall[i] == False:
                            barrelLeft[i], barrelRight[i] = boundaries(barrelX[i], barrelY[i]-15)
                            
                            #reset variable si el barril ha golpeado una plataforma y no puede moverse ni hacia la izquierda ni hacia la derecha
                            if barrelLeft[i] == False or barrelRight[i] == False:
                                fall[i] = True
                        
                       #comprueba en qué plataforma está el barril para determinar en qué dirección va
                        if (barrelY[i] <= 255 and barrelY[i] >= 243) or (barrelY[i] <= 452 and barrelY[i] >= 415) or (barrelY[i] <= 648 and barrelY[i] >= 611):
                            barrelDirection[i] = "right"
                            
                        elif (barrelY[i] <= 353 and barrelY[i] >= 317) or (barrelY[i] <= 550 and barrelY[i] >= 513) or (barrelY[i] <= 731 and barrelY[i] >= 709):
                            barrelDirection[i] = "left"
                        
                        #Si el barril no está en una escalera, rueda o cae.
                        if barrelPic[i] != barrelDown:
                            
                            #si el Barril no cae, rueda hacia la izquierda o hacia la derecha
                            if fall[i] == False:
                                
                                if barrelDirection[i] == "right":
                                    barrelX[i] = barrelX[i] + 10
                                else:
                                    barrelX[i] = barrelX[i] - 10
                                
                                #comprueba si el barril necesita inclinarse hacia arriba/abajo y cambia el valor en la función
                                barrelY[i] = incline(barrelY[i]-11, barrelX[i], barrelDirection[i], "barrel")
                                barrelY[i] = barrelY[i] + 11
                                # restó 11 y luego lo volvió a agregar para que en la función, los valores que las funciones verifican con el valor y se puedan usar tanto para el barril como para mario

                           #si no, el barril está en proceso de caer.    
                            else:
                               #añadir uno para realizar un seguimiento de cuánto tiempo ha caído
                                fallCount[i] = fallCount[i] + 1
                                
                                #si el cañón cae por el lado izquierdo, x se resta en 5
                                if barrelLeft[i] == False:
                                    barrelX[i] = barrelX[i] - 5
                                
                                #si cae desde la derecha x se suma en 5
                                elif barrelRight[i] == False:
                                    barrelX[i] = barrelX[i] + 5
                                
                                #cambiando y por 7 cada vez    
                                barrelY[i] = barrelY[i] + 7
                                
                                #si el conteo ha llegado a 8, deja de caer y restablece los valores para la próxima vez
                                if fallCount[i] == 8:
                                    #ajustar para asegurarse de que aterrice correctamente en la plataforma
                                    barrelY[i] = barrelY[i] + 6
                                    
                                    #restablecer variables
                                    fallCount[i] = 0
                                    fall[i] = False
                                    barrelLeft[i] = True
                                    barrelRight[i] = True
                            
                           #cambia la imagen del barril cada vez
                            #si la imagen del barril está en el índice 3, cámbiela al índice 0
                            if barrelPic[i] == barrelSequence[3]:
                                barrelPic[i] = barrelSequence[0]
                                
                            #else cámbielo al siguiente número de la lista
                            else:
                                for j in range(0, len(barrelSequence)-1):
                                    if barrelPic[i] == barrelSequence[j]:
                                        barrelPic[i] = barrelSequence[j+1]
                        
                        #si la imagen del barril [i] está bajando, el barril bajará por una escalera y suma 10 al valor y cada vez                
                        else:
                            barrelY[i] = barrelY[i] + 10
                        
                        #recorre todas las coordenadas de la escalera de los barriles
                        for j in range(0, len(barrelLadderX)):
                            #si las coordenadas x del barril son las mismas que las de barrilLadderX[j] y barrilLadderY[j], respectivamente, use un número aleatorio para elegir si el barril debe bajar o no.
                            if barrelX[i] == barrelLadderX[j] and barrelY[i] == barrelLadderY1[j]:
                                barrelChoice = random.randint(0, 1)
                                
                                #si el número aleatorio elegido es 0, la imagen del barril y las coordenadas se restablecerán
                                if barrelChoice == 0:
                                    barrelPic[i] = barrelDown
                                    
                                    #Ajusta un poco porque el cañón que baja es más ancho que las otras imágenes del cañón.
                                    barrelX[i] = barrelX[i] - 2
                            
                            #si el barril ha llegado al final de una escalera, reinicie las variables
                            if barrelX[i]+2 == barrelLadderX[j] and barrelY[i] == barrelLadderY2[j]:
                                barrelPic[i] = barrelSequence[0]
                                barrelX[i] = barrelX[i] + 2
                                
                                #esto asegura que cuando baje, aterrice correctamente en la plataforma en lugar de 5 píxeles demasiado alto, ya que los barriles se mueven 10 píxeles a la vez.
                                barrelY[i] = barrelY[i] + barrelAdjust[j]
                    
                    #si throwBarrel es falso, obtiene un número aleatorio para decidir si DK lanzará otro barril o no.        
                    if throwBarrel == False:
                       #después de cada nivel el alcance será menor, lo que significa una mayor probabilidad de lanzar barriles
                        dkChoice = random.randint(0, 50-difficulty)
                        
                        #si el numero es 0, resetea variables para tirar el barril
                        if dkChoice == 0:
                            dkImage = dkLeft
                            throwBarrel = True
                       #si no, no tires ningún barril.
                        else:
                            dkImage = dkForward
                            throwBarrel = False
                    
                    #si throwBarrel es verdadero, realiza estos cambios
                    if throwBarrel:
                        
                       #add para darle a DK algo de tiempo para conseguir el barril
                        throwCountdown = throwCountdown + 1
                        
                        #si throwCountdown es 20, crea un nuevo barril
                        if throwCountdown == 20:
                            #restablecer variable
                            dkImage = dkRight
                            
                           #declaración de información sobre barriles nuevos
                            barrelX.append(250)
                            barrelY.append(243)
                            barrelDirection.append("right")
                            barrelPic.append(barrel1)
                            fall.append(False)
                            fallCount.append(0)
                            barrelLeft.append(True)
                            barrelRight.append(True)
                            
                        #si throwCountdown llega a 40, restablece las variables cuando DK no estaba lanzando    
                        if throwCountdown == 40:
                            throwCountdown = 0
                            dkImage = dkForward
                            throwBarrel = False
            
            #else, mario es golpeado, comienzan las secuencias de muerte.
            else:
                #if la escena de la muerte no está hecha
                if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.play(death)

                if deathScene == False:
                    #mueve las coordenadas y del mario muerto hacia abajo para asegurarse de que descanse donde estaban sus pies, no donde estaba su cabeza.
                    if deathCount == 0:
                        marioY = marioY + 10
                    
                    deathCount = deathCount + 1
                    
                    #cuando el conteo llega a 60, el breve retraso termina, se reinician las variables y se pierde una vida
                    if deathCount == 60:
                        deathScene = True
                        deathCount = 0 
                        lives = lives - 1
                    
                    #restablece variables
                    marioImage = dead
                    
                #si deathScene es verdadero, restablezca las variables para comenzar nuevamente al principio del nivel
                else:
                    startDone = False
                    gameStart = False
                    throwBarrel = False
                    deathScene = False
                    hit = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    inclineCount = 0
                    jumpPoint = 0
                    marioX = 150
                    marioY = 720
                    addJump = -7
                    jumpCount = 0
                    direction = "right"
                    marioImage = marioRight
                
                #si las vidas son menores que 0, gameDone es True, coloca la puntuación en las tablas de clasificación y encuentra la puntuación más alta usando highScore()
                if lives < 0:
                    gameDone = True
                    highestScore = highScore()
        
        #si la puntuación supera los 999999, ganas el juego
        if score >= 999999:
           #restablecer valores
            score = 999999  #este es el número máximo que puede generar el juego
            scoreWin = True
            dkImage = dkDefeat
        
        #si ganas el nivel, inicia procesos winLevel
        if winLevel:
            #si LevelNum es 5 o ScoreWin es verdadero, restablezca los valores para generar imágenes correctas en redraw_screen
            if levelNum == 5 or scoreWin:
                #si esto es falso, restablece los valores para iniciar el final del juego
                if winGameSceneDone == False:
                    dkImage = dkDefeat
                    winGameSceneOutput = True
                #de lo contrario, agregue las coordenadas y del confeti, busque la puntuación más alta y coloque la puntuación del usuario en la tabla de clasificación.
                else:
                    # recorre todos los círculos de confeti
                    for i in range(0, 400):
                        #add to make if fall down
                        confettiY[i] = confettiY[i] + confettiSpeed[i]
                    highestScore = highScore()
                
                #restablecer valores
                gameStart = False
                winGame = True
            
            #si no, continúa al siguiente nivel
            else:
                
                #DK sube
                dkClimb = dkClimb + climbCount
                
                #si DK sube 15 píxeles, agrega 250 a la puntuación y retrasa el tiempo
                if dkClimb == 15:
                    score = score + 250
                    pygame.time.delay(1000)
                
                #si DK sube menos o igual a 30 píxeles, las dos imágenes son dk no sostienen a peach
                if dkClimb <= 30:
                    dkImage1 = dkEmptyClimb1
                    dkImage2 = dkEmptyClimb2
                    moveOver1 = 0
                    moveOver2 = 0
                #else, dk sostiene a peach en estas dos imágenes
                else:
                    dkImage1 = dkUp1
                    dkImage2 = dkUp2
                    
                   #ajusta la imagen para que suba suavemente
                    moveOver1 = 13
                    moveOver2 = 35
                
                #si DK ha subido 150 píxeles, restablece las variables para el siguiente nivel
                if dkClimb == 150: 
                    winLevel = False
                    climbDone = False
                    introDone = False
                    startDone = False
                    gameStart = False
                    throwBarrel = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    hit = False
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    inclineCount = 0
                    dkClimb = 0
                    platNum = 0
                    climbCount = 15
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    addJump = -7
                    jumpCount = 0
                    direction = "right"
                    
                    #para hacer el siguiente nivel más difícil
                    difficulty = difficulty + 8
            
        #se ocupa de cualquier opción de teclado una vez que se ejecuta el programa
        #busca el evento (acción de usar el teclado)
        pygame.event.get()
        
        # El método get_pressed() genera una lista Verdadero/Falso para el estado de todas las claves.
        keys = pygame.key.get_pressed()
        
        #busca escape para ser presionado
        if keys[pygame.K_ESCAPE]:
            #encuentra la puntuación más alta y la añade al diccionario
            highestScore = highScore()
            
            #reset variables para salir del programa
            inPlay = False
            replay = False
        
        #busca el espacio que se debe presionar para que se presione en Verdadero y comenzar el juego
        if keys[pygame.K_SPACE]:
            pressed = True
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(intro)


        
        #debe satisfacer todas estas condiciones para poder presionar la tecla izquierda, derecha, arriba, abajo, espacio (para saltar) y regresar para hacer cualquier cosa.
        if (gameStart and jumpLeft == False and jumpRight == False and jumpStill == False and winLevel == False and hit == False) or gameDone or winGame:      
            
            #busca que se presione la flecha izquierda
            if keys[pygame.K_LEFT] and moveSides and (marioX != 320 or marioY > 232) and moveLeft and marioX != 60:
                #cambia la y de mario para subir/bajar con la pendiente
                marioY = incline(marioY, marioX, direction, "mario")
                # si mario ya está mirando hacia la izquierda, resta 5 a marioX
                if direction == "left":
                    marioX = marioX - 5
                
                #si las imágenes de mario son marioLeft cámbialas a runLeft
                if marioImage == marioLeft:
                    marioImage = runLeft
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)


                #otro, cámbialo a marioLeft
                else:
                    marioImage = marioLeft
                    
                #si se presiona la barra espaciadora mientras también se presiona la izquierda, saltar a la izquierda es Verdadero y cambia la imagen 
                if keys[pygame.K_SPACE]:
                    jumpLeft = True
                    marioImage = marioJumpLeft
                   # si no es pygame.mixer.get_busy():
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(jump)
                
                direction = "left"
            #busca que se presione la flecha derecha
            elif keys[pygame.K_RIGHT] and moveSides and moveRight and marioX != 710:
                #cambia la y de mario para subir/bajar con la pendiente
                marioY = incline(marioY, marioX, direction, "mario")
                
                #si mario ya estaba mirando hacia la derecha, suma 5 al valor de x
                if direction == "right":
                    marioX = marioX + 5
                #si las imágenes de mario son marioRight cámbialas a runRight
                if marioImage == marioRight:
                    marioImage = runRight
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)
                #otro cámbialo a marioRight
                else:
                    marioImage = marioRight
                
                #si se presiona la barra espaciadora mientras también se presiona la derecha, jumpRight es True y cambia la imagen
                if keys[pygame.K_SPACE]:
                    jumpRight = True
                    marioImage = marioJumpRight
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(jump)
                direction = "right"
            
            # busca la flecha hacia arriba para ser presionado
            elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
                pygame.mixer.Sound.stop(walk)
            if keys[pygame.K_UP] and (upLadder or gameDone or winGame):
                # si upLadder es verdadero, mueve a mario hacia arriba 5 píxeles
                if upLadder:
                    marioY = marioY - 5
                    
                    #si marioImage es marioClimb1, cámbialo a marioClimb2
                    if marioImage == marioClimb1:
                        marioImage = marioClimb2
                    #de lo contrario, cámbialo a marioClimb1
                    else:
                        marioImage = marioClimb1
                
                #si el usuario está en uno de los menús, cambie la opción para seleccionar el superior
                if gameDone or winGame:
                    option = "top"
            
           #busca que se presione la flecha hacia abajo y solo se ejecuta cuando puedes bajar una escalera y seleccionar
            if keys[pygame.K_DOWN] and (downLadder or gameDone or winGame):
                #si downLadder es verdadero, cambia las coordenadas y de mario para bajar
                if downLadder:
                    marioY = marioY + 5
                    
                    #si marioImage es marioClimb1, cámbialo a marioClimb2
                    if marioImage == marioClimb1:
                        marioImage = marioClimb2
                    #de lo contrario, cámbialo a marioClimb1
                    else:
                        marioImage = marioClimb1
                
                #si el usuario está en uno de los menús, cambie la opción para seleccionar el inferior
                if gameDone or winGame:
                    option = "bottom"
            
            #busca que se presione la barra espaciadora y solo puede hacer algo cuando mario ya salta hacia la izquierda o hacia la derecha y no estás en medio de una escalera
            if keys[pygame.K_SPACE] and jumpLeft == False and jumpRight == False and moveSides:
                #hace saltarStil verdadero
                jumpStill = True
                
                #si estás mirando hacia la izquierda, borra la imagen de Mario saltando, mirando hacia la derecha.
                if direction == "right":
                    marioImage = marioJumpRight
                    
                #otro blit mario saltando y mirando hacia la izquierda
                else:
                    marioImage = marioJumpLeft
            
            #busca que se presione regresar y solo puede hacer algo cuando el juego se pierde o se gana
            if keys[pygame.K_RETURN] and (gameDone or winGame):
                #si se selecciona la opción superior, reinicia el juego
                if option == "top":
                    
                    #reset variables para reiniciar
                    inPlay = False
                    winLevel = False
                    pressed = False
                    climbDone = False
                    introDone = False
                    gameStart = False
                    startDone = False
                    gameDone = False
                    throwBarrel = False
                    jumpLeft = False
                    jumpRight = False
                    jumpStill = False
                    winGame = False
                    winLevel = False
                    deathScene = False
                    scoreWin = False
                    winGameSceneDone = False
                    score = 0
                    levelNum = 0
                    dkClimb = 0
                    climbCount = 15
                    platNum = 0
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    marioX = 150
                    marioY = 720
                    addJump = -7
                    marioJumpCount = 0
                    lives = 2
                    difficulty = 0
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                
                #si se selecciona la opción inferior, saldrás del juego    
                elif option == "bottom":
                    #restablecer variables
                    inPlay = False
                    replay = False
        clock.tick(30)
        pygame.display.update()      
        if inPlay:
            redraw_screen()                 # la ventana de la pantalla debe redibujarse constantemente - animación
            # pygame.time.delay(30) # pausa durante 20 milisegundos
        
        if startOutput:
            # pygame.time.delay(2000)
            
            startOutput = False
            gameStart = True
        
        if winGameSceneOutput:
            # pygame.time.delay(2500)
            
            winGameSceneOutput = False
            winGameSceneDone = True

    #---------------------------------------#
    pygame.quit()                      # ¡Sal siempre de pygame cuando hayas terminado!        

pygame.quit()