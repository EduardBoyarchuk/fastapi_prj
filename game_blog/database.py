#Это функция-конструктор, которая используется
# для создания объекта подключения к базе данных
from sqlalchemy import create_engine
#Выполняем импорт функции, с помощью которой
# создается базовый класс для определения классов-моделей.
from sqlalchemy.ext.declarative import declarative_base
#Это функция-конструктор для создания класса-фабрики сессий.
from sqlalchemy.orm import sessionmaker


#Определяем путь до файла базы данных. Будем использовать файловую СУБД SQLite.
# Файл базы данных будет создаваться в корне проекта, т.е. в директории fastapi_prj.
SQLALCHEMY_DATABASE_URL = 'sqlite:///./site.db'
#Создаем объект подключения к базе данных.
#Особое внимание необходимо обратить на параметр:
#"check_same_thread": False
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)
#Создаем класс-фабрику сессий
# в привязке к объекту подключения (bind=engine).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=False)
#Создаем класс-фабрику для описания классов-моделей приложения.
# От этого класса будут наследоваться классы-модели приложения.
Base = declarative_base()