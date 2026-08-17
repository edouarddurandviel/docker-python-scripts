from crontab import CronTab

def helloWorld():
    
    with CronTab(user='root') as cron:
        job = cron.new(command='python _exec_every_minutes')
        job.minute.every(1)
        print('cron.write() was just executed')
        