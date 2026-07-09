from pydantic import BaseModel
class ShipmentUpdate(BaseModel):
    receive_name:str
    delivery_address:str