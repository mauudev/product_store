import json

from src.apps.products.domain.models import Product
from src.modules.shared.database import async_db_session


async def read_and_seed_json(file_path: str = "src/modules/shared/data.json"):
    with open(file_path, "r") as json_file:
        data_to_seed = json.load(json_file)
        async with async_db_session() as session:
            for data in data_to_seed:
                await Product.create(
                    session, data["product_name"], data["stock"], data["product_image"]
                )
