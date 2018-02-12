class Display:
    def format_and_print_output(self, source_building, destination_building, path_direction, path_name):
        """ Prints the complete output of a given string, from a starting point to an ending point on the node

        :rtype: object
        :param source_building: The prior building/node in our case
        :param destination_building: The posterior node
        :param path_direction: Gives path North South East West
        :param path_name: street name of the edge

        >>> d=Display()
        >>> d.format_and_print_output('Lincoln Hall','School of Information Sciences',['EW','SN','EW','SN','WE'],['Lincoln Hall_S. Wright St','S. Wright St','E. Chalmers St','S. 5th St','E. Daniel St'])
        Travel from Lincoln Hall to School of Information Sciences :
        Starting on Lincoln Hall , turn West
        At S. Wright St , turn North
        At E. Chalmers St , turn West
        At S. 5th St , turn North
        At E. Daniel St , turn East
        Proceed until you arrive at School of Information Sciences
        """
        direction={'S':'South','N':'North','E':'East','W':'West'}

        print("Travel from", source_building, "to", destination_building, ":")
        print("Starting on", source_building, ", turn", direction[path_direction[0][1]])
        for index in range(1, len(path_name)):
            if (path_name[index - 1] == path_name[index]) and (index is not 1):
                pass
            else:
                print("At", path_name[index], ", turn", direction[path_direction[index][1]])
        print("Proceed until you arrive at", destination_building)