import subprocess


class PC:

    def connect_wifi(self, ssid, password):
        command = 'networksetup -setairportnetwork en0 ' + ssid + ' ' + password + ''
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Wifi Connected !!")
