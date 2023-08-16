from dataclasses import dataclass
from itemadapter import ItemAdapter

@dataclass
class TestItem:
    name: str
    price: float
    stock: int


obj = TestItem(name='test', price=1.0, stock=10)
adapter = ItemAdapter(obj)
print(adapter.item)