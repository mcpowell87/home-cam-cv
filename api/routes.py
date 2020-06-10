from api import api

@api.route('/')
def index():
    return "Hey, you shouldn't be here!"

from api import testGet
from api import check_face
from api import errorhandler