import os
import shutil


def remove_data(data_path):
		if os.path.exists(data_path):
			shutil.rmtree(data_path)
