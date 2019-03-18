# redefine platformio UPLOAD target to copy executable to a directory in %PATH% (local app data)
# TODO: does not work: *** Do not know how to make File target `upload'
Import('env')
environ = env['ENV']
target='%s\\Microsoft\\WindowsApps' % environ['LOCALAPPDATA']
env.Replace(UPLOADCMD='copy /y %s %s' % (env['PROG_PATH'], target))
