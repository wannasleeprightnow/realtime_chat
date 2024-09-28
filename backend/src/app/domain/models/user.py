from dataclasses import asdict, dataclass, field
from typing import Any
from uuid import UUID, uuid4


@dataclass
class User:
    name: str
    id: UUID = field(default_factory=uuid4)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
