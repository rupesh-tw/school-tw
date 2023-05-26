from abc import ABC, abstractmethod


class StudentBaseService(ABC):

    @abstractmethod
    def create(self):
        """ 
        Abstract method to create student.
        """
        pass

    @abstractmethod
    def update(self):
        """ 
        Abstract method to update student.
        """
        pass

    @abstractmethod
    def get(self):
        """ 
        Abstract method to get student.
        """
        pass

    @abstractmethod
    def delete(self):
        """ 
        Abstract method to delete student.
        """
        pass