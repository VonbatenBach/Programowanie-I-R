print('Podaj mase ciala w kilogramach:')
mass = float(input())

print('Podaj wzrost w metrach:')
height = float(input())

bmi = mass/(height**2)

print("BMI={0}".format(bmi))

if(bmi > 18):
    print('Nadwaga!')




