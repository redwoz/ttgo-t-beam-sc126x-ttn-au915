lib_name = "basicmac"
git_user = "meetjestad"

##################################################################

from genericpath import isdir
from os.path import join, isfile

Import("env")

# check to see if package already downloaded
lib_path = join(env['PROJECT_DIR'], "lib", lib_name)

if not isdir(lib_path):
    # need to git/clone it
    env.Execute("rm -rf /tmp/%s/; cd /tmp; git clone https://github.com/%s/%s;" % ( lib_name, git_user, lib_name ) )
    env.Execute("cd /tmp/basicmac; ./target/arduino/export.sh %s/lib/basicmac; rm -rf /tmp/basicmac/;" % ( env['PROJECT_DIR'] ) )

# patch file only if we didn't do it before
patchflag_path = join(env['PROJECT_DIR'], "lib", lib_name+".patch.done")

if not isfile(patchflag_path):
    env.Execute("cd %s; patch --forward --batch --strip=0 --input=../%s --no-backup-if-mismatch --reject-file=- > %s" % (lib_path, lib_name+".patch", patchflag_path))

# reverse: env.Execute("cd %s; patch --reverse --batch --strip=0 --input=../%s --no-backup-if-mismatch --reject-file=-" % (lib_path, lib_name+".patch"))

# diff -Naru /tmp/USB_Host_Shield_2.0 . --exclude=".git" > ../USB_Host_Shield_2.0.patch
