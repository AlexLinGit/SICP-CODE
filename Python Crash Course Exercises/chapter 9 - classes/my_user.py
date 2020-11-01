from users import Users
from m_admins_privileges import Admins

admin = Admins(first='alex', last='lin', user_info=['lynnfield', 'anonymous'])
admin.describe_user()
admin.privileges.show_privileges()
