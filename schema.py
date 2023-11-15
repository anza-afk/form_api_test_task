from pydantic import BaseModel


class RequestForm(BaseModel):
    """
    Модель для тела запроса с необязательными полями.
    """
    class Config:
        extra = "allow"
