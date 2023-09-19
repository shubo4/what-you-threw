from garb_classifier import logger
from garb_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
  
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f'<<<<<<<<< {STAGE_NAME} started >>>>>>>>>')
    di = DataIngestionTrainingPipeline()
    di.main()
    logger.inof(f'<<<<<<<< {STAGE_NAME}completed >>>>>>>>>')
except Exception as e:
    logger.exception(e)
    raise(e)
