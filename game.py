import os
import random
from settings import MIN_NUMBER, MAX_NUMBER, MAX_TRIES


def getRandomNumber(minNumber: int = MIN_NUMBER, maxNumber: int = MAX_NUMBER) -> int:
	"""Generate a random number."""
	
	randomNumber = random.randint(minNumber, maxNumber)
	return randomNumber

def askForInput(question: str) -> str:
	"""Ask a question and return the answer."""

	answer = input(question)
	return answer



	guesses_made = 0

def saveToFile(
		text: str,
		filename: str = "output.txt"
	) -> None:
	"""Save text to file."""

	with open(filename, "a", encoding="utf-8") as file:
		file.write(text + "\n")

def sayHello():
	"""Print initial greeting"""

	print("¡Hola, te damos la bienvenida!")
	print()

def startGame(name: str, minNumber: int = MIN_NUMBER, maxNumber: int = MAX_NUMBER) -> int:
	"""Print instructions."""

	print(f"¡Muy bien, {name}, adivina el número!")
	print(f"Estoy pensando en un número entre {minNumber} y {maxNumber}")
	number = getRandomNumber(minNumber=minNumber, maxNumber=maxNumber)
	return number

def mainGameLoop(secretNumber: int, tries: int = 5) -> tuple:
	"""Main game loop"""
	
	guessesMade = 0
	while guessesMade < MAX_TRIES:
		lastGuess = int(askForInput("Tu apuesta: "))
		guessesMade += 1
		if lastGuess == secretNumber:
			break
		if lastGuess < secretNumber:
			print("Tu apuesta es muy baja.")
		if lastGuess > secretNumber:
			print("Tu apuesta es muy alta.")
	return (lastGuess, guessesMade)

def checkResults(
		secretNumber: int,
		playerName: str,
		playerBet: int,
		totalBets: int
	) -> str:
	"""End of game, check bet and print results"""
	
	if playerBet == secretNumber:
		print(f"¡Buen trabajo, {playerName}, lo adivinaste en {totalBets} intentos!")
		result = "winner"
	else:
		print(f"¡Ooooh, noooo! Lo siento, has perdido, el número secreto era {secretNumber}")
		result = "looser"
	return result

def sayGoodbye(name: str):
	"""Print closing message."""

	print(f"¡Adiós, {name}, hasta la próxima!")



if __name__ == "__main__":
	sayHello()
	playerName = askForInput("¿Cómo te llamas?\n")
	numberToGuess = startGame(playerName)
	lastBet, betsMade = mainGameLoop(numberToGuess, tries=MAX_TRIES)
	winnerOrLooser = checkResults(
		secretNumber=numberToGuess,
		playerName=playerName,
		playerBet =lastBet,
		totalBets = betsMade)
	gameData = f"{playerName}\t{winnerOrLooser}\t{betsMade}"
	saveToFile(gameData, "gameResults.txt")
	sayGoodbye(playerName)
