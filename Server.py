import networkx as nx
import pandas as pd
from Building import Building
from Node import Node
from Road import Road
from tabulate import tabulate

class Server:

    def __init__(self):
        """
        This is a constructor to initialize private member variables
        """
        self.__building_by_mail_code = {}
        self.__node_by_id={}
        self.__G = nx.DiGraph()
        self.__data= pd.read_excel("Data_All.xlsx", sheetname=None, skiprows=[0], header=None)

    def get_node_by_id(self):
        """ Getter for private member variale __node_by_id
        """
        return self.__node_by_id

    def get_building_by_mail_code(self):
        """Getter for private variable __building_by_mail_code
        """
        return self.__building_by_mail_code

    def get_data(self):
        return self.__data

    def populate_building(self, single_row):
        """ From each row of an Excel sheet Building,it craetes object of Building and stores it in dictionary.
        Also populates the dictionary which maps mail codes with corresponding buildings
        Args:
        :param single_row: represents one row of the sheet building of an excel file
        """
        b = Building(single_row[0], single_row[1], single_row[2])
        self.__node_by_id[single_row[0]] = b
        self.populate_bulding_mail_code_from_list(single_row[0], single_row[3])


    def populate_intersection_node(self, single_row):
        """ From each row of an Excel sheet Intersection,it creates object of Node and stores it in dictionary.
        Args:
        :param single_row: represents one row of the sheet Intersection of an excel file
        """
        intersect = Node(single_row[0], single_row[1])
        self.__node_by_id[single_row[0]] = intersect


    def populate_edges(self, single_row):
        """ From each row of an Excel sheet Connection,it creates object of Road and
        Using existing nodes it creates the edges and hence the graph is generated
                Args:
                :param single_row: represents one row of the sheet Connection of an excel file
        """
        road = Road(single_row[2], single_row[3], single_row[4], single_row[5])
        self.__G.add_edge(self.__node_by_id[single_row[0]], self.__node_by_id[single_row[1]], link=road._length, name=road._name, direction = road._direction)
        if single_row[2] == 2:
            direction_op = single_row[3][1] + single_row[3][0]
            road_1 = Road(single_row[2], direction_op, single_row[4], single_row[5])
            self.__G.add_edge(self.__node_by_id[single_row[1]], self.__node_by_id[single_row[0]], link=road_1._length, name=road_1._name, direction = road_1._direction)

    def populate_bulding_mail_code_from_list(self, building_id, mail_codes):
        """Maps the mail code with building id

           :rtype: object
           :param building_id:
           :param mail_codes: """

        if type(mail_codes) == str: # If current cell contains more than one mail code, split them
            mail_code_list = mail_codes.strip().split(', ')
            for mail_code in mail_code_list:
                self.__building_by_mail_code[str(mail_code)] = building_id
        else:
            self.__building_by_mail_code[str(mail_codes)] = building_id

    def find_distance(self,postal_code_start,postal_code_end):

        """
        Finds the shortest distance between source and destination mail codes and lists the nodes on the shortest path
        :param postal_code_start: Source mail code
        :param postal_code_end: Destination mail code
        :return: list of Nodes
        >>> s=Server()
        >>> s.populateGraph()
        >>> s.find_distance('382','272')
        [B14, I37, I50, I41, I44, I70, I71, I51, I45, I43, B18]
        """
        return nx.shortest_path(self.__G, source  = self.__node_by_id[self.__building_by_mail_code[postal_code_start]], target  = self.__node_by_id[self.__building_by_mail_code[postal_code_end]], weight='link')

    def populateGraph(self):
        """ Reads the three sheets of an excel namely Building, Connection and Intersection and passses each rows of an excel to various functions
         and ultimately creates Graph
        """
        buildings = self.__data['Buildings']  # to populate building info
        for each in buildings.iterrows():
            self.populate_building(each[1])

        intersection = self.__data['Intersection']
        for each in intersection.iterrows():
            self.populate_intersection_node(each[1])

        connection = self.__data['Connection']
        for each in connection.iterrows():
            self.populate_edges(each[1])

    def get_path(self, node_list):

        """
        :param node_list: List of nodes forming the path from source to destination
        :return: all edges along with direction connecting input node list
        >>> s=Server()
        >>> s.populateGraph()
        >>> p=s.find_distance('382','272')
        >>> s.get_path(p)
        (['S. Wright St', 'S. Wright St', 'S. Wright St', 'S. Wright St', 'S. Wright St', 'W. Springfield Ave', 'S. Goodwin Ave', 'W. Green St', 'W. Green St'], ['EW', 'SN', 'SN', 'SN', 'SN', 'WE', 'NS', 'EW', 'EW'])
        """
        actual_path_name=[]
        actual_path_direction=[]
        for index in range(0, len(node_list)-2):
            actual_path_name.append(self.__G.edges[node_list[index], node_list[index + 1]]['name'])
            actual_path_direction.append(self.__G.edges[node_list[index], node_list[index + 1]]['direction'])
        return actual_path_name, actual_path_direction

    def get_building_name_by_mail_code(self, source_mail_code):

        """
        :param source_mail_code:
        :return: all edges along with direction connecting input node list
        >>> s=Server()
        >>> s.populateGraph()
        >>> s.get_building_name_by_mail_code('382')
        'Altgeld Hall'
        """
        return self.get_node_by_id()[self.get_building_by_mail_code()[source_mail_code]].get_name()

    def get_buildings_and_mail_codes(self):
        """
                :return: Building name and mail codes from excel sheet Building
                """
        return self.__data['Buildings'].drop([0, 2], axis=1)


