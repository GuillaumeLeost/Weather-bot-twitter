from crontab import CronTab

cron = CronTab(user='pi')
job = cron.new(command='python weather.py')
job.minute.every(30)

cron.write()
