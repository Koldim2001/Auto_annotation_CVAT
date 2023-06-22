import os
import shutil
import zipfile

import gdown
import click
import torch
import cv2

def download_models(folder_name='models'):
    '''
    Функция для загрузки моделей обученных нейронных сетей в папку folder_name 
    из моего гугл диска
    '''
    output = folder_name + "/bag_belt_yolo.pt"

    if not os.path.exists(output):
        # Создание пустой папки 
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        print('Загружаю модель нейронной сети:')
        url = "https://drive.google.com/uc?id=1p2ErNFGtcN9Gly3ewy1UAz68wAKxSFW3"

        gdown.download(url, output, quiet=False)


def save_annotations_to_yolo_format(output_file, results, height_max, width_max):
    with open(output_file, 'w') as f:
        for result in results.xyxy[0]:
            label = result[-1]
            xmin, ymin, xmax, ymax = result[:4]

            # Получение координат центра объекта и его ширины и высоты
            width = xmax - xmin
            height = ymax - ymin
            x_center = xmin + width / 2
            y_center = ymin + height / 2

            # Запись аннотации в формате YOLO 1.1
            label = int(label)
            x_center_formatted = '{:.6f}'.format(x_center.item() / width_max)
            y_center_formatted = '{:.6f}'.format(y_center.item() / height_max)
            width_formatted = '{:.6f}'.format(width.item() / width_max)
            height_formatted = '{:.6f}'.format(height.item() / height_max)

            line = f"{label} {x_center_formatted} {y_center_formatted} {width_formatted} {height_formatted}\n"
            f.write(line)


def copy_files_to_folder(source_folder, destination_folder):
    # Создание пустой папки
    os.makedirs(destination_folder, exist_ok=True)

    # Копирование файлов в папку
    for file_name in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        shutil.copy2(source_file, destination_file)


def delete_folder(folder):
    # Удаление папки со всем содержимым
    shutil.rmtree(folder)


def create_zip_archive(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, folder_path))


@click.command()
@click.option(
    "--img_folder",
    default="images",
    help="Папка с изображениями (task из CVAT)",
    type=str,
)
@click.option(
    "--weights",
    default="models/bag_belt_yolo.pt",
    help="Путь к натренированным весам yolov5",
    type=str,
)
@click.option(
    "--annotation_zip_file",
    default="annotations.zip",
    help="Имя zip архива аннотаций для CVAT формата YOLO",
    type=str,
)
@click.option(
    "--conf",
    help="Порог уверенности классификатора (меньше боксов будет при увеличении значения)",
    default=0.20,
    type=float,
)
@click.option(
    "--iou",
    help="Порог iou на non max suppression (больше боксов будет при увеличении значения)",
    default=0.20,
    type=float,
)
def main(**kwargs):
    # ------------------ ARG parse ------------------
    conf = kwargs["conf"]
    iou = kwargs["iou"]
    zip_path = kwargs["annotation_zip_file"]
    weights_path = kwargs["weights"]
    image_folder = kwargs["img_folder"]
    output_folder = 'results/obj_train_data'
   
    # Загрузка с диска модели при выборе режима по умолчанию
    if weights_path == "models/bag_belt_yolo.pt":
        download_models()

    # Загрузка модели YOLOv5
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)
    # Установка порога по уверенности и подавления
    model.conf = conf  # Порог по уверенности
    model.iou = iou  # Порог подавления

    # Создание папки для сохранения аннотаций, если она не существует
    os.makedirs(output_folder, exist_ok=True)

    # Обработка изображений и сохранение аннотаций в формате YOLO 1.1
    for image_file in os.listdir(image_folder):
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height_max, width_max = image.shape[0], image.shape[1]

        # Инференс с использованием модели YOLOv5
        results = model(image)

        # Путь к файлу аннотации
        annotation_file = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}.txt")

        # Сохранение аннотаций в формате YOLO 1.1
        save_annotations_to_yolo_format(annotation_file, results, height_max, width_max)

    print(f"Аннотации сохранены")

    train_file = 'results/train.txt'  # Имя файла train.txt
    # Создание пустого файла train.txt, если он не существует
    if not os.path.exists(train_file):
        open(train_file, 'w').close()

    # Запись имен файлов в train.txt
    with open(train_file, 'w') as f:
        for image_file in os.listdir(image_folder):
            f.write('data/obj_train_data/' + image_file + '\n')

    # Добавим в папку 2 файла с конфигами модели (их стоит править если меняем классы модели)
    # Путь к папке, из которой нужно скопировать файлы
    source_folder = 'extra_data'
    # Путь к папке, в которую нужно скопировать файлы
    destination_folder = 'results'

    # Копирование файлов в папку
    copy_files_to_folder(source_folder, destination_folder)

    # Теперь архивируем итоговую аннотационную папку
    # Указать путь к папке для сохранения zip-архива
    zip_path = 'annotations.zip'

    create_zip_archive(destination_folder, zip_path)

    # Удаление папки вспомогательной (results) со всем содержимым
    delete_folder(destination_folder)


if __name__ == "__main__":
    main()