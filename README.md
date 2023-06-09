# Проект автоматизации тестирования API для [reqres.in](https://reqres.in/)
Проект api автотестов для сайта reqres.in

<a name="оглавление"></a>
# Оглавление
1. [Технологии](#технологии)
2. [Описание проекта](#описание)
3. [Запуск тестов в Jenkins](#запуск_дженкинс)
4. [Результат прохождения тестов в Allure report](#report)
5. [Результаты тестов в телеграм](#телеграм)
6. [Allure TestOps](#проект)
    1. [Проект](#проект)
    2. [Dashboard](#дашборд)

<a name="технологии"></a>
# Использованны следующие технологии:
<p align="center">
<img width="16%" title="pytest" src="media/pytest.png">
<img width="16%" title="python" src="media/python.png">
<img width="16%" title="requests" src="media/requests.png">
<img width="16%" title="pycharm" src="media/pycharm.png">
<img width="16%" title="Allure Report" src="media/allure.svg">
<img width="16%" title="GitHub" src="media/github.svg">
<img width="16%" title="Jenkins" src="media/jenkins.svg">
<img width="15%" title="Allure TestOps" src="media/allure testops.svg">
</p>

[К оглавлению ⬆](#оглавление)
<a name="описание"></a>
# Описание проекта
Автоматизирована проверка регистрации, создания, изменения, удаления и получения данных пользователя.

Используются: 
- авторизация по токену, полученному из запроса авторизации
- модели, 
- проверки(assert),
- allure steps


<a name="запуск_дженкинс"></a>
# Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/reqres_api/) выглядит следующим образом
Главная страница сборки
![](media/jenkins_api.png)
[К оглавлению ⬆](#оглавление)

<a name="report"></a>
# [Отчет](https://jenkins.autotests.cloud/job/reqres_api/allure/) о выполнении тестов
![](media/allurereport_api.png)

Каждый тест, независимо от результата, состоит из:
- шагов, 
- лога запроса,
- лога ответа. 

![](media/allreport_api.png)

Окно с графиками
![](media/graphsreport_api.png)

[К оглавлению ⬆](#оглавление)
<a name="телеграм"></a>
# По результатам работы тестов отправляется краткий отчет в Telegram
![](media/telegrambot.png)

[К оглавлению ⬆](#оглавление)
<a name="проект"></a>
# Создан проект в [Allure TestOps](https://allure.autotests.cloud/project/2071/test-cases?treeId=0)
![](media/testops_api.png)

[К оглавлению ⬆](#оглавление)


<a name="дашборд"></a>
# Настроен [Dashboard](https://allure.autotests.cloud/project/2071/dashboards) с разными показателями
![](media/testops_api2.png)

[К оглавлению ⬆](#оглавление)
