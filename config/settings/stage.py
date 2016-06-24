from .base import *

DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "{{ lookup('vault', 'secret/yurttest_staging', 'secret_key', 'vault_one_true_vault.json') }}"

ALLOWED_HOSTS = ["162.243.112.16", ]
