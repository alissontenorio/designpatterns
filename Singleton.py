# Keep only one instance


class Singleton:
    __instance = None
    id = ''

    @staticmethod
    def get_instance():
        if Singleton.__instance is not None:
            return Singleton.__instance

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = super().__new__(cls)
            return Singleton.__instance
        else:
            raise Exception("Singleton class already instanciated!")