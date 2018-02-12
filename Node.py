class Node:
    def __init__(self,node_id,name):

        """

        :param node_id:
        :param name:
        """
        self.__node_id = node_id
        self.__name=name

    def get_name(self):

        """

        :return:
        """
        return self.__name

    def __str__(self):
        """

        :return:
        """
        return self.__name

    def __repr__(self):

        """

        :return:
        """
        return self.__node_id