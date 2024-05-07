import json
from enum import Enum, auto
from socket import socket
from typing import Union, List

from src.data_model import PipelineDataModel


class InputAndParsing:

    class InputType(Enum):
        CSV = auto()
        JSON = auto()
        STREAM = auto()

    class Consumers:
        @staticmethod
        def csv_consumer(path: str) -> str:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def socket_consumer(_socket: socket) -> str:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def json_consumer(path: str) -> str:
            with open(path, 'r') as file:
                data = file.read()
            return data

    class Parsers:
        @staticmethod
        def csv_parser(data_txt: str) -> str:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def socket_parser(data_txt: str) -> str:
            raise NotImplemented(f"{__name__} not implemented!")

        @staticmethod
        def json_parser(data_txt: str) -> List[PipelineDataModel]:
            json_data = json.loads(data_txt)
            data_modeled: List[PipelineDataModel] = [
                PipelineDataModel(srcip=l.get("srcip"),
                                  dstip=l.get("dstip"),
                                  srcport=l.get("srcport"),
                                  dstport=l.get("dstport"),
                                  protocol=l.get("protocol"),
                                  numbytes=l.get("numbytes"),
                                  numpackets=l.get("numpackets")) for l in json_data
            ]
            return data_modeled

    consumers = {
        InputType.CSV: Consumers.csv_consumer,
        InputType.JSON: Consumers.json_consumer,
        InputType.STREAM: Consumers.socket_consumer
    }

    parsers = {
        InputType.CSV: Parsers.csv_parser,
        InputType.JSON: Parsers.json_parser,
        InputType.STREAM: Parsers.socket_parser
    }

    def __call__(self, input_src: Union[str, socket], input_type: InputType) -> List[PipelineDataModel]:
        """

        :param input_src: path of csv or json files or socket
        :param input_type: csv/json/socket
        :return: List[PipelineDataModel]
        """
        # consume data
        consumer_func = self.consumers[input_type]
        data = consumer_func(input_src)
        # parse data
        parser_func = self.parsers[input_type]
        data_modeled: List[PipelineDataModel] = parser_func(data)

        return data_modeled
