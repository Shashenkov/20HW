import pytest

from service.movie import MovieService


# Шаг 8. Пишем класс с тестами для MovieService.
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.title == 'Фортитьюд'

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) == 2

    def test_create(self):
        genre_d = {'name': 'Name'}
        new_movies = self.movie_service.create(genre_d)
        assert new_movies.id is not None
        assert new_movies.title == 'Сияние'
        assert new_movies.year == 1980

    def test_update(self):
        self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None
