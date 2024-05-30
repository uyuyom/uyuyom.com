from dirsync import sync

source_path = 'C:\\Users\\nauxnam\\AppData\\LocalLow\\IronGate\\Valheim\\worlds_local'
target_path = 'D:\\uyuyom.com\\valheim'

sync(source_path, target_path, 'sync', purge=True)
