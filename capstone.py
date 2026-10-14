# My capstone Project: Flowstation daily log 

class Reading:
    def __init__(self, date, well_tank, pressure, temperature, oil_volume):
        self.date = date
        self.well_tank = well_tank
        self.pressure = pressure
        self.temperature = temperature
        self.oil_volume = oil_volume
        

readings = []

import json

pressure_max = 600
temperature_max = 200

def add_reading():
    
    while True:
        date = input('Enter date: ').strip()
        
        if date == '':
            print("Date cannot be empty. Please enter a valid date.")
        else:
            break
        
    while True:
            well_tank = input('Enter well/tank name: ').strip()
            
            if well_tank == '':
                print("Well/Tank name cannot be empty. Please enter a valid name.")
            else:
                break    
            
    while True:
        try:
            pressure = float(input('Enter pressure reading(psi): '))
            if pressure < 0:
                print("Pressure cannot be negative. Please enter a valid value.")
            elif pressure > pressure_max:
                print(f"Warning: Pressure reading of {pressure} psi exceeds the safety limit of {pressure_max}")
                break
            else:   
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    while True:            
        try:
            temperature = float(input('Enter temperature reading(°F): '))
            if temperature < 0:
                print("Temperature cannot be negative. Please enter a valid value.")
            elif temperature > temperature_max:
                print(f"Warning: Temperature reading of {temperature} °F exceeds the safety limit of {temperature_max}")
                break
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    
    while True:
        try:
            oil_volume = float(input('Enter oil volume reading(bbl): '))

            if oil_volume < 0:
                print("Oil volume cannot be negative. Please enter a valid value.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
    reading = Reading(date, well_tank, pressure, temperature, oil_volume)

    readings.append(reading)
    print('Reading added successfully!')
    print()
    
def view_readings():
    if not readings:
        print('No readings recorded yet.')
        print()
        return
    
    print("\n========== SAVED READINGS ==========")
    for index, reading in enumerate(readings, start=1):
        print(f"\nReading {index}:")
        print("-" * 30)
        print(f"Date: {reading.date}")
        print(f"Well/Tank: {reading.well_tank}")
        print(f"Pressure: {reading.pressure} psi")
        print(f"Temperature: {reading.temperature} °F")
        print(f"Oil Volume: {reading.oil_volume} bbl")

def search_by_well_tank():
    search_name = input('Enter well/tank name to search: ').strip()
    
    found = False
   
    for reading in readings:    
        if reading.well_tank.lower() == search_name.lower():
            print(f"Date: {reading.date}")
            print(f"Well/Tank: {reading.well_tank}")
            print(f"Pressure: {reading.pressure} psi")
            print(f"Temperature: {reading.temperature} °F")
            print(f"Oil Volume: {reading.oil_volume} bbl")
            found = True
           
    if not found:
        print(f"No readings found for well/tank: {search_name}")
        
def view_summary():
    print("\n========== SUMMARY ==========")
    print(f"Total number of readings recorded: {len(readings)}")
    
    
    oil_volumes = [reading.oil_volume for reading in readings]

    print(f"Total oil volume: {sum(oil_volumes)} bbl")
    
    if oil_volumes:
        print(f"Average oil volume: {sum(oil_volumes)/len(oil_volumes)} bbl")
        print(f"Highest oil volume: {max(oil_volumes)} bbl")
        print(f"Lowest oil volume: {min(oil_volumes)} bbl")
    else:
        print("No readings available to calculate average, highest, or lowest oil volume.")
        
def check_safety_limits():
    for reading in readings:
        if reading.pressure > pressure_max:
            print(f"Warning!: Pressure reading of {reading.pressure} psi exceeds the safety limit of {pressure_max}")
        if reading.temperature > temperature_max:
            print(f"Warning!: Temperature reading of {reading.temperature} °F exceeds the safety limit of {temperature_max}")

def save_readings():
    readings_data = []

    for reading in readings:
        reading_data = {
            'date': reading.date,
            'well_tank': reading.well_tank,
            'pressure': reading.pressure,
            'temperature': reading.temperature,
            'oil_volume': reading.oil_volume
        }

        readings_data.append(reading_data)
    with open('readings.json', 'w') as file:
        json.dump(readings_data, file, indent=4)
        

def load_readings():
    global readings

    try:
        with open('readings.json', 'r') as file:
            readings_data = json.load(file)

    except FileNotFoundError:
        print('No saved readings file found. Save some readings first.')
        return False
        
    except json.JSONDecodeError:
        print("Error: The saved readings file contains invalid JSON.")
        return False
    
    readings = []

    for reading_data in readings_data:
        reading = Reading(
            reading_data['date'],
            reading_data['well_tank'],
            reading_data['pressure'],
            reading_data['temperature'],
            reading_data['oil_volume']
        )

        readings.append(reading)
    return True
    
while True:
    
    print('=' * 30)
    print('Flow station daily log manager')
    print('=' * 30)
    print()
    print('1. Add Reading')
    print('2. View Readings')
    print('3. Search by well tank')
    print('4. View Summary')
    print('5. Check safety limits')
    print('6. Save readings')
    print('7. Load readings')
    print('8. Exit')
    print()
    
    choice = input('Enter your choice (1-8): ')
    
    if choice == '1':
        add_reading()
        
    elif choice == '2':
        view_readings()
    
    elif choice == '3':
        search_by_well_tank() 
         
    elif choice == '4':
        view_summary()
        
    elif choice == '5':
        check_safety_limits()
    
    elif choice == '6':
        save_readings()
        print("Readings saved successfully!")
    
    elif choice == '7':
        if load_readings():
            print("Readings loaded successfully!")
        
    elif choice == '8':
        print('Goodbye!')
        break
    else:
        print(f"This feature is not available yet")