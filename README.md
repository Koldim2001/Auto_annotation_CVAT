# Создание автоматической аннотации в CVAT с использованием предобученной модели YOLOv5

### Пример скрипта для запуска кода:
python main.py --img_folder=image_folder

#### Опции для парсинга аргументоов в cli:
  --img_folder (TEXT)    &emsp;   &emsp;  &emsp;  &emsp;  &emsp;  Папка с изображениями (task из CVAT)</br>
  --weights (TEXT)     &emsp;   &emsp;   &emsp; &ensp;   &emsp;  &nbsp; &nbsp; &nbsp;  Путь к натренированным весам yolov5</br>
  --annotation_zip_file (TEXT) &emsp;   &emsp;  Имя zip архива аннотаций для CVAT формата YOLO</br>
  --conf (FLOAT)     &emsp;    &emsp;  &emsp;   &emsp;  &emsp;  &emsp; &ensp;  Порог уверенности классификатора</br>
  --iou (FLOAT)        &emsp;  &emsp;  &emsp;  &emsp;  &emsp;  &emsp;   &emsp;   Порог iou на non max suppression</br>
  --help   &emsp;  &emsp;  &emsp;   &emsp;  &emsp;  &emsp;    &emsp;    &emsp;   &emsp;  &nbsp;    Покажет существующие варианты парсинга аргументов</br>
