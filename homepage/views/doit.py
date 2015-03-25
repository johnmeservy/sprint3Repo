import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django; django.setup()

from django.contrib.auth import models as conmod
import homepage.models as hmod

from django.contrib.auth.models import Group, Permission, ContentType
permission = Permission()
permission.codename = 'super'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Superuser Privileges'
permission.save()

group = Group()
group.name = "superusers"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=82)
group.permissions.add(permission)

user = hmod.User()
user.username = 'super'
user.set_password('super')
user.is_superuser = True
user.is_staff = True
user.save()

group.user_set.add(user)


permission = Permission()
permission.codename = 'staff'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Staff Privileges'
permission.save()

group = Group()
group.name = "staff"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=83)
group.permissions.add(permission)

user = hmod.User()
user.username = 'staff'
user.set_password('staff')
user.is_superuser = False
user.is_staff = True
user.save()

group.user_set.add(user)


permission = Permission()
permission.codename = 'guests'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Guest Privileges'
permission.save()

group = Group()
group.name = "guest"
group.save()
group.permissions.add(permission)
permission = Permission.objects.get(id=84)
group.permissions.add(permission)

user = hmod.User()
user.username = 'guest'
user.set_password('guest')
user.is_superuser = False
user.is_staff = False
user.save()

group.user_set.add(user)
