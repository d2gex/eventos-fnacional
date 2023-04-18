from typing import List, Dict, Any, Optional
from src.db import models
from src.db import utils as utils_db
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class ApiDB:
    @classmethod
    def get_table(cls, model: Any) -> List[Dict]:
        with utils_db.session_scope() as dbs:
            db_data = dbs.query(model).all()
            data = [x.to_dict() for x in db_data]
        return data

    @classmethod
    def get_toreros(cls) -> List[Dict]:
        with utils_db.session_scope() as dbs:
            db_data = dbs.query(
                models.ModelTorero.nombre_profesional, models.ModelTorero.id
            ).all()
            data = [{"nombre_profesional": row[0], "id": row[1]} for row in db_data]
        return data

    @classmethod
    def save_torero_details(cls, data: Dict) -> Optional[Dict]:
        try:
            for torero_details in data["toreroRow"]:
                torero_details[
                    "nombre_profesional"
                ] = f"{torero_details['nombre']} {torero_details['apellidos']} {torero_details['apodo']}".strip()
                with utils_db.session_scope() as s_db:
                    s_db.add(models.ModelTorero(**torero_details))
        except IntegrityError:
            result = torero_details
        else:
            result = None
        return result

    @classmethod
    def save_ganaderia_details(cls, data: Dict) -> Optional[Dict]:
        try:
            for ganaderia_details in data["ganaderiaRow"]:
                with utils_db.session_scope() as s_db:
                    s_db.add(models.ModelGanaderia(**ganaderia_details))
        except IntegrityError:
            result = ganaderia_details
        else:
            result = None
        return result

    @classmethod
    def save_festejo(cls, data: Dict, db_session: Any):
        data["fecha"] = datetime.strptime(data["fecha"], "%d/%m/%Y").date()
        db_session.add(models.ModelFestejo(**data))

    @classmethod
    def save_ganaderia_festejo(cls, data: List[Dict], festejo_id: str, db_session: Any):
        db_data = [
            models.ModelGanaderiaFestejo(
                ganaderia_id=ganaderia_details["ganaderiaName"]["id"],
                festejo_id=festejo_id,
            )
            for ganaderia_details in data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_torero_premios_by_festejos(
        cls, data: List[Dict], festejo_id: str, db_session: Any
    ):
        toreros_premios_data = []
        for row in data:
            torero_details = row["toreroName"]
            torero_premios = row["toreroPremios"]
            for premio_instance in torero_premios:
                toreros_premios_data.append(
                    {
                        "festejo_id": festejo_id,
                        "torero_id": torero_details["id"],
                        "tipo_premio_id": premio_instance,
                    }
                )
        db_data = [
            models.ModelToreroPremioFestejo(**premio_row)
            for premio_row in toreros_premios_data
        ]
        db_session.add_all(db_data)

    @classmethod
    def save_festejos(cls, data: Dict):
        data["festejos"].pop("provincia_id")
        festejo_id = data["festejos"]["tipo_festejo_id"]
        with utils_db.session_scope() as s_db:
            cls.save_festejo(data["festejos"], s_db)
            cls.save_ganaderia_festejo(data["ganaderiaRow"], festejo_id, s_db)
            cls.save_torero_premios_by_festejos(data["toreroRow"], festejo_id, s_db)


"""
{
  "festejos": {
    "tipoFestejo": 2,
    "nombreFestejo": "Nombre festejo",
    "poblacion": 1,
    "provincia": 45,
    "celebracion": "18/04/2023"
  },
  "ganaderiaRow": [
    {
      "ganaderiaName": {
        "id": 1,
        "nombre_ganaderia": "Ganaderia_0",
        "provincia_id": 45
      }
    },
    {
      "ganaderiaName": {
        "id": 3,
        "nombre_ganaderia": "Ganaderia_2",
        "provincia_id": 45
      }
    }
  ],
  "toreroRow": [
    {
      "toreroName": {
        "id": 1,
        "nombre_profesional": "aaron abad aaad"
      },
      "toreroPremios": [
        1,
        3
      ]
    },
    {
      "toreroName": {
        "id": 4,
        "nombre_profesional": "abby abbott abtt"
      },
      "toreroPremios": [
        4,
        3
      ]
    }
  ]
}
"""