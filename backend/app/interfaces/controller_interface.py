from abc import ABC, abstractmethod
from flask import Response

class Controller_interface(ABC):

    @staticmethod
    @abstractmethod
    def get_all(request)-> tuple[Response, int]: pass

    @staticmethod
    @abstractmethod
    def show(id:int)-> tuple[Response, int]: pass

    @staticmethod
    @abstractmethod
    def create(request)-> tuple[Response, int]: pass          #preguntar al chat si es lo mismo request solo resquest:dic

    @staticmethod
    @abstractmethod
    def update(request:dict, id:int)-> tuple[Response, int]: pass

    @staticmethod
    @abstractmethod
    def destroy(id:int)-> tuple[Response, int]: pass


