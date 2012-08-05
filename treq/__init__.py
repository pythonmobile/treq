import treq.api
from treq.api import head, get, post, put, delete, request
head, get, post, put, delete, request
pool = treq.api.pool

__all__ = ('head', 'get', 'post', 'put', 'delete', 'pool')
__version__ = "0.1dev"
