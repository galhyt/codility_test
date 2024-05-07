import parser
import re
from typing import List

from src.data_model import PipelineDataModel


class Enrichment:

    def __call__(self, data_modeled: List[PipelineDataModel]):
        r = re.compile(r'^(?P<a>\d+)\.(?P<b>\d+)\.(?P<c>\d+)\.\d+$')

        for m in data_modeled:
            src_match = re.search(r, m.srcip)
            attr = src_match.groupdict()
            m.src_subnet_group_a, m.src_subnet_group_b, m.src_subnet_group_c =\
                f"{attr['a']}.0.0.0", f"{attr['a']}.{attr['b']}.0.0", f"{attr['a']}.{attr['b']}.{attr['c']}.0"

            dst_match = re.search(r, m.dstip)
            attr = dst_match.groupdict()
            m.dst_subnet_group_a, m.dst_subnet_group_b, m.dst_subnet_group_c =\
                f"{attr['a']}.0.0.0", f"{attr['a']}.{attr['b']}.0.0", f"{attr['a']}.{attr['b']}.{attr['c']}.0"

        return data_modeled
