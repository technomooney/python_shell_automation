import subprocess, re, datetime, os


def main():
    #variables	
    file_name = '\\python_wifi_reconnect_log.txt'
    log_path = get_path(file_name)
    counter = 0 #limmit the runs
    address = "8.8.8.8"
    wifi_profile_name = '' #add your profile that you want to connect to... use the netsh wlan show profiles command to find the names
    connected= detect_connectivity(address)
    result,flag = '',''
	
	
    while connected !=True or counter >= 4:
        result,flag = reconenct_to_wifi(wifi_profile_name)
        connected = detect_connectivity(address)
        counter +=1
    while flag == False:
        save_to_log(result,log_path,wifi_profile_name)
        main()
    if connected == True:
        save_to_log(f'Already Conneted at {datetime.datetime.now()}',log_path,wifi_profile_name)
    

def get_path(file_name):
    home_path = os.path.join(os.getenv("HomeDrive"),os.getenv("HomePath"))
    log_path=home_path+file_name
    return log_path

def detect_connectivity(address, times_to_ping='3'):
    ping_output = subprocess.run(['ping','-n',times_to_ping, address],capture_output=True).stdout.decode()
    if re.findall(r'[Reply]', ping_output):
        return True
    else:
        return False
def reconenct_to_wifi(wifi_profile):
    subprocess.run(['netsh','wlan','connect','name=',wifi_profile],capture_output=True).stdout.decode()
    results = subprocess.run(['netsh','wlan','connect','name=',wifi_profile],capture_output=True).stdout.decode()

    if 'successfully' in results:
        return f"compleated successfully on {datetime.datetime.now()}", True
    else:
        return results,False
def save_to_log(result,log_path,profile_name=None):
    if os.path.exists(log_path) == True:
        log_file = open(log_path,'a')
    elif os.path.exists(log_path) !=True:
        log_file = open(log_path,'w')
    else:
        print(f"errors with opening {log_path}!")
    log_file.write(f'got result [{result}] with profile [{profile_name}].\n')
    log_file.close()
main()

