from flask import Blueprint

from ..controllers.user import UserController

# "g" is a global object (scoped to your current request)
# where you can store everything:
#
# g.user = my_current_user_extracted_from_cookie
#

user_views = Blueprint("user_views", __name__, url_prefix="/users")


@user_views.route("", methods=["GET"])
def get_users():
    return UserController.get_all()
