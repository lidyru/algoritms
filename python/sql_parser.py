
from os import listdir, path

start_path = "/home/gnome/src/bdsp-backend/bdsp-db/novelty/"
sql_files = [path.join(start_path, file) for file in listdir(start_path) if path.isfile(path.join(start_path, file))]


def extract_params(file_path: str):
    """give file name and return dict with file name and list of params"""

    params = set()
    with open(file_path, "r") as script:
        for line in script:
            if " :" in line:
                # python street magic
                param = line.split(" :")[1].split(" ")[0].split(":")[0].split(";")[0].strip()

                if param:
                    params.add(f':{param}')

    return {file_path: list(params)}


def map_params():
    """give path to script and params to map, return script with mapped params"""

    # with open(file_path, "r") as script:
    #     for line in script:
    #         line.replace()


for sql_file in sql_files:
    print(extract_params(sql_file))
