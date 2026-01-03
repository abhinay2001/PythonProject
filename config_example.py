import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': os.getenv('SOURCE_DB_HOST', '127.0.0.1'),
            'DB_PORT': int(os.getenv('SOURCE_DB_PORT', '3306')),
            'DB_NAME': os.getenv('SOURCE_DB_NAME', 'retail_db'),
            'DB_USER': os.getenv('SOURCE_DB_USER', 'retail_user'),
            'DB_PASS': os.getenv('SOURCE_DB_PASS', 'retail_pass'),
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': os.getenv('TARGET_DB_HOST', '127.0.0.1'),
            'DB_PORT': int(os.getenv('TARGET_DB_PORT', '5432')),
            'DB_NAME': os.getenv('TARGET_DB_NAME', 'retail_db'),
            'DB_USER': os.getenv('TARGET_DB_USER', 'retail_user'),
            'DB_PASS': os.getenv('TARGET_DB_PASS', 'retail_pass'),
        }
    }
}