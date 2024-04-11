
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MYAPP",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=["development", "production", "testing"],
    env_switcher="MYAPP_MODE",
    
)








# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
