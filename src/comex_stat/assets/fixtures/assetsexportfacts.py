from class_fixtures.models import Fixture
from comex_stat.assets.models import AssetExportFacts

assets = Fixture(AssetExportFacts)
assets.add(name="origin_fed_unit")
assets.add(name="destination_country")
