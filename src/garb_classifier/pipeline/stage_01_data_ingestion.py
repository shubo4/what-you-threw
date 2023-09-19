from garb_classifier.config.configuration import ConfigurationManager
from garb_classifier.components.data_ingestion import DataIngestion
from garb_classifier import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f'<<<<<<<<< {STAGE_NAME} started >>>>>>>>>')
        di = DataIngestionTrainingPipeline()
        di.main()
        logger.inof(f'<<<<<<<< {STAGE_NAME}completed >>>>>>>>>')
    except Exception as e:
        logger.exception(e)
        raise(e)
