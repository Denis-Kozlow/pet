from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_SQLITE_NAME: str
    SECRET_KEY: str
    REDIS_HOST: str
    RABBIT_HOST: str
    TTLCACHE: int
    GETRATEDOLLAR: str

    @property
    def DATABASE_URL_AIOSQLITE(self):
        return f"sqlite+aiosqlite:///database.db"

    @property
    def DATABASE_URL_ASYNCPG(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_PSYCOPG(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_SQLITE(self):
        return f"sqlite:///{self.DB_SQLITE_NAME}"

    @property
    def GETSECRET_KEY(self):
        return f"{self.SECRET_KEY}"

    @property
    def GETREDIS_HOST(self):
        return f"{self.REDIS_HOST}"

    @property
    def GETRABBIT_HOST(self):
        return f"{self.RABBIT_HOST}"

    @property
    def TIMETOLIVECACHE(self):
        return self.TTLCACHE

    @property
    def URLRATE(self):
        return f'{self.GETRATEDOLLAR}'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
