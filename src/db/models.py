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


class ModelTipoEstado(ModelBase):
    __tablename__ = "tipo_estado"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_estado = Column(String, nullable=False, unique=True)
    torero_estado_festejo = relationship(
        "ModelToreroEstadoFestejo", back_populates="tipo_estado"
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

    tipo_torero_id = Column(Integer, ForeignKey("tipo_torero.id"), nullable=False)
    tipo_torero = relationship(ModelTipoTorero, back_populates="torero")


class ModelFestejo(ModelBase):
    __tablename__ = "festejo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_festejo = Column(String, nullable=False)
    fecha = Column(DateTime, nullable=False)
    notas = Column(Text)

    # M: 1 relationships
    poblacion_id = Column(Integer, ForeignKey("poblacion.id"))
    poblacion = relationship(ModelPoblacion)
    tipo_festejo_id = Column(Integer, ForeignKey("tipo_festejo.id"))
    tipo_festejo = relationship(ModelTipoFestejo, back_populates="festejo")

    # M:M relationships
    # torero_premio_festejo = relationship(
    #     "ModelToreroPremioFestejo"
    # )  # Parent to Association Object
    torero_festejo = relationship(
        "ModelToreroFestejo"
    )  # From parent to Association Object
    ganaderia_festejo = relationship(
        "ModelGanaderiaFestejo"
    )  # From parent to Association Object


class ModelToreroFestejo(ModelBase):  # M:M, Association object Pattern
    __tablename__ = "torero_festejo"

    # M:M
    torero_id = Column(
        Integer,
        ForeignKey("torero.id"),
        primary_key=True,
    )
    festejo_id = Column(
        Integer,
        ForeignKey("festejo.id"),
        primary_key=True,
    )


class ModelGanaderiaFestejo(ModelBase):  # M;M, Association object Pattern
    __tablename__ = "ganaderia_festejo"

    # M:M
    ganaderia_id = Column(
        Integer,
        ForeignKey("ganaderia.id"),
        primary_key=True,
    )
    festejo_id = Column(
        Integer,
        ForeignKey("festejo.id"),
        primary_key=True,
    )

    ganaderia = relationship(ModelGanaderia)


class ModelToreroPremioFestejo(ModelBase):  # M:M, Association object Pattern
    __tablename__ = "torero_premio_festejo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # primary keys from parent
    torero_id = Column(Integer, ForeignKey("torero_festejo.torero_id"), nullable=False)
    festejo_id = Column(
        Integer, ForeignKey("torero_festejo.festejo_id"), nullable=False
    )
    # primary keys from child
    tipo_premio_id = Column(Integer, ForeignKey("tipo_premio.id"), nullable=False)

    # relationship with child
    tipo_premio = relationship(ModelTipoPremio)


class ModelToreroEstadoFestejo(ModelBase):  # M:M, Association object Pattern
    __tablename__ = "torero_estado_festejo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # primary keys from parent
    torero_id = Column(Integer, ForeignKey("torero_festejo.torero_id"), nullable=False)
    festejo_id = Column(
        Integer, ForeignKey("torero_festejo.festejo_id"), nullable=False
    )
    # primary keys from child
    tipo_estado_id = Column(Integer, ForeignKey("tipo_estado.id"), nullable=False)

    # relationship with child
    tipo_estado = relationship(ModelTipoEstado)
