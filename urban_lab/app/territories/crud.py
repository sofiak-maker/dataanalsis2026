from sqlalchemy.orm import Session
from geoalchemy2 import WKTElement
from app.territories import models, schemas

def get_territory(db: Session, territory_id: int):
    return db.query(models.Territory).filter(models.Territory.id == territory_id).first()
def list_territory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Territory).offset(skip).limit(limit).all()
def create_territory(db: Session, data: schemas.TerritoryCreate):
    geom = WKTElement(data.geom_wkt, srid=4326)
    db_territory = models.Territory(
        name=data.name,
        territory_type=data.territory_type,
        level=data.level,
        description=data.description,
        geom=geom
    )
    db.add(db_territory)
    db.commit()
    db.refresh(db_territory)
    return db_territory
def delete_territory(db: Session, territory_id: int):
    territory = db.query(models.Territory).filter(models.Territory.id == territory_id).first()
    if not territory:
        return False
    db.delete(territory)
    db.commit()
    return True
def update_territory(db: Session, territory_id: int, data: schemas.TerritoryUpdate):
    territory = db.query(models.Territory).filter(models.Territory.id == territory_id).first()
    if not territory:
        return None
    update_data = data.model_dump(exclude_unset=True)
    if "geom_wkt" in update_data:
        update_data["geom"] = WKTElement(update_data.pop("geom_wkt"), srid=4326)
    for field, value in update_data.items():
        setattr(territory, field, value)
    db.commit()
    db.refresh(territory)
    return get_territory(db, territory_id)
def create_metric(db: Session, territory_id: int, data: schemas.TerritoryMetricCreate):
    db_metric = models.TerritoryMetric(
        territory_id=territory_id,
        year=data.year,
        population=data.population,
        area_km2=data.area_km2,
        source=data.source
    )
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric
def list_metrics_by_territory(db: Session, territory_id: int):
    return db.query(models.TerritoryMetric).filter(
        models.TerritoryMetric.territory_id == territory_id
    ).order_by(models.TerritoryMetric.year).all()
def update_metric(db: Session, metric_id: int, data: schemas.TerritoryMetricUpdate):
    metric = db.query(models.TerritoryMetric).filter(models.TerritoryMetric.id == metric_id).first()
    if not metric:
        return None
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(metric, field, value)
    db.commit()
    db.refresh(metric)
    return metric
def delete_metric(db: Session, metric_id: int):
    metric = db.query(models.TerritoryMetric).filter(models.TerritoryMetric.id == metric_id).first()
    if not metric:
        return False
    db.delete(metric)
    db.commit()
    return True
def list_intersecting_territories(db: Session, wkt: str, skip: int = 0, limit: int = 100):
    search_geom = WKTElement(wkt, srid=4326)
    return db.query(models.Territory).filter(
        modeles.Territory.geom.ST_Intersects(search_geom)
    ).offset(skip).limit(limit).all()