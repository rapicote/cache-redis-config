import os
import json
from redis import Redis
from typing import Dict

class CacheRedisConfig:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = self.connect_to_redis()

    def connect_to_redis(self) -> Redis:
        return Redis(host=self.host, port=self.port, db=self.db)

    def get_config(self, key: str) -> Dict:
        config = self.redis_client.get(key)
        if config:
            return json.loads(config)
        else:
            return {}

    def set_config(self, key: str, config: Dict) -> bool:
        try:
            self.redis_client.set(key, json.dumps(config))
            return True
        except Exception as e:
            print(f"Error setting config: {str(e)}")
            return False

    def delete_config(self, key: str) -> bool:
        try:
            self.redis_client.delete(key)
            return True
        except Exception as e:
            print(f"Error deleting config: {str(e)}")
            return False

def main():
    cache_redis_config = CacheRedisConfig()
    config_key = "example_config"
    example_config = {"key": "value"}
    cache_redis_config.set_config(config_key, example_config)
    retrieved_config = cache_redis_config.get_config(config_key)
    print(retrieved_config)
    cache_redis_config.delete_config(config_key)

if __name__ == "__main__":
    main()