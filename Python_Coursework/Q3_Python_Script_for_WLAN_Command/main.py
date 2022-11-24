'''

If you want to run this script on an ENGLISH LANGUAGE computer,
you should replace "所有用户配置文件" with "All User" on line 19
and replace "关键内容" with "Key Content" on line 33.

'''

import subprocess
# the library we need to use in this program

# search the wifi names
output = subprocess.run(['netsh','wlan','show','profiles'], capture_output = True)\
    .stdout.decode('gbk').split('\n')
# This is the progress when we want to acquire all user configuration profiles in cmd, in the other words, all the names of wifi that the computer connected.
# we will capture the output and error from the subprocess ==> "capture_output = True"
# the output will be decoded by 'gbk' ==> "stdout.decode('bgk')
# split by ('\n'), because the format of the output in cmd is line by line.
wifi_p = [line.split(':')[1][1:-1] for line in output if "所有用户配置文件" in line]
# because the language of my computer is CHINESE, So it's no denied that using "所有用户配置文件", which means that "all user configuration profiles"
# all the names of wifi the computer connected will be assigned to "wifi_p"
# the format of the output will be "all user configuration profile : wifi_names", and I save it into list, so use "split(':')" to save it,
# and the names of wifi will be in the second place, that means that using '[1]'.
# there is an indent before the wifi names, so it will start from 1, instead of 0, and end to -1 ==> [1:-1]

# search the password
lst=[]         # create a list to save all the wifi names and passwords
for wifi in wifi_p:         # iterate through the list of wifi names
    pass_word = subprocess.run(['netsh','wlan','show','profile',wifi,'key=clear'],capture_output = True).stdout.decode('gbk',errors = 'ignore').split('\n')
    # the same thing as the previous that, but i add "wifi" and "key=clear" to get password
    # "wifi" is value we iterate in wifi_p
    # "key=clear" is that we want to display the output as plaintext
    password_res = [line.split(':')[1][1:-1] for line in pass_word if "关键内容" in line]
    # the same thing as the previous that
    # "关键内容" means "key content" (MAYBE)
    try: # use "try" to prevent the program from error.
        print(f'wifi：{wifi}，password: {password_res[0]}')
        # show the names of wifi and the password
        lst.append(f"wife: {wifi} | password: {password_res[0]}\n")
        # append the wifi names and password into the lst
    except IndexError:
        print(f'wifi：{wifi}，password: fail to extract')
        # if the password of some wifi can not be identified, the program will show the index error, but we can use except to ignore it

print(lst)
# show the list after iteration

f = open("secret.txt", "w")
# create a txt file called secret, and ready to write something
f.writelines(lst)
# write something (list)
f.close()
# close it, otherwise this file will always be occupied.