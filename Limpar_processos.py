import psutil

processos = []

for proc in psutil.process_iter([
    'pid','username','name'
    ]):
    try:
        info = {
            'pid':proc.info['pid'],
            'name':proc.info['name'],
           ## "cpu":proc.cpu_percent(),
            'memory':proc.memory_percent()
        }
        processos.append(info)

    except:
        print('fail')

processos.sort(key = lambda p: p['name'])
for p in processos:
    if p['memory']>3:
        print(
            p['pid'],
            p['name'],
            p['memory']
        )
        psutil.Process.terminate
        print(psutil.Process.terminate)
#   process = psutil.Process(p['pid'])
#    process.terminate()