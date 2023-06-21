
import os
import shutil
import zipfile

import gdown
import click
import torch
import cv2

@click.command()
@click.option(
    "--split",
    help="A percentage of a split, e.g. 0.9 means split 0.9 for train and 0.1 for test",
    default=0.7,
    type=float,
)
@click.option(
    "--label_tfrms",
    help="Label union with another existed in dataset (example: 'head->hood,helmet->hat')",
    default=None,
    type=str,
)
@click.option(
    "--train_folder",
    default="obj_Train_data",
    help="Folder with Train subset inside cvat path (default obj_Train_data)",
    type=str,
)
@click.option(
    "--val_folder",
    default="obj_Validation_data",
    help="Folder with Val subset inside cvat path (default obj_Validation_data)",
    type=str,
)
@click.option(
    "--test_folder",
    default="obj_Test_data",
    help="Folder with Test subset inside cvat path (default obj_Test_data)",
    type=str,
)
@click.option("--img_format", default="png", help="Format of images", type=str)
@click.option(
    "--percentage_empty",
    default=10,
    help="Percentage of images without any labels in relation to full dataset size",
    type=float,
)
@click.option(
    "--classes",
    default="keep-all",
    help="Classes which labels to keep (e.g. 'A|C')",
    type=str,
)
def main(**kwargs):
    # ------------------ ARG parse ------------------
    CVAT_input_folder = kwargs["cvat"]
    mode = kwargs["mode"]
    output_folder = kwargs["output_folder"]
    split = kwargs["split"]
    train_folder = kwargs["train_folder"]
    val_folder = kwargs["val_folder"]



if __name__ == "__main__":
    main()