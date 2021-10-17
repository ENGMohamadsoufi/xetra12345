""" Runing Xetra ETl App """

import logging
import logging.config
import yaml


def main():
    """
    entry point to run xtra ETL project

    """
    # parsing yamal file
    config_path = 'D:/xetra_project/xetra12345/configs/xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))

    # configure loggin
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("this is a test.")


if __name__ == '__main__':
    main()
