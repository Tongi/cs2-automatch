import random

def measure_outdoor_temperature():
    # Simulerer måling af udendørs temperatur
    # Simulér ændringer i temperaturen baseret på tid og vejrforhold
    # Her kan du tilføje mere avanceret logik for at simulere realistiske temperaturændringer
    # For eksempel kan du tage højde for tidspunktet på dagen og vejrforhold som solskin, skyer, regn osv.
    # Til dette eksempel bruger vi en simpel tilfældig ændring i temperatur inden for et interval
    current_temperature = 20  # Standard temperaturværdi
    temperature_change = random.uniform(-2, 2)  # Simuler en tilfældig ændring mellem -2 og 2 grader
    current_temperature += temperature_change
    return current_temperature

def adjust_outdoor_temperature(current_temperature, new_temperature):
    # Metode til manuelt at justere den simulerede udendørs temperatur
    return new_temperature

# Eksempel på brug:
# outdoor_temperature = measure_outdoor_temperature()
# print(outdoor_temperature)  # Simuler måling af udendørs temperatur

# Juster den simulerede udendørs temperatur
# new_outdoor_temperature = adjust_outdoor_temperature(outdoor_temperature, 25)
# print(new_outdoor_temperature)
