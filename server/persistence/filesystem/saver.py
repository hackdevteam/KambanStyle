import pickle
from os import makedirs
from os.path import exists, join

COLUMN_PROPERTIES_FILE = ".properties"


def save_column(working_directory, column):
	column_directory = join(working_directory, str(column.id))
	column_properties_file = join(column_directory, COLUMN_PROPERTIES_FILE)
	create_directory(column_directory)
	serialize_object(column, column_properties_file)


def create_directory(column_directory):
	if not exists(column_directory):
		makedirs(column_directory)


def serialize_object(object_to_save, destination_path):
	property_file = open(destination_path, "w+")
	pickle.dump(object_to_save, property_file)
	property_file.close()