#thi# Enter Code here
# Read the README - under files on left
# Delete these three lines before submitting

#this program solves for the future population of country and sees if it will increase or decrease over time

#prompt user to input seconds between birth
sec_birth_str = float(input('enter seconds between birth:'))
sec_birth_int = int(sec_birth_str)

#prompt user to input seconds between death
sec_death_str = float(input('enter seconds between death:'))
sec_death_int = int(sec_death_str)

#prompt user to input immigration
sec_immigration_str = float(input('enter seconds between immigrant:'))
sec_immigration_int = int(sec_immigration_str)

#prompt user to input current population of the country
current_population_str = float(input('enter current population:'))
current_population_int = int(current_population_str)

#prompt user to input years in the future
years_str = float(input('enter years:'))
years_int = int(years_str)

#calculate the change in population
change_in_population_int: float = (((31536000 / sec_birth_int) + (31536000 / sec_immigration_int)-(31536000 / sec_death_int)) * years_int)

#calculate the new population
New_population = current_population_int + change_in_population_int

#output result to user
print('Your population will be :', New_population)

#calculate if the population increased or decreased
if current_population_int < New_population:
    print('the population increased')
else:
    print('the population decreased')

