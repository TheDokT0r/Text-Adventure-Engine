import os


class WorldLoader:
    PATH = None

    def __init__(self):
        selectPath()

        def selectPath(self):
            selectPath = input("Please enter the path to the world folder: ")
            if os.path.exists(selectPath):
                self.PATH = selectPath
                return True
            selectPath()
