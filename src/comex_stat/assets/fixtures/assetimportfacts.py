from class_fixtures.models import Fixture
from comex_stat.assets.models import AssetImportFacts

assets = Fixture(AssetImportFacts)
assets.add(name="destination_fed_unit")
assets.add(name="origin_country")
