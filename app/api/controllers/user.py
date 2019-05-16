from ...models.user import User


class UserController:
    @classmethod
    def get_all(cls):
        users = []
        for user in User.all():
            users.append(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            )
        return users
