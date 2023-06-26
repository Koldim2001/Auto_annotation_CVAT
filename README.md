# Создание автоматической аннотации в CVAT с использованием предобученной модели YOLOv5
Необходимо передать путь к папке с изображениями, которые будут загружены в таску на CVAT. В результате работы программы будет сформирован zip архив с аннотациями, полученными на основе работы предобученной сети yolo.

 Все, что останется сделать: после создания таски навестись на панель Actions и выбрать Upload annotations. Далее выбрать в разделе Import format YOLO 1.1 и загрузить тот архив. 
 
 PS: В папке extra_data лежат вспомогательные файлы, которые используются в финальном файле аннотаций. Данные файлы необходимо менять исключительно при изменении числа или наименований классов модели. На текущий момент все настроено на следующие 6 классов: _person,
head,
torso,
face,
bag,
belt_.

### Installation:
```
git clone https://github.com/Koldim2001/Auto_annotation_CVAT.git
```
```
cd Auto_annotation_CVAT
```
```
pip install -e .
```
### Пример скрипта для запуска кода:
```
auto_annotate --img_folder=image_folder
```
#### Опции для парсинга аргументоов в cli:
  --img_folder (TEXT)    &emsp;   &emsp;  &emsp;  &emsp;  &emsp;  Папка с изображениями (task из CVAT)</br>
  --weights (TEXT)     &emsp;   &emsp;   &emsp; &ensp;   &emsp;  &nbsp; &nbsp; &nbsp;  Путь к натренированным весам yolov5</br>
  --annotation_zip_file (TEXT) &emsp;   &emsp;  Имя zip архива аннотаций для CVAT формата YOLO</br>
  --conf (FLOAT)     &emsp;    &emsp;  &emsp;   &emsp;  &emsp;  &emsp; &ensp;  Порог уверенности классификатора</br>
  --iou (FLOAT)        &emsp;  &emsp;  &emsp;  &emsp;  &emsp;  &emsp;   &emsp;   Порог iou на non max suppression</br>
  --help   &emsp;  &emsp;  &emsp;   &emsp;  &emsp;  &emsp;    &emsp;    &emsp;   &emsp;  &nbsp;    Покажет существующие варианты парсинга аргументов</br>
