from abc import ABC, abstractmethod


class StudentBaseService(ABC):

    @abstractmethod
    def create_update(self):
        """ 
        Abstract method to create or Update student.
        """
        pass

    # @abstractmethod
    # def update(self):
    #     """ 
    #     Abstract method to update student.
    #     """
    #     pass