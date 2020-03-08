import os
Import("env")

env_name = str(env["PIOENV"])
env.Replace(PROGNAME="%s_DW6" % (env_name))
print("Environment: %s" % (env_name))