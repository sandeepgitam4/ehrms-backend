from database import engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)
print("Tables created successfully")
