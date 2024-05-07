import json
from dataclasses import fields
from enum import Enum, auto
from typing import List, Union

from src.data_model import PipelineDataModel


class OutputAndPublishing:

    class OutputType(Enum):
        CSV = auto()
        JSON = auto()
        STREAM = auto()

    class Destination(Enum):
        CONSOLE = auto()
        FILE = auto()
        HTTP = auto()
        TCP = auto()

    class FormatProducer:
        @staticmethod
        def csv_producer(data_modeled: List[PipelineDataModel]) -> str:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def stream_producer(data_modeled: List[PipelineDataModel]) -> bytes:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def json_producer(data_modeled: List[PipelineDataModel]) -> str:
            attribs = fields(PipelineDataModel)
            dict = [{attr.name: getattr(m, attr.name) for attr in attribs} for m in data_modeled]
            return json.dumps(dict, indent=4)

    class SendToDestination:
        @staticmethod
        def console(data: str):
            print(data)

        @staticmethod
        def file(data: Union[str, bytes]):
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def http(data: Union[str, bytes]):
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def tcp(data: Union[str, bytes]):
            raise NotImplemented(f"{__name__} not implemented!")

    format_producers = {
        OutputType.JSON: FormatProducer.json_producer,
        OutputType.CSV: FormatProducer.csv_producer,
        OutputType.STREAM: FormatProducer.stream_producer
    }

    destinations = {
        Destination.TCP: SendToDestination.tcp,
        Destination.FILE: SendToDestination.file,
        Destination.HTTP: SendToDestination.http,
        Destination.CONSOLE: SendToDestination.console
    }

    def __call__(self, output_type: OutputType, destination_type: Destination):
        def _output_and_publishing(data_modeled: List[PipelineDataModel]) -> None:
            format_producer_func = self.format_producers[output_type]
            data = format_producer_func(data_modeled)
            send_to_func = self.destinations[destination_type]
            send_to_func(data)

        return _output_and_publishing
