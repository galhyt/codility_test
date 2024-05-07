from typing import List, Callable, Tuple

from src.data_model import PipelineDataModel


class Filtering:
    """
    rules: list of tuples
        [allow/deny (True/False), func represents filter on the model]
    description:
        if filter func return True then allow/deny operation applied on model
    """

    rules: List[Tuple[bool, Callable[[PipelineDataModel], bool]]] = [
        (True, lambda m: m.src_subnet_group_a == "10.0.0.0"),
        (True, lambda m: m.dst_subnet_group_a == "10.0.0.0"),
        (True, lambda m: m.protocol in [1, 17] and m.srcport == 123),
        (False, lambda m: m.dstport == 443),
        (False, lambda m: m.dstport == 80),
    ]

    def __call__(self, data_modeled: List[PipelineDataModel]):
        for i in range(len(data_modeled) - 1, -1, -1):
            m = data_modeled[i]
            for allow, filter_func in self.rules:
                if filter_func(m):
                    if not allow:
                        data_modeled.pop(i)
                    break

        return data_modeled