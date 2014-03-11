import os
import pickle


def create_directory(new_directory):
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)


def serialise_object(object_to_save, destination_path):
    property_file = open(destination_path, "w+")
    pickle.dump(object_to_save, property_file)
    property_file.close()


def deserialise_object(object_path):
    properties_file = open(object_path, "r")
    loaded_object = pickle.load(properties_file)
    properties_file.close()
    return loaded_object


def join_paths(path, *paths):
    return os.path.abspath(os.path.join(path, *paths))


def list_directories(path):
    for dir_name, directories, files in os.walk(path):
        return directories


def list_files(path):
    for dir_name, directories, files in os.walk(path):
        return files


def remove(file_name):
    os.remove(file_name)