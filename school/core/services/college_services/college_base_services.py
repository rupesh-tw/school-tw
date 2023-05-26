from abc import ABC, abstractmethod


class CollegeBaseService(ABC):

    @abstractmethod
    def create(self):
        """ 
        Abstract method to create college.
        """
        pass

    @abstractmethod
    def update(self):
        """ 
        Abstract method to update college.
        """
        pass

    @abstractmethod
    def get(self):
        """ 
        Abstract method to get college.
        """
        pass