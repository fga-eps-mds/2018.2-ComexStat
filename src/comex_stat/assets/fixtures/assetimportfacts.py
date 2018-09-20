from class_fixtures.models import Fixture
from comex_stat.assets.models import AssetImportFacts

assets = Fixture(AssetImportFacts)
assets.add(name="Teste")
