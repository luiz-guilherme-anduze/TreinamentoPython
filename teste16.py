entrada = float(input())

if(entrada >= 0.0) & (entrada <= 25.0):
    print('Intervalo [0,25]')
elif(entrada > 25.0) & (entrada <= 50):
    print('Intervalo (25,50]')
elif(entrada > 50.0) & (entrada <= 75.0):
    print('Intervalo (50,75]')
elif(entrada > 75.0) & (entrada <= 100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')


