from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class PipelineDataModel:
    srcip: Optional[str] = None
    dstip: Optional[str] = None
    srcport: Optional[int] = None
    dstport: Optional[int] = None
    protocol: Optional[int] = None
    numbytes: Optional[int] = None
    numpackets: Optional[int] = None

    # Enriched attributes
    src_subnet_group_a: Optional[str] = None
    src_subnet_group_b: Optional[str] = None
    src_subnet_group_c: Optional[str] = None
    dst_subnet_group_a: Optional[str] = None
    dst_subnet_group_b: Optional[str] = None
    dst_subnet_group_c: Optional[str] = None
    processing_timestamp: str = datetime.utcnow().isoformat()
