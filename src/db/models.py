from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, inspect
from sqlalchemy.orm import relationship


SQLAlchemyModelBase = declarative_base()


class ModelBase(SQLAlchemyModelBase):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class ModelTipoFestejo(ModelBase):
    __tablename__ = "tipo_festejo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_festejo = Column(String, nullable=False, unique=True)
    festejo = relationship("ModelFestejo", back_populates="tipo_festejo")


class ModelTipoTorero(ModelBase):
    __tablename__ = "tipo_torero"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_torero = Column(String, nullable=False, unique=True)
    torero = relationship("ModelTorero", back_populates="tipo_torero")


class ModelTipoPremio(ModelBase):
    __tablename__ = "tipo_premio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_premio = Column(String, nullable=False, unique=True)
    torero_premio_festejo = relationship(
        "ModelToreroPremioFestejo", back_populates="tipo_premio"
    )


class ModelPoblacion(ModelBase):
    __tablename__ = "poblacion"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String, nullable=False, unique=True)
    provincia_id = Column(Integer, ForeignKey("provincia.id"))
    provincia = relationship("ModelProvincia", back_populates="poblacion")


class ModelProvincia(ModelBase):
    __tablename__ = "provincia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    provincia = Column(String, nullable=False, unique=True)
    poblacion = relationship(ModelPoblacion, back_populates="provincia")
    ganaderia = relationship("ModelGanaderia", back_populates="provincia")


class ModelGanaderia(ModelBase):
    __tablename__ = "ganaderia"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ganaderia = Column(String, nullable=False, unique=True)
    provincia_id = Column(Integer, ForeignKey("provincia.id"))
    provincia = relationship("ModelProvincia", back_populates="ganaderia")


class ModelTorero(ModelBase):
    __tablename__ = "torero"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    apodo = Column(String, nullable=True)
    nombre_profesional = Column(String, nullable=True, unique=True)

    tipo_torero_id = Column(Integer, ForeignKey("tipo_torero.id"))
    tipo_torero = relationship(ModelTipoTorero, back_populates="torero")


class ModelFestejo(ModelBase):
    __tablename__ = "festejo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    celebracion = Column(DateTime, nullable=False)
    notas = Column(Text)

    # M: 1 relationships
    poblacion_id = Column(Integer, ForeignKey("poblacion.id"))
    poblacion = relationship(ModelPoblacion)
    tipo_festejo_id = Column(Integer, ForeignKey("tipo_festejo.id"))
    tipo_festejo = relationship(ModelTipoFestejo, back_populates="festejo")

    # M:M relationships
    torero_premio_festejo = relationship(
        "ModelToreroPremioFestejo"
    )  # Parent to Association Object
    ganaderia_festejo = relationship(
        "ModelGanaderiaFestejo"
    )  # Parent to Association Object


class ModelToreroPremioFestejo(ModelBase):  # Association object Pattern
    """There is a M:M relationship between Festejo (Parent) and Torero (Child) and a 1:M relationship between
    TipoPremio and the table resulting from the M:M relationship (which is this class itself)
    """

    __tablename__ = "torero_premio_festejo"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M between festejo and torero
    torero_id = Column(Integer, ForeignKey("torero.id"))
    festejo_id = Column(Integer, ForeignKey("festejo.id"))
    torero = relationship(ModelTorero)  # Association object to child

    # M: 1 between TipoPremio and the above (M:M) relationship
    tipo_premio_id = Column(Integer, ForeignKey("tipo_premio.id"))
    tipo_premio = relationship(ModelTipoPremio, back_populates="torero_premio_festejo")


class ModelGanaderiaFestejo(ModelBase):  # Association object Pattern
    __tablename__ = "ganaderia_festejo"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M
    ganaderia_id = Column(Integer, ForeignKey("ganaderia.id"))
    festejo_id = Column(Integer, ForeignKey("festejo.id"))

    ganaderia = relationship(ModelGanaderia)
