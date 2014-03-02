from os import makedirs
from os.path import exists
from pickle import dump, load


def create_directory(column_directory):
		if not exists(column_directory):
			makedirs(column_directory)


def serialize_object(object_to_save, destination_path):
		property_file = open(destination_path, "w+")
		dump(object_to_save, property_file)
		property_file.close()


def deserialize_object(object_path):
	properties_file = open(object_path, "r")
	loaded_object = load(properties_file)
	properties_file.close()
	return loaded_object
