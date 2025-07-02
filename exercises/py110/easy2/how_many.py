def count_occurrences(cars):
    '''
    best way to do this is with a hashmap, cars as the key, number as the amount.
    loop through once to create the dictionary
    loop through again to print out the vehicle and its value


    '''
    my_map = {}
    for car in cars:
        if car in my_map:
            my_map[car] += 1
        else:
            my_map[car] = 1
        
    
    for key, value in my_map.items():
        print(f'{key} => {value}')


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)