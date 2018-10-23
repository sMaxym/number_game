import happyNumbers
import primeNumber
import ulamNumber
import random


def generateRandomUlam(amount, numberTo, numberFrom = 1):
    randomIndexes = []
    randomUlams = []
    ulams = []
    for num in range(numberTo):
        if ulamNumber.ulamNumbers(num):
            ulams.append(num)
    for i in range(amount):
        randomNumber = random.randint(numberFrom, len(ulams))
        randomIndexes.append((randomNumber))
    for index in randomIndexes:
        randomUlams.append(ulams[index - 1])
    return randomUlams 


def generateRandomHappy(amount, numberTo, numberFrom = 1):
    randomIndexes = []
    randomHappy = []
    happies = []
    for num in range(numberTo):
        if happyNumbers.happyNumbers(num):
            happies.append(num)
    for i in range(amount):
        randomNumber = random.randint(numberFrom, len(happies))
        randomIndexes.append((randomNumber))
    for index in randomIndexes:
        randomHappy.append(happies[index - 1])
    return randomHappy


def generateRandomPrime(amount, numberTo, numberFrom = 1):
    randomIndexes = []
    randomPrimes = []
    primes = []
    for num in range(numberTo):
        if primeNumber.primeNumber(num):
            primes.append(num)
    for i in range(amount):
        randomNumber = random.randint(numberFrom, len(primes))
        randomIndexes.append((randomNumber))
    for index in randomIndexes:
        randomPrimes.append(primes[index - 1])
    return randomPrimes
