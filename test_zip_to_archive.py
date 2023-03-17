from zipfile import ZipFile, ZIP_DEFLATED
import os
import pandas as pd

csv_rows = len(pd.read_csv("examples/cities.csv"))



cities_size = os.path.getsize("examples/cities.csv")
sample_size = os.path.getsize("examples/sample.pdf")
sample3_size = os.path.getsize("examples/sample3.xlsx")


def test_check_files_in_archive():
    with ZipFile("resourses/myzip.zip", "w", compression=ZIP_DEFLATED, compresslevel=5) as myzip:
        myzip.write("examples/cities.csv", "cities.csv")
        cities_size_in_archive = myzip.getinfo("cities.csv").file_size
        cities = myzip.open("cities.csv")
        csv_rows_in_archive = 0
        for row in cities:
            csv_rows_in_archive += 1
        myzip.write("examples/sample.pdf", "sample.pdf")
        sample_size_in_archive = myzip.getinfo("sample.pdf").file_size
        myzip.write("examples/sample3.xlsx", "sample3.xlsx")
        sample3_size_in_archive = myzip.getinfo("sample3.xlsx").file_size
        assert myzip.testzip() is None


    assert cities_size == cities_size_in_archive, f"Размер файла в архиве не совпадает с тем, что был до архивирования"
    assert sample_size == sample_size_in_archive, f"Размер файла в архиве не совпадает с тем, что был до архивирования"
    assert sample3_size == sample3_size_in_archive, f"Размер файла в архиве не совпадает с тем, что был до архивирования"
    assert csv_rows == csv_rows_in_archive, f"Количество строк csv файла в архиве не совпадает с изначальным кол-вом"
