from class_fixtures.models import Fixture
from comex_stat.assets.models import AssetFacts

assets = Fixture(AssetFacts)
assets.add(name="date")
assets.add(name="name")
assets.add(name="port")
assets.add(name="port_code")
assets.add(name="transportation")
assets.add(name="registries")
assets.add(name="net_kilogram")
assets.add(name="fob_value")
