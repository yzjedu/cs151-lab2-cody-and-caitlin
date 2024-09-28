# Programmers:  Caitlin Burns and Cody King
# Course:  CS151, Professor Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: This program calculates future population
# Data In: The input requires birth rate, death rate, immigration rate, current population,and the amount of years
# Data Out:  This program outputs the future population and if it increased or decreased
# Credits: This code is based on the example we were given in the excel spreadsheet
from math import ceil

#the purpose of this program solves for the future population of country and sees if it will increase or decrease over time

#prompt user to input seconds between birth
sec_birth = float(input('Enter seconds between birth:'))

#prompt user to input seconds between death
sec_death = float(input('Enter seconds between death:'))

#prompt user to input immigration
sec_immigration = float(input('Enter seconds between immigrant:'))

#prompt user to input current population of the country
current_population = float(input('Enter current population:'))

#prompt user to input years in the future
years = float(input('Enter years in the future:'))

#calculate the change in population
change_in_population = (((31536000 / sec_birth) + (31536000 / sec_immigration)-(31536000 / sec_death)) * years)

#calculate the new population
New_population = current_population + change_in_population

#this rounds up to the nearest integer
New_population = ceil(New_population)

#output result to user
print('Your population will be :', New_population)

#calculate if the population increased or decreased
if current_population < New_population:
    print('the population increased')
else:
    print('the population decreased')

