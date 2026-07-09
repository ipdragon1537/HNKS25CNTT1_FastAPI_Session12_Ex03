from fastapi import FastAPI,Depends,status
from sqlalchemy.orm import Session
from database import engine,Base,get_db
from schema import ShipmentUpdate
from service import update_shipment_service
from model import ShipmentModel
Base.metadata.create_all(bind = engine)
app = FastAPI()
@app.put("/shipment/{shipment_id}",status_code=status.HTTP_200_OK)
def update_shipment(id:int,shipment_update:ShipmentUpdate,db:Session = Depends(get_db)):
    update_shop = update_shipment_service(db = db,id = id,shipment_update=shipment_update)
    return {
        "status":"success",
        "message":"Cập nhật đơn hàng thành công",
        "data":update_shop
    }
