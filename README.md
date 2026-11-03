# P32. Alea-BFT: асинхронная репликация с византийскими отказами

**Проектное задание:** [Alea-BFT](https://distsys.ru/osukhoroslov/nis2/src/branch/main/project-tasks/p32-alea-bft.md)

**Участники:**

- Дегтярев Филипп
- Артем Коновалов
- Эйбатов Эмиль

## Сокращённый запуск
На данный момент возможна ручная установка:
Для начала в корне репозитория нужно скачать внешний репозиторий(содержащий alea-bft) с помощью: 

```bash
mkdir external && cd external

curl -fL https://codeload.github.com/diogoantunes25/AleaBFT/tar.gz/543786ef199a -o source.tar.gz

tar -xzf source.tar.gz && cd AleaBFT-543786ef199a
```

Далее нужно исправить ошибку сборки у скачанного проекта, подробнее описано в [01.md](nis/checkpoints/01.md)

После чего нужно перейти к корню репозитория и собрать проект и запустить тестовый прогон. Код для этих действий указан в [build.sh](src/build.sh) и в [simple.py](src/simple.py) соответственно, содержание описано в [01.md](nis/checkpoints/01.md)

И выполняется командами соответственно:
```bash
cd src && chmod +x build.sh && ./build.sh && python3 simple.py
```

## Навигация

- [Описание проекта](nis/project.md)
- [План эксперимента](nis/experiment-plan.md)
- [Контрольная точка 1](nis/checkpoints/01.md)
- [Контрольная точка 2](nis/checkpoints/02.md)
- [Контрольная точка 3](nis/checkpoints/03.md)
- [Состояние проекта](nis/status.md)
- [Результаты](nis/results.md)
- [Финальная версия](nis/final.md)
- Код: [путь]
- Тесты: [путь]
- Данные: [путь или описание внешнего хранилища]
