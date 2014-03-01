from os.path import join
import pickle

COLUMN_PROPERTIES_FILE = ".properties"


def load_column(working_directory, column_id):
	column_properties_path = join(working_directory, str(column_id), COLUMN_PROPERTIES_FILE)
	properties_file = open(column_properties_path, "r")
	column = pickle.load(properties_file)
	properties_file.close()
	return column