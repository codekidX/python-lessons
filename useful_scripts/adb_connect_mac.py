
import os

def main():
	port = raw_input("In which port is your mobile running adb ? : ")
	cmd = './adb connect 192.168.0.' + port + ':5555'
	adb_cmd = 'cd /Users/snowpuppet/Library/Android/sdk/platform-tools && ' + cmd
	os.system(adb_cmd)


if __name__ == '__main__':
	main()