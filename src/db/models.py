from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship


ModelBase = declarative_base()


class ModelTipoFestejo(ModelBase):
    __tablename__ = 'tipo_festejo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False, unique=True)
    festejo = relationship('ModelFestejo', backref="festejo")


class ModelTipoTorero(ModelBase):
    __tablename__ = 'tipo_torero'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_torero = Column(String, nullable=False, unique=True)
    torero = relationship('ModelTorero', backref="torero")


class ModelTipoPremio(ModelBase):
    __tablename__ = 'tipo_premio'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_premio = Column(String, nullable=False, unique=True)
    torero_premio_festejo = relationship('ModelTorero',
                                           secondary='torero_premio_festejo')


class ModelPoblacion(ModelBase):
    __tablename__ = 'poblacion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ciudad = Column(String, nullable=False, unique=True)
    provincia_id = Column(
        Integer,
        ForeignKey('provincia.id'))
    provincia = relationship('ModelProvincia')


class ModelProvincia(ModelBase):
    __tablename__ = 'provincia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    provincia = Column(String, nullable=False, unique=True)
    poblacion = relationship(ModelPoblacion, backref="poblacion")
    ganaderia = relationship('ModelGanaderia', backref="ganaderia")


class ModelGanaderia(ModelBase):
    __tablename__ = 'ganaderia'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ganaderia = Column(String, nullable=False, unique=True)
    provincia_id = Column(
        Integer,
        ForeignKey('provincia.id'))
    provincia = relationship('ModelProvincia')
    ganaderia_festejo = relationship('ModelFestejo',
                                       secondary="ganaderia_festejo")


class ModelTorero(ModelBase):
    __tablename__ = 'torero'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=True)
    apellidos = Column(String, nullable=True)
    nombre_profesional = Column(String, nullable=True, unique=True)

    tipo_torero_id = Column(Integer, ForeignKey('tipo_torero.id'))
    tipo_torero = relationship(ModelTipoTorero)

    torero_premio_festejo = relationship(ModelTipoPremio,
                                           secondary='torero_premio_festejo')


class ModelFestejo(ModelBase):
    __tablename__ = 'festejo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    celebracion = Column(DateTime, nullable=False)
    notas = Column(Text)

    # M: 1 relationships
    poblacion_id = Column(
        Integer,
        ForeignKey('poblacion.id'))
    poblacion = relationship(ModelPoblacion)
    tipo_festejo_id = Column(
        Integer,
        ForeignKey('tipo_festejo.id'))
    tipo_festejo = relationship(ModelTipoFestejo)

    # M:M relationships
    torero_premio_festejo = relationship(ModelTipoPremio,
                                            backref="torero_premio_festejo")
    ganaderia_festejo = relationship(ModelGanaderia,
                                       backref="ganaderia_festejo")


class ModelToreroPremioFestejo(ModelBase):
    __tablename__ = 'torero_premio_festejo'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M
    torero_id = Column(
        Integer,
        ForeignKey('torero.id'))
    festejo_id = Column(
        Integer,
        ForeignKey('festejo.id'))
    # M: 1
    tipo_premio_id = Column(
        Integer,
        ForeignKey('tipo_premio.id'))
    tipo_premio = relationship(ModelTipoPremio)


class ModelGanaderiaFestejo(ModelBase):
    __tablename__ = 'ganaderia_festejo'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # M:M
    ganaderia_id = Column(
        Integer,
        ForeignKey('ganaderia.id'))
    festejo_id = Column(
        Integer,
        ForeignKey('festejo.id'))
