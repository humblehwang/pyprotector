from converter.file_converter import file_converter_

def convert_file_to_py(filepath: str) -> None:
    """Convert the given file into .py file.
    """
    data = file_converter_.read_file(filepath)
    file_converter_.write_file(filepath, data)

def convert_dir_to_py(dirpath: str) -> None:
    """Convert the files which file extension is in SUPPORT_FILE_EXTENSION
     and also in given directory into .py files.
    """