# Создание автоматической аннотации в CVAT с использованием предобученной модели YOLOv5

### Пример скрипта для запуска кода:
python main.py --img_folder=image_folder

#### Опции для парсинга аргументоов в cli:
  --img_folder (TEXT)    &emsp;      Папка с изображениями (task из CVAT)</br>
  --weights (TEXT)     &emsp;         Путь к натренированным весам yolov5</br>
  --annotation_zip_file (TEXT) &emsp;  Имя zip архива аннотаций для CVAT формата YOLO</br>
  --conf (FLOAT)     &emsp;         Порог уверенности классификатора</br>
  --iou (FLOAT)        &emsp;         Порог iou на non max suppression</br>
  --help          &emsp;            Покажет существующие варианты парсинга аргументов</br>