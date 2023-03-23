import allure
from pytest_voluptuous import S
from schemas.reqres import single_user, register, create, update
from utils.helpers import authorization
from utils.sessions import reqres


def test_register_user():
    response = reqres().post('/api/register', cookies=authorization(), data={
        "email": "george.bluth@reqres.in",
        "password": "test123"
    })

    with allure.step('Код ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Id пользователя в ответе равен 1'):
        assert int(response.json()['id']) == 1
    with allure.step('Схема ответа верна'):
        assert S(register) == response.json()


def test_create_user():
    response = reqres().post('/api/users', cookies=authorization(), data={
        "name": "Max",
        "job": "tester"
    })

    with allure.step('Код ответа равен 201'):
        assert response.status_code == 201
    with allure.step('Имя в ответе равно Max'):
        assert str(response.json()['name']) == 'Max'
    with allure.step('Работа в ответе равна tester'):
        assert str(response.json()['job']) == 'tester'
    with allure.step('Схема ответа верна'):
        assert S(create) == response.json()


def test_update_user():
    response = reqres().put('/api/users/1', cookies=authorization(), data={
        "name": "Anton",
        "job": "project manager"
    })

    with allure.step('Код ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Имя в ответе равно Anton'):
        assert str(response.json()['name']) == 'Anton'
    with allure.step('Работа в ответе равна project manager'):
        assert str(response.json()['job']) == 'project manager'
    with allure.step('Схема ответа верна'):
        assert S(update) == response.json()


def test_update_part_of_user():
    response = reqres().patch('/api/users/1', cookies=authorization(), data={
        "name": "Ivan"
    })

    with allure.step('Код ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Имя в ответе равно Ivan'):
        assert str(response.json()['name']) == 'Ivan'
    with allure.step('Схема ответа верна'):
        assert S(update) == response.json()


def test_get_single_user():
    response = reqres().get('/api/users/1', cookies=authorization())
    with allure.step('Код ответа равен 200'):
        assert response.status_code == 200
    with allure.step('Схема ответа верна'):
        assert S(single_user) == response.json()


def test_delete_user():
    response = reqres().delete('/api/users/1', cookies=authorization())

    with allure.step('Код ответа равен 200'):
        assert response.status_code == 204
