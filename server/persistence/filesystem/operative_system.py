from os import makedirs
from os.path import exists
from pickle import dump, load


def create_directory(new_directory):
	if not exists(new_directory):
		makedirs(new_directory)


def serialise_object(object_to_save, destination_path):
	property_file = open(destination_path, "w+")
	dump(object_to_save, property_file)
	property_file.close()


def deserialise_object(object_path):
	properties_file = open(object_path, "r")
	loaded_object = load(properties_file)
	properties_file.close()
	return loaded_object
