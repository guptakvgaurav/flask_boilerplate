from . import base_config


base_config.log_config.update({
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

log_config = base_config.log_config

flask_config = {
    'DEBUG': True,
    'ENV': 'development'
}
