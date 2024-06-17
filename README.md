# Дипломный проект профессии «Fullstack-разработчик на Python»

## Установка

Для успешной установки необходимо предварительно запустить и развернуть сервер Postgres с БД.

Скачать репозиторий фронтенда и бэкенда и скопировать файлы проекта в папку /app

В файле `.env`, который находится в репозитории бэкенда необходимо заполнить все поля:
Либо прописать данные значения в переменных окружения

- `REACT_APP_API_URL`
- `SECRET_KEY`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

В файле settings.py (бэкенд) в переменных CSRF_TRUSTED_ORIGINS  и CORS_ALLOWED_ORIGINS необходимо прописать ip-адрес фронта

В файлах adminSlice.js, authSlice.js, fileSlice.js фронтенд) необходимо заменить переменные со значением http://127.0.0.1:8000/ на http://ip-адрес-бэкенда:8000/

## Команды

### Для бэкенда

```bash

pip install -r requirements.txt
python manage.py makemigrations accounts
python manage.py makemigrations storage
python manage.py migrate
python manage.py runserver ip-адрес
```
### Фронтенда
```bash
yarn
yarn start
```

## Облачное хранилище «MyCloud»

### Цель проекта

Цель дипломного проекта - разработать веб-приложение, которое будет работать как облачное хранилище. Приложение позволит пользователям отображать, загружать, отправлять, скачивать и переименовывать файлы. 


Вам предстоит:

1. Создать комплексное веб-приложение, включающее в себя:
- бэкенд на языке Python с использованием фреймворка Django и СУБД PostgreSQL
- фронтенд на языках JavaScript, HTML, CSS с использованием библиотек React, Redux, React Router.
2. Развернуть созданное веб-приложение на платформе reg.ru.

В результате выполнения этого задания вы:

- получите опыт разработки комплексного приложения, включающего в себя бэкенд и фронтенд
- примените знания языка Python и фреймворка Django при разработке бэкенда
- примените знания языка JavaScript и библиотек React при разрабоке фронтенда
- получите опыт развёртывания приложения в облачной инфраструктуре reg.ru
- получите возможность использовать данный проект в своем портфолио разработчика.

------

### Чеклист готовности к работе над проектом

1. Освоены все модули профессии в объеме обязательных требований по сдаче ДЗ и курсовых работ.
2. Освоена самостоятельная установка и настройка инструментов, перечисленных в следующем разделе. Имеются навыки работы с ними, необходимые для проекта.
3. Техника и базовое ПО используемые при работе над проектом соответствуют требованиям необходимых инструментов.

Если все этапы чеклиста пройдены, то можете стартовать работу над проектом. Успехов в работе!


------

### Инструменты/ дополнительные материалы, которые пригодятся для выполнения задания

- [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) или [VS Code](https://code.visualstudio.com)
- [Python](https://www.python.org/)
- [Django](https://github.com/django/django)
- [NodeJS](https://nodejs.org/)
- [React](https://reactjs.org/)
- [WebPack](https://webpack.js.org/)
- [Git](https://git-scm.com/) + [Github](https://github.com/)
- [reg.ru](https://www.reg.ru/)

#### Рекомендации по использованию инструментов/ дополнительных материалов

- Для работы над различными частями проекта возможно использование единой IDE, например PyCharm или VS Code, а также текстовый редактор по вашему выбору.
- Также возможно использовать отдельные инструменты для разработки бэкенда и фронтенда, например, PyCharm для бэкенда и VS Code для фронтенда.
- В проекте рекомендуется использовать версии фреймворков и библиотек, актуальные на момент ведения разработки, например Python версии не ниже 3.10, Django не ниже 3.0, NodeJS не ниже 18.0, React не ниже 18.0, WebPack не ниже 5.0.
- Работа над проектом ведется с использованием системы контроля версий Git с опубликованием результатов в публичном репозитории(ях) автора на Github.com.
- Публиковаться в репозиторий должны не только окончательные версии файлов, но и промежуточные результаты с возможным тегированием стадий разработки.
- Возможно опубликование проекта как в едином монорепозитории содержащем код бэкенда и фронтенда, так и в двух отдельных репозиториях. Разбиение кода на большее количество репозиториев (например, с выделением библиотек и модулей) не рекомендуется, т.к. это существенно усложнит работу на стадиях разработки, развёртывания и проверки результатов.
- Допускается использование дополнительных инструментов и модулей, не перечисленных в данном задании, если это необходимо для реализации требуемой функциональности и существенно не усложняет ведение проекта и его дальнейшее развёртывание на открытых платформах.
- Не допускается использование библиотек и инструментов, требующих оплаты или заключения лицензионных договоров при своем использовании в открытых проектах такого масштаба.
- Не допускается использование в проекте дополнительных ресурсов, которые потребуют существенных трудовых и финансовых затрат на их организацию и развёртывание при проверке работоспособности проекта.

------

### Инструкция к работе над проектом

#### Пользовательский интерфейс (фронтенд)

Вам необходимо разработать приложение, состоящее из следующих основных блоков пользовательского интефейса:

*1. Основная страница приложения.*

Основная страница должна содержать:
- общую информацию для пользователя о приложении;
- кнопку или ссылку для перехода на форму регистрации пользователя с заданием минимальноо набора данных: логин, полное имя, e-mail, пароль. 

При этом должны проверяться основные ограничения на значения этих полей:
- [x] логин только из латинских букв и цифр, первая буква, длина от 4 до 20 символов
- [x] e-mail должен соответствовать формату для адресов электронной почты (для проверки можно использовать регулярные выражения)
- [x] пароль должен содержать не менее 6 символов, включающий как минимум одну заглавную букву, одну цифру и один специальный символ.

При несоответствии требованиям должны отображаться соответствующие информативные сообщения в форме с возможностью исправления и повторной отправки на сервер.

- кнопку или ссылку для перехода на форму аутентификации с вводом и проверкой логина на наличие в БД и правильности пароля. Результат неуспешной проверки должен отображаться в форме с возможностью повторной отправки на сервер. При успешной аутентификации должен осуществляться переход на страницу в зависимости от прав пользователя в системе.

*2. Административный интерфейс системы для настройки её параметров и управления пользователями и их файловыми хранилищами.*

Вход в эту часть приложения доступен только пользователям, имеющим признак «администратор» в списке пользователей:
- список пользователей с выводом признака «администратор» и информации, введённой пользователем в форме регистрации (кроме пароля). В списке должна быть возможность удаления пользователей и изменения значения признака «администратор»;
- в списке пользователей должна также отображаться информация об их файловых хранилищах - количество и размер файлов, ссылка для перехода к интерфейсу управления файлами в хранилище.

*3. Интерфейс управления файловым хранилищем.*

Вход в интерфейс доступен для любых пользователей. При этом администратор должен иметь право управления хранилищами любых пользователей, включая своё собственное. Обычные пользователи должны иметь доступ только к своему хранилищу:
- в интерфейсе должен отображаться список файлов, загруженных пользователем в хранилище, с основной информацией о них: имя файла, комментарий, размер, дата загрузки, дата последнего скачивания;
- для каждого файла должны быть доступны операции: удаление файла, переименование файла, просмотр файла (средствами браузера или через загрузку на локальный диск), копирование специальной ссылки на файл для предоставления доступа другим пользователям или использования его в качестве ресурса в веб-приложениях;
- должна быть реализована возможность загрузить новый файл в хранилище с указанием комментария.

Общие требования к интерфейсу приложения:

- должна быть максимально использована концепция SPA (single page application), т.е. весь переменный контент на странице (списки пользователей и файлов и т.п.) должен формироваться кодом на JavaScript с использованием библиотеки React. Для получения данных должны использоваться асинхронные api-вызовы к серверу приложения;
- все страницы приложения должны содержать навигационное меню, формируемое в зависимости от состояния аутентификации пользователя (кнопки «Вход», «Выход» и «Регистрация»)
- время, отводимое на дипломную работу, не предполагает существенных усилий по оформлению приложения с использованием графики, внешних библиотек элементов и т.п. Однако интерфейс приложения должен быть логичным и интуитивно понятным пользователю, имеющему опыт работы с аналогичными веб-приложениями.

#### Серверная часть приложения (бэкенд) должна соответствовать следующим требованиям:

1. Реализация на Python с использованием фреймворка Django и использованием для хранения информации СУБД Postgres.

1. Настройки приложения, такие как параметры подключения к БД, размещения файлового хранилища и т.п., должны быть выделены в коде в отдельный модуль.

1. Загрузка статических ресурсов, таких как HTML, CSS, JS файлов фронтенда, а также api-вызовы, должны обрабатываться единым сервером.

1. В проекте должны быть созданы все миграции, необходимые для инициализации БД в работоспособное состояние - создание БД, таблиц, пользователя admin с правами администратора.

1. Все API-вызовы должны соответствовать семантическим правилам для REST API, для обмена данными между фронтендом и бэкендом используется формат JSON.

1. Сервер должен содержать реализацию бэкенда для двух основных блоков приложения: административный интерфейс, работа с файловым хранилищем.

1. Административный интерфейс должен содержать следующие функции (конкретные api-вызовы вам необходимо спроектировать самостоятельно):

- [x] регистрация пользователя (с валидацией входных данных на соответствие требованиям, описанным выше)
- [x] получение списка пользователей
- [x] удаление пользователя
- [x] аутентификация пользователя
- [x] выход пользователя из системы (logout).

Общие комментарии к этому блоку:

- данные о пользователях должны храниться в таблице(ах) БД в полях, имеющих соответствующие им типы: логин, полное имя, e-mail, пароль, признак администратора, путь к хранилищу пользователя относительно общего пути к хранилищу файлов
- все вызовы кроме регистрации пользователя должны быть защищены проверкой на то, что пользователь аутентифицирован в системе
- функция удаления пользователей должна быть доступна только пользователю, имеющему признак администратора
- ошибки должны возвращаться из api в виде соответствующих статус-кодов, а также в формате JSON.

8. Блок работы с файловым хранилищем должен содержать следующие функции (конкретные api-вызовы вам необходимо спроектировать самостоятельно):

- получения списка файлов пользователя
- загрузка файла в хранилище
- удаление файла из хранилища
- переименование файла
- изменение комментария к файлу
- скачивание файла
- формирование специальной ссылки на файл для использования внешними пользователями
- скачивание файла через специальную ссылку, используемую внешними пользователями или веб-приложениями.

Общие комментарии к этому блоку:

- все функции работы с хранилищем должны проверять права доступа пользователя к хранилищу
- для администратора должна быть доступна работа с хранилищем любого пользователя (функция получения списка файлов должна принимать параметр с указанием хранилища, если пользователь администратор). 
- файлы должны сохраняться на диске сервера под уникальными именами в системе папок, не допускающей конфликты имен в случае, если разные пользователи загружают файлы с одинаковыми именами
- для каждого файла в БД должна сохраняться информация: оригинальное имя файла, размер, дата загрузки, последняя дата скачивания, комментарий, путь к файлу в хранилище, специальная ссылка, по которой файл может быть скачан внешним пользователем
- базовая папка для хранения файлов должна настраиваться как параметр системы
- специальная ссылка на файлы должна формироваться в максимально обезличенном виде, т.е. не содержать в себе имени пользователя, информации о хранилище пользователя, оригинальном имени файла
- при скачивании файла по такой ссылке он должен выгружаться сервером с указанием оригинального имени файла.

Общие требования к серверу:

- должно отслеживаться состояние аутентификации пользователя через сохранение информации о сессии
- все API-вызовы должны проверять права доступа пользователя и возвращать соответствующие ошибки через HTTP-статус и сообщение в формате JSON
- все события сервера должны логироваться путем вывода на консоль сообщений по типам DEBUG, INFO, WARNING, ERROR с указанием даты и времени, содержать информацию достаточную для анализа работоспособности и отладки сервера.

*Примечание*

Для лучшего понимания задачи рекомендуется ознакомиться с функционалом существующих аналогичных проектов, например, Google Drive, Yandex Drive, Dropbox и т.п. В связи с ограниченным временем отводимым на работу над проектом предполагается реализация только основных функций в упрощённом варианте.

------

### Правила сдачи работы

1. Опубликуйте все изменения в файлах проекта в публичном(ых) репозитории(ях) на github.com. Убедитесь, что репозитории содержат действительно последние версии со всеми изменениями.
2. Попробуйте самостоятельно полностью с нуля развернуть приложение, следуя инструкции, описанной вами в README.md. Убедитесь, что приложение разворачивается успешно и работоспособно, протестируйте основные функции.
3. Приложите в личном кабинете ссылки на репозиторий(ии) и развёрнутое приложение либо указание, что приложение может быть развёрнуто вами в течение не более 1 рабочего дня по запросу проверяющего.
4. Отправьте дипломную работу на проверку.
5. В случае возвращения работы на доработку и устранения замечаний выполните необходимые действия в короткий срок и повторно сдайте работу на проверку. В случае необходимости уточнения и каких-либо вопросов, связанных с результатом проверки, свяжитесь с руководителем вашей дипломной работы.

------

### Критерии оценки

1. Результаты работы должны быть сданы в виде ссылок на публичный(е) репозиторий(и) с кодом на github.com, а также на развёрнутое приложение на reg.ru.

2. В корневой папке репозиториев должны обязательно содержаться файлы README.md с детальным описанием структуры папок и файлов проекта, а также инструкции по его развёртыванию и запуску, достаточно подробные для выполнения специалистом, прошедшим обучение по профессии.

3. В случае использования дополнительных инструментов, которые не изучались в программе профессии, должны быть приложены ссылки на документацию по их установке и использованию.

4. В случае опубликования кода фронтенда и бэкенда в раздельных репозиториях общие инструкции по развёртыванию приложения должны быть описаны в README.MD в репозитории с бэкендом, в репозитории с фронтендом должны быть инструкции по сборке и подготовке артефактов фронтенда, которые необходимы для развёртывания.

5. Для минимизации затрат на использование ресурсов платформы reg.ru в период проверки работ допускается развёртывание приложения на reg.ru в момент, согласованный с руководителем диплома, при условии, что такое развёртывание было заранее отработано и не занимает продолжительное время.

6. В сданной работе должен быть реализован полностью и соответствовать требованиям функционал из разделов, помеченных как обязательные, и может быть частично или полностью реализован дополнительный функционал.

7. В связи с тем, что профессия Fullstack-разработчика предполагает владение всеми технологиями, используемыми при разработке комплексных приложений с пользовательским интерфейсом, оценке подлежит также внешний вид и удобство пользования приложением. Недостатки, ведущие к существенным трудностям в работе пользователя с приложением могут быть основанием для отправки работы на доработку и устранением замечаний. При этом дипломный руководитель будет исходить из того, что данное приложение не является коммерческим продуктом для конечного пользователя, его использование предполагается опытными ИТ-специалистами. Рекомендуется снабдить все элементы интерфейса приложения, которые могут вызвать сложности у такого пользователя, явными или всплывающими подсказками, а также описать в README.md.

8. при проверке развёрнутое приложение должно быть работоспособно в объеме реализованного обязательного функционала.

9. Развёртывание приложения должно быть повторяемо не разработчиком по инструкциям, содержащимся в README.md, без использования каких-либо инструментов или зависимостей, не описанных в README.md. В результате такого развёртывания должно получаться также работоспособное приложение в объеме обязательного функционала.
