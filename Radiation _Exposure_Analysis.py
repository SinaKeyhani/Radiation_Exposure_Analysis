
# Dictionary containing radiation readings from different locations 
radiation_data = {
    "Urban Area": [22, 19, 20, 31, 28],
    "Industrial Zone": [35, 32, 30, 37, 40],
    "Residential District": [15, 12, 18, 20, 14],
    "Rural Outskirts": [9, 13, 16, 14, 7],
    "Downtown": [25, 18, 22, 21, 26],
    "City Center": [22, 19, 20, 31, 28],
    "Business Park": [28, 26, 29, 30, 27],
    "Shopping Mall": [23, 24, 26, 21, 22],
    "Park": [17, 16, 19, 18, 20],
    "Subway Station": [33, 31, 35, 32, 30]
}

# # calculate and display average radiation level for each area 
def calculate_average(level): 
    return sum(level) / len(level)


# This function witll display the list of areas
def display_areas(y: dict):
    for index, loc in enumerate(y.keys()):
        print(index + 1, loc)


# This function will get the new area from users 
def get_location():
    while True: 
        user_location = input('Please enter the location of your observation: ').capitalize()
        if user_location in radiation_data.keys():
            print(f'{user_location} is already in the list of areas, please try somewhere new!')
        else:
            print(f'{user_location} is a new location, thanks for your effort')
            return user_location


# This function will get the observation for the new area 
def get_observation():
    measurements = []
    print("Begin entering new radiation levels. Type 'done' to finish.")

    while True:
        level = input("Enter radiation level or 'done' to finish: ").lower()
        if level == 'done':
            break

        try:
            measurements.append(int(level))
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")

    return measurements


# This function will add the new area and its observation to the database
def add_observation(radiation_data, location, observation):
    radiation_data[location] = observation


# Asking The users (doctors) to start the program 
print('\nWelcome to the program. Please choose between the options below or "done" to exit:')
print('\nOption 1: See the average radiation for a specific location.')
print('\nOption 2: Add a new observation for a new location.')

while True:
    user_input = input('\nPlease enter "one" or "two" to proceed: ').lower()

    if user_input == 'one':
        print('\nThis is the list of different areas where average radiations are available:')
        display_areas(radiation_data)
        user_choice = input('\nPlease enter the area that you want to see its average radiation: ').capitalize()
        if user_choice in radiation_data.keys():
            print(f'\nThe average radiation for {user_choice} is {calculate_average(radiation_data[user_choice]):.2f}')
        else:
            print('Please make sure you are picking the area from the provided list.')

    elif user_input == 'two':
        new_location = get_location()
        new_observation = get_observation()
        add_observation(radiation_data, new_location, new_observation)
        print(f'\nObservation added for {new_location}: {new_observation}')
        print('\nUpdated list of areas with observations:')
        display_areas(radiation_data)
        user_choice = input('Please enter the area that you want to see its average radiation: ').capitalize()
        if user_choice in radiation_data.keys():
            print(f'\nThe average radiation for {user_choice} is {calculate_average(radiation_data[user_choice]):.2f}')
        else:
            print('Please make sure you are picking the area from the provided list.')

    elif user_input == 'done':
        break

    else: 
        print('Please enter "one", "two", or "done" to continue.')
