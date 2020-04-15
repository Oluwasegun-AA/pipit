#!/bin/sh
import os
from decouple import config

if config('ENV') == 'DEVELOPMENT':
  os.system('''psql django postgres << EOF
      DROP TABLE IF EXISTS "Users", "Users_groups", "Users_user_permissions", "auth_group", "auth_group_permissions", "auth_permission", "django_admin_log", "django_content_type", "django_migrations", "django_session" CASCADE;
  ''')
  # os.system('python manage.py migrate users zero')
  os.system('rm -rf **/**/migrations')
  os.system('python3 manage.py makemigrations users')
  os.system('python3 manage.py migrate')
  os.system('python3 manage.py loaddata app/users/fixtures/users.json')
  os.system('python3 manage.py runserver')
else:
  os.system('python3 manage.py runserver')
