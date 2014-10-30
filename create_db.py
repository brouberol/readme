from readme.db import engine
from readme.model import Recommendation

Recommendation.metadata.create_all(bind=engine)
