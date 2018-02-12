from Server import Server
import networkx as nx
from tabulate import tabulate
import pandas as pd
from Display import Display

if __name__ == '__main__':
    server = Server()
    server.populateGraph()
    available_buildings = server.get_buildings_and_mail_codes()
    available_buildings.columns = ['Name', 'Mail codes']
    available_buildings.sort_values(by=['Name'], inplace=True)
    # Print out all available buildings (names and mail codes)
    print(tabulate(available_buildings, headers=['Name', 'Mail codes']), '\n')
    run_once = True
    while run_once:
        print('Please enter starting mail code:')
        source_mail_code = str(input())
        print('Please enter destination mail code:')
        destination_mail_code = str(input())
        mail_code_not_found = False
        try:
            # Make sure the input mail codes are in our list
            source_building = server.get_building_name_by_mail_code(source_mail_code)
            destination_building = server.get_building_name_by_mail_code(destination_mail_code)
            try:
                # Try to find shortest path
                path = server.find_distance(source_mail_code, destination_mail_code)
                path_name, path_direction = server.get_path(path)
                display = Display()
                display.format_and_print_output(source_building, destination_building, path_direction, path_name)
            except KeyError:
                print('No path available.')
                path_available = False
        except KeyError:
            print('Unrecognized Mail Code! Please try again.')
            run_once = True
        # Ask users to enter another navigation query, or quit
        print('Do you want another navigation?(Y/N):')
        yn = input()
        if yn == 'Y':
            run_once = True
        elif yn == 'N':
            run_once = False







































