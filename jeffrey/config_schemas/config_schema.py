from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    dvc_remote_name: str = "gs-remote-storage"
    dvc_remote_url: str = "gs://jeffrey-data-versioning/data/raw"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)