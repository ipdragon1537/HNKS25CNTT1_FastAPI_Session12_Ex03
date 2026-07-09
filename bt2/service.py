from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from model import ShipmentModel
from schema import ShipmentUpdate
def update_shipment_service(db:Session,id:int,shipment_update:ShipmentUpdate):
    update_ship = db.query(ShipmentModel).filter(ShipmentModel.id == id).first()
    if not update_ship:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Shipment with id {id} not found")
    for key,value in shipment_update.model_dump().items():
        setattr(update_ship,key,value)
    db.commit()
    db.refresh(update_ship)
    return update_ship
