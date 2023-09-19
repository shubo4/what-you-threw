from garb_classifier.constants import *
from garb_classifier.utils.common import read_yaml,create_directories
from garb_classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file = CONFIG_FILE_PATH, params_file = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    