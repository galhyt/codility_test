from functools import reduce
from typing import List, Callable

from src.Input_and_parsing import InputAndParsing
from src.enrichment import Enrichment
from src.filtering import Filtering
from src.output_and_publishing import OutputAndPublishing


def pipeline_digest_creator(steps: List[Callable]):
    return reduce(lambda s1, s2: lambda *args, **kwargs: s2(s1(*args, **kwargs)), steps)


if __name__ == '__main__':
    # digest_pipeline = pipeline_digest_creator([InputAndParsing(), Enrichment(), Filtering(), OutputAndPublishing()])
    digest_pipeline = pipeline_digest_creator([
        InputAndParsing(), Enrichment(), Filtering(), OutputAndPublishing()(OutputAndPublishing.OutputType.JSON, OutputAndPublishing.Destination.CONSOLE)
    ])
    digest_pipeline("../sample_data.json", InputAndParsing.InputType.JSON)
