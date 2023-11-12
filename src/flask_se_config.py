# -*- coding: utf-8 -*-

import os
import sys
import re
import pathlib
from datetime import datetime

type_id_string = [
    "",
    "Bachelor_Report",
    "Bachelor_Thesis",
    "Master_Thesis",
    "Autumn_practice_2nd_year",
    "Spring_practice_2nd_year",
    "Autumn_practice_3rd_year",
    "Spring_practice_3rd_year",
    "Production_practice",
    "Pre_graduate_practice",
]

PY2 = sys.version_info[0] == 2
if PY2:
    text_type = unicode
else:
    text_type = str

_windows_device_files = (
    "CON",
    "AUX",
    "COM1",
    "COM2",
    "COM3",
    "COM4",
    "LPT1",
    "LPT2",
    "LPT3",
    "PRN",
    "NUL",
)

_filename_strip_re = re.compile(r"[^A-Za-zа-яА-ЯёЁ0-9_.-]")


def secure_filename(filename: str) -> str:
    if isinstance(filename, text_type):
        from unicodedata import normalize

        filename = normalize("NFKD", filename)

    for sep in os.path.sep, os.path.altsep:
        if sep:
            filename = filename.replace(sep, " ")

    filename = str(_filename_strip_re.sub("", "_".join(filename.split()))).strip("._")

    if (
        os.name == "nt"
        and filename
        and filename.split(".")[0].upper() in _windows_device_files
    ):
        filename = "_{filename}"

    return filename


def get_hours_since(date):
    time_diff = datetime.utcnow() - date
    return int(time_diff.total_seconds() / 3600)


def plural_hours(n):
    hours = ["час", "часа", "часов"]
    days = ["день", "дня", "дней"]

    if n > 24:
        n = int(n / 24)
        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2

        return str(n) + " " + days[p]

    if n == 0:
        return "меньше часа"
    if n % 10 == 1 and n % 100 != 11:
        p = 0
    elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
        p = 1
    else:
        p = 2

    return str(n) + " " + hours[p]


def get_thesis_type_id_string(id):
    return type_id_string[id - 1]
