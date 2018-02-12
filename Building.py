from Node import Node
class Building(Node):

    def __init__(self, id, name, address):

        """

        :param id:
        :param name:
        :param address:
        """
        super().__init__(id,name)
        self._address = address

    def __str__(self):

        """

        :return:
        """
        return super().__str__()