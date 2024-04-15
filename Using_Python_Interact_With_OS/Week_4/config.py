import subprocess

subprocess.run(['cmd.exe', '/c', 'dir'])
#alternative on sleep command
subprocess.run(['cmd.exe', '/c', 'timeout', '5'])
#return the error code 1, not ok code 0
print(erro:= subprocess.run(['cmd.exe', '/c', 'this_file_does not_exist']))
#just check the connectivity. -n did not working correctly
ping_result = list(subprocess.Popen('ping 127.0.0.1') for _ in range(0,4))

import re
def show_time_of_pid(line):
  pattern = r'(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+)\s[\w\.]+\s[\w=_]+\[(\d{5})]'
  result = re.search(pattern, line)
  return '{} pid:{}'.format(result[1],result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440