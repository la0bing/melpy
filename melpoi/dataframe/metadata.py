from dataclasses import asdict, dataclass
from typing import Dict, List


@dataclass
class BaseDataType:
    name: str


@dataclass
class StringDataType(BaseDataType):
    name: str = "string"


@dataclass
class FloatDataType(BaseDataType):
    name: str = "float"


@dataclass
class IntegerDataType(BaseDataType):
    name: str = "integer"


@dataclass
class DatetimeDataType(BaseDataType):
    name: str = "datetime"


@dataclass
class Column:
    name: str
    dtype: BaseDataType = None
    distinct_count: int = 0
    na_count: int = 0
    na_percentage: float = 0
    remarks: List[str] = ""

    def unpack(self):
        return asdict(self)


@dataclass
class DataFrameInfo:
    columns: Dict[str, Column] = None
    max_na_count_per_row: int = 0
    max_na_percentage_per_row: float = 0
    max_na_count_ids: List[int] = None
