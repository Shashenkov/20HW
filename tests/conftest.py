from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


#Шаг 3. Создаем фикстуру с моком для DirectorDAO.
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Jora")
    d2 = Director(id=2, name="Gogi")
    d3 = Director(id=3, name="Barbara")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2])
    director_dao.create = MagicMock(return_value=d3)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


#Шаг 5. Создаем фикстуру с моком для GenreDAO.
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name="Комедия")
    g2 = Genre(id=2, name="Семейный")
    g3 = Genre(id=3, name="Драма")

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2])
    genre_dao.create = MagicMock(return_value=g3)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


#Шаг 7. Создаем фикстуру с моком для  MovieDAO.
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title="Фортитьюд", description="маленький шахтерский городок за Северным полярным кругом. Дикие пейзажи резко контрастируют с дружелюбной атмосферой, царящей в поселении.")
    m2 = Movie(id=2, title="Душа", description="Уже немолодой школьный учитель музыки Джо Гарднер всю жизнь мечтал выступать на сцене в составе джазового ансамбля. Однажды он успешно проходит прослушивание у легендарной саксофонистки и, возвращаясь домой вне себя от счастья, падает в люк и умирает. Теперь у Джо одна дорога — в Великое После, но он сбегает с идущего в вечность эскалатора и случайно попадает в Великое До. Тут новенькие души обретают себя, и у будущих людей зарождаются увлечения, мечты и интересы. Джо становится наставником упрямой души 22, которая уже много веков не может найти свою искру и отправиться на Землю.", trailer="https://www.youtube.com/watch?v=vsb8762mE6Q")
    m3 = Movie(id=3, title="Сияние", year=1980, rating=8.4)

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2])
    movie_dao.create = MagicMock(return_value=m3)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
