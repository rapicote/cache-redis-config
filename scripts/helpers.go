package cache_redis_config

import (
	"fmt"
	"log"
)

func GetRedisConfig(redisHost string, redisPort int, redisPassword string) RedisConfig {
	redisConfig := RedisConfig{
		Host:     redisHost,
		Port:     redisPort,
		Password: redisPassword,
	}

	if redisHost == "" {
		log.Fatal("Redis host is required")
	}

	if redisPort <= 0 {
		log.Fatal("Redis port should be greater than 0")
	}

	return redisConfig
}

type RedisConfig struct {
	Host     string
	Port     int
	Password string
}