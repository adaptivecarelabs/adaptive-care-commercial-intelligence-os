class Settings:
    APP_NAME = "CIOS API"
    VERSION = "1.0.0"
    DESCRIPTION = "Adaptive Care Technology Ltd - Commercial Intelligence Operating System API"

    DATABASE_URL = (
        "postgresql+psycopg://localhost/cios"
    )

    REDIS_URL = "redis://localhost:6379/0"
    S3_ENDPOINT = "http://localhost:9000"
    S3_ACCESS_KEY = "minioadmin"
    S3_SECRET_KEY = "minioadmin"
    S3_BUCKET = "cios-raw"
    S3_REGION = "us-east-1"


settings = Settings()
