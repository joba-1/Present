# use PROGNAME as defined in platformio.ini as executable name
Import('env')
build_flags = env.ParseFlags(env['BUILD_FLAGS'])
defines = {key: value for (key, value) in build_flags.get('CPPDEFINES')}
env.Replace(PROGNAME=defines.get('PROGNAME', 'Program'))
