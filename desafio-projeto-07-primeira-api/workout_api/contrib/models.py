from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)


# TEORIA

# A Declarative Base do SQLAlchemy serve como uma classe base a partir da qual
# todas as classes de mapeamento de tabelas são derivadas. Ela combina as
# capacidades de mapeamento de objetos do SQLAlchemy com a definição de
# esquemas de tabelas, proporcionando uma maneira mais intuitiva e coesa de
# definir modelos de banco de dados.

# Essa será a classe pai das outras de mesmo tipo.
# https://docs.sqlalchemy.org/en/20/orm/declarative_styles.html#orm-declarative-generated-base-class