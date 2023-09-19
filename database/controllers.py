import logging
from typing import List, Dict, Union
from sqlalchemy import update, delete
from database.models import Subscriber, TgBot
from database.database import session


class DataController:
    def __init__(self):
        self.model = Union[Subscriber, TgBot]

    @staticmethod
    def write(data: Union[Subscriber, TgBot]):
        session.add(data)
        session.commit()

    def read(self) -> List[Union[Subscriber, TgBot]]:
        return session.query(self.model).all()

    def update(self, id_: int, data: Dict):
        stmt = update(self.model).values(data).where(self.model.id == id_)
        try:
            session.execute(stmt)
            session.commit()
        except Exception as ex:
            session.rollback()
            logging.exception(f"Error:\n    {ex}\nAn error occurred during update data from model: {self.model}")

    def delete(self, id_: int):
        stmt = delete(self.model).where(self.model.id == id_)
        try:
            session.execute(stmt)
            session.commit()
        except Exception as ex:
            session.rollback()
            logging.exception(f"Error:\n    {ex}\nAn error occurred during delete data from model: {self.model}")
