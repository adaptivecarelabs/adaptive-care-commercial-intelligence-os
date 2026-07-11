class Settings:
    APP_NAME = "CIOS API"
    VERSION = "1.0.0"
    DESCRIPTION = "Adaptive Care Technology Ltd - Commercial Intelligence Operating System API"

    DATABASE_URL = (
        "postgresql+psycopg://localhost/cios"
    )

    REDIS_URL = "redis://localhost:6379/0"


settings = Settings()
