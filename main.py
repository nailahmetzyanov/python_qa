import subprocess
import time

output = subprocess.run(["ps", "axo", "user:20,pcpu,rss,comm:20", "--sort", "-%cpu", "--no-heading"],
                        capture_output=True).stdout.decode("utf-8")
list_of_processes = [i.split() for i in output.split("\n")]
list_of_processes.pop()
prc_users = {}
total_cpu = 0
total_mem = 0

for i in list_of_processes:
    while len(i) > 4:
        i[len(i) - 2] += f" {i.pop()}"
    if i[0] in prc_users.keys():
        prc_users[i[0]] += 1
    else:
        prc_users[i[0]] = 1
    total_cpu += float(i[1])
    total_mem += float(i[2])

processes_per_user = "\n".join([f"{i[0]}: {i[1]}" for i in sorted(prc_users.items(), key=lambda x: x[1], reverse=True)])
total_processes = len(list_of_processes)
total_mem_mb = total_mem / 1000
system_users = ", ".join([i for i in prc_users.keys()])

output_dict = {
    "Отчёт о состоянии системы:\n"
    "Пользователи системы": f"{system_users}\n",
    "Процессов запущено": f"{total_processes}\n\n",
    "Пользовательских процессов": f"\n{processes_per_user}\n\n",
    "Всего памяти используется": f"{'%.2f' % total_mem_mb}Mb\n",
    "Всего CPU используется": f"{'%.2f' % total_cpu}%\n",
    "Больше всего памяти использует": f"{list_of_processes[0][3]}\n",
    "Больше всего CPU использует": f"{sorted(list_of_processes, key=lambda x: x[2], reverse=True)[0][3]}\n"
}

for i, j in output_dict.items():
    print(f"{i}: {j}", end='')

with open(f"{time.strftime('%d-%m-%y-%H:%M', time.localtime())}-stats.txt", "w") as out:
    for i, j in output_dict.items():
        out.write(f"{i}: {j}")