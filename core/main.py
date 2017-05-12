#!/usr/bin/env  python3
# author: wugong
import os
import sys
import configparser
import paramiko,threading
from multiprocessing import Process,freeze_support
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

user_file=os.path.join(BASE_DIR,'conf','user_info')

class Fabric(object):
    @staticmethod
    def exec_cmd(hostinfo,cmd,print_status):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostinfo["ip"], int(hostinfo['port']), hostinfo["user"], hostinfo["password"])

        t = paramiko.Transport(hostinfo["ip"], int(hostinfo['port']))
        t.connect(username=hostinfo["user"], password=hostinfo["password"])
        sftp = paramiko.SFTPClient.from_transport(t)

        if cmd.split()[0] in ('put','get'):

            cmd_dic = cmd.split()
            if cmd_dic[0] == 'put':
                cur_remote_dir = Fabric.exec_cmd(hostinfo, 'pwd',1).replace('\n', '')
                print(hostinfo["ip"],'upload to:',cur_remote_dir)
                cur_remote_dir = cur_remote_dir + '/' + os.path.basename(cmd_dic[1])
                sftp.put(cmd_dic[1], cur_remote_dir, callback=print("Upload Successfull"))
            elif cmd_dic[0] == 'get':
                local_dir = os.path.join(BASE_DIR, 'download', os.path.basename(cmd_dic[1]))
                sftp.get(cmd_dic[1], local_dir, callback=print("Download Successfull"))
        else:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            err=stderr.read()
            if len(err) == 0:
                result=stdout.read().decode()
            else:
                result=err.decode()
            if print_status == 0: print('------------[',hostinfo["ip"],'] ouput------------\n',result)
            return result

def run():
    ip_list=[]
    group_list=[]
    user_info = configparser.ConfigParser()
    user_info.read(user_file)
    for i in user_info:
        if i != 'DEFAULT':
            print("Group:".rjust(10, " "), i)
            group_list.append(i)
        for j in user_info[i]:
            a = eval(user_info[i][j])
            print("{0}".rjust(10, " ").format(a['ip']))
            ip_list.append(a['ip'])
    while True:
        ip_gname=input("Please select a ip address or group name >>:").strip()
        hostinfo_list=[]
        excu_cmd = Fabric()
        if ip_gname in ip_list:
            for i in user_info:
                for j in user_info[i]:
                    item=eval(user_info[i][j])
                    if item['ip'] == ip_gname:
                        hostinfo_list.append(item)
            break
        elif ip_gname in group_list:
            for i in user_info:
                if i == ip_gname:
                    for j in user_info[i]:
                        hostinfo_list.append(eval(user_info[i][j]))
            break
        else:
            print("The item not exists, Please retry.")
    th_list = []
    print_status=0
    while True:
        cmd = input(">>").strip()
        if len(cmd) == 0 :continue
        if cmd.lower() == 'exit':exit()
        for i in hostinfo_list:
            st = threading.Thread(target=excu_cmd.exec_cmd, args=(i,cmd,print_status,))
            st.start()
            th_list.append(st)

        for j in th_list:
            j.join()


