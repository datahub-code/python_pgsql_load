import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'postgresql',
            'DB_HOST': 'postgresql',
            'DB_NAME': 'postgresql',
            'DB_USER': 'postgresql',
            'DB_PASS': 'postgresql'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgresql',
            'DB_HOST': 'postgresql',
            'DB_NAME': 'postgresql',
            'DB_USER': 'postgresql',
            'DB_PASS': 'postgresql'
        }
    },
    'uat': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'postgresql',
            'DB_NAME': 'postgresql',
            'DB_USER': 'postgresql',
            'DB_PASS': 'postgresql'
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgresql',
            'DB_HOST': 'postgresql',
            'DB_NAME': 'postgresql',
            'DB_USER': 'postgresql',
            'DB_PASS': 'postgresql'
        }
    }

}