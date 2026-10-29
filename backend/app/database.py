import os

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Si existe DB_HOST significa que queremos utilizar PostgreSQL.
DB_HOST = os.getenv("DB_HOST")


if DB_HOST:
    DATABASE_URL = URL.create(
        drivername="postgresql+psycopg",
        username=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=DB_HOST,
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.environ["DB_NAME"],
    )
else:
    # Con esto podemos ejecutar pytest sin tener PostgreSQL levantado.
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./smartcampus.db",
    )


# SQLite necesita este parámetro para poder ser utilizado
engine_options = {}

if isinstance(DATABASE_URL, str) and DATABASE_URL.startswith("sqlite"):
    engine_options["connect_args"] = {
        "check_same_thread": False,
    }


# Motor de conexión de SQLAlchemy.
engine = create_engine(
    DATABASE_URL,
    **engine_options,
)


# Fábrica de sesiones utilizada por los endpoints.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Clase base de los modelos SQLAlchemy.
class Base(DeclarativeBase):
    pass


# Dependencia utilizada por FastAPI para obtener una sesión de bd.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()