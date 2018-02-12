import networkx as nx


G = nx.DiGraph()
class Road:
    def __init__(self,direction_type, direction, length, name):

        """

        :param direction_type: Unidirectinal or Bidirectional
        :param direction:
        :param length: length of the edge in our case
        :param name:
        """
        self._direction_type = direction_type
        self._direction = direction
        self._length = length
        self._name = name

    def __str__(self):

        """will return a human readable string

        :return: name of the road
        """
        return self._name