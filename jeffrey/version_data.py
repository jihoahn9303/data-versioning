from jeffrey.config_schemas.config_schema import Config
from jeffrey.utils.config_utils import get_config
from jeffrey.utils.data_utils import (
    initialize_dvc, 
    initialize_dvc_storage,
    update_data_version
)


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    initialize_dvc()
    initialize_dvc_storage(
        dvc_remote_name=config.dvc_remote_name,
        dvc_remote_url=config.dvc_remote_url
    )
    update_data_version(
        dvc_raw_data_folder=config.dvc_raw_data_folder,
        dvc_remote_name=config.dvc_remote_name
    )

if __name__ == "__main__":
    version_data() 