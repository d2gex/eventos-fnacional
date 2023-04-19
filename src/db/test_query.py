from src.db import models as m, utils as utils_db
from sqlalchemy import and_

if __name__ == "__main__":
    with utils_db.session_scope() as db_session:
        db_data = (
            db_session.query(
                m.ModelFestejo.id,
                m.ModelFestejo.nombre_festejo,
                m.ModelFestejo.fecha,
                m.ModelFestejo.notas,
                m.ModelGanaderia.nombre_ganaderia,
                m.ModelPoblacion.ciudad,
                m.ModelTorero.nombre_profesional,
                m.ModelTipoTorero.tipo_torero,
                # m.ModelTipoPremio.tipo_premio,
            )
            # Get Ganaderias associated to festejos
            .join(
                m.ModelGanaderiaFestejo,
                m.ModelFestejo.id == m.ModelGanaderiaFestejo.festejo_id,
            )
            .join(
                m.ModelGanaderia,
                m.ModelGanaderiaFestejo.ganaderia_id == m.ModelGanaderia.id,
            )
            .join(m.ModelPoblacion, m.ModelFestejo.poblacion_id == m.ModelPoblacion.id)
            # Festejos with Toreros
            .join(
                m.ModelToreroFestejo,
                m.ModelFestejo.id == m.ModelToreroFestejo.festejo_id,
            )
            .join(m.ModelTorero, m.ModelToreroFestejo.torero_id == m.ModelTorero.id)
            .join(
                m.ModelTipoTorero, m.ModelTorero.tipo_torero_id == m.ModelTipoTorero.id
            )
            # Festejos y Toreros with Premios
            .join(
                m.ModelToreroPremioFestejo,
                and_(
                    m.ModelToreroFestejo.festejo_id
                    == m.ModelToreroPremioFestejo.festejo_id,
                    m.ModelToreroFestejo.torero_id == m.ModelToreroPremioFestejo.torero_id,
                ),
            )
            .join(m.ModelTipoPremio, m.ModelToreroPremioFestejo.tipo_premio_id == m.ModelTipoPremio.id)
            .all()
        )
    print(len(db_data))
    print(db_data)
