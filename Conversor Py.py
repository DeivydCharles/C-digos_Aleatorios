from datetime import datetime, timedelta

# Convertendo milissegundos em segundos
milliseconds = int(input("Digite o milisegundo: "))

#milliseconds = 1724238057000

seconds = milliseconds / 1000.0

# Convertendo para um objeto datetime
date_time = datetime.utcfromtimestamp(seconds)

# UTC do Brasil
brasil_time = date_time - timedelta(hours=3)

# Saída em um formato de data
brasil_time.strftime('%Y-%m-%d %H:%M:%S')
for i in range(10):
    print()
print(brasil_time)
for i in range(5):
    print()