import os
import pickle
import shutil


def remove_data(data_path):
		if os.path.exists(data_path):
			shutil.rmtree(data_path)


def serialize_object(directory, object_file_name, object_to_serialise):
		os.makedirs(os.path.join(directory, object_to_serialise.get_id()))
		object_file = open(os.path.join(directory, object_file_name), "w+")
		pickle.dump(object_to_serialise, object_file)
		object_file.close()
