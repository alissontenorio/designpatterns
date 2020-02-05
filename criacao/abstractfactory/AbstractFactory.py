import abc


class GameAbstractFactory(abc.ABC):

    """
    CLASSE ABSTRATA
    """
    @abc.abstractmethod
    def create_rpg_game(self):
        pass

    def create_action_game(self):
        pass
