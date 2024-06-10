import random

# Simulate the outdoor temperature measurement
def measure_outdoor_temperature():
    current_temperature = 20  # Standard temperature value
    temperature_change = random.uniform(-2, 2)  # Simulate a random change between -2 and 2 degrees
    current_temperature += temperature_change
    return int(current_temperature)

if __name__ == "__main__":
    print(measure_outdoor_temperature())
