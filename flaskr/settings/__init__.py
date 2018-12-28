import os
import sys
from . import local, prod, stage

_env = os.environ.get('FLASK_ENV', 'development')
env = _env.lower()

if env == 'development':
    config = local
elif env == 'staging':
    config = stage
elif env == 'production':
    config = prod
else:
    raise sys.exit(-1)

__all__ = [config]

