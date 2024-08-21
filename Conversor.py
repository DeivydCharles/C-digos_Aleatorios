from datetime import datetime

# Convertendo milissegundos em segundos
milliseconds = int(input("Digite o milisegundo: "))

#milliseconds = 1724238057000

seconds = milliseconds / 1000.0

# Convertendo para um objeto datetime
date_time = datetime.utcfromtimestamp(seconds)

# Saída em um formato de data
date_time.strftime('%Y-%m-%d %H:%M:%S')
for i in range(15):
    print()
print(date_time)
for i in range(5):
    print()
