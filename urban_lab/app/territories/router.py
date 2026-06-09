from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.common.db import get_db
from app.territories import crud, schemas

router = APIRouter(prefix="/territories", tags=["territories"])
@router.get("/", response_model=list[schemas.TerritoryRead])
def list_territories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_territory(db, skip=skip, limit=limit)
@router.get("/{territory_id}", response_model=schemas.TerritoryRead)
def get_territory(territory_id: int, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return territory
@router.post("/", response_model=schemas.TerritoryRead, status_code=201)
def create_territory(data: schemas.TerritoryCreate, db: Session = Depends(get_db)):
    return crud.create_territory(db, data)
@router.put("/{territory_id}", response_model=schemas.TerritoryRead)
def update_territory(territory_id: int, data: schemas.TerritoryUpdate, db: Session = Depends(get_db)):
    territory = crud.update_territory(db, territory_id, data)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return territory
@router.delete("/{territory_id}", status_code=204)
def delete_territory(territory_id: int, db: Session = Depends(get_db)):
    if not crud.delete_territory(db, territory_id):
        raise HTTPException(status_code=404, detail="Territory not found")
    return
@router.get("/intersects", response_model=list[schemas.TerritoryRead])
def get_intersecting_territories(wkt: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_intersecting_territories(db, wkt, skip, limit)
@router.post("/{territory_id}/metrics", response_model=schemas.TerritoryMetricRead, status_code=201)
def create_metric(
    territory_id: int,
    data: schemas.TerritoryMetricCreate,
    db: Session = Depends(get_db)
):
   
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.create_metric(db, territory_id, data) 
@router.get("/{territory_id}/metrics", response_model=list[schemas.TerritoryMetricRead])
def list_metrics(
    territory_id: int,
    db: Session = Depends(get_db)
):
   
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.list_metric_by_territory(db, territory_id)
@router.put("/{territory_id}/metrics/{metric_id}", response_model=schemas.TerritoryMetricRead)
def update_metric(
    territory_id: int,
    metric_id: int,
    data: schemas.TerritoryMetricUpdate,
    db: Session = Depends(get_db)
):
    
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    
    metric = crud.update_metric(db, metric_id, data)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")
    return metric
@router.delete("/{territory_id}/metrics/{metric_id}", status_code=204)
def delete_metric(
    territory_id: int,
    metric_id: int,
    db: Session = Depends(get_db)
):
   
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    
    if not crud.delete_metric(db, metric_id):
        raise HTTPException(status_code=404, detail="Metric not found")
    return