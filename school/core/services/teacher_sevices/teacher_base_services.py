from abc import ABC, abstractmethod


class TeacherBaseService(ABC):

    @abstractmethod
    def create(self):
        """ 
        Abstract method to create teacher.
        """
        pass

    @abstractmethod
    def update(self):
        """ 
        Abstract method to update teacher.
        """
        pass

    @abstractmethod
    def get(self):
        """ 
        Abstract method to get teacher.
        """
        pass

    @abstractmethod
    def delete(self):
        """ 
        Abstract method to delete teacher.
        """
        pass