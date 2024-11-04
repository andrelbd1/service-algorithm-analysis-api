from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config import ApplicationConfig
from src.exceptions import ParamInvalid
from src.internal_services.app_ulid import AppUlid

from .base import BaseModel
from .tb_form import Form
from .tb_question import Question

config_app = ApplicationConfig()


class Algorithm(BaseModel):
    __tablename__ = "algorithm"
    algorithm_id = Column(UUID(as_uuid=True), primary_key=True, default=AppUlid.ulid_to_uuid)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    source = Column(String(50))
    __table_args__ = (
        {"schema": config_app.DB_SCHEMA},
    )

    @property
    def __name(self):
        return self.name

    @__name.setter
    def __name(self, value):
        validate_param("name", value, "str")
        self.name = value

    @property
    def __description(self):
        return self.description

    @__description.setter
    def __description(self, value):
        self.description = value

    @property
    def __source(self):
        return self.source

    @__source.setter
    def __source(self, value):
        self.source = value

    def __set_params(self, params):
        self.__set_name(params.get("name"))
        self.__set_description(params.get("description"))
        self.__set_source(params.get("source"))

    def add(self, params):
        self.__enabled = True
        self.__set_params(params)

    def update(self, params):
        self.__set_params(params)

    def get(self):
        return {
            "algorithm_id": str(self.algorithm_id),
            "name": self.__name,
            "description": self.__description,
            "source": self.__source,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }