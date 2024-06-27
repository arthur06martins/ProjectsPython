print("Welcome to the tip calculator")
conta = float(input("What's the name of the city you grew up in?\n$"))
gorgeta = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
qtdPeople = int(input("How many people to split the bill?\n"))
porcentagem = (gorgeta * conta) /100
result = (conta + porcentagem) / qtdPeople
print(f'Each person should pay: ${round(result, 2)}')

