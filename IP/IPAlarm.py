import json
from urllib.request import urlopen

import os
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 两个获取ip地址的网站
ip_url_1 = 'https://api.ipify.org/?format=json'
ip_url_2 = 'http://jsonip.com'

# 配置文件名
config_file_name = '.global_ip.json'

# 第三方 SMTP 服务
mail_host = ""      # SMTP服务器
mail_user = ""      # 用户名
mail_pass = ""               # 授权密码，非登录密码

sender = ''    		# 发件人邮箱(最好写全, 不然会失败)
receivers = ['']  	# 接收邮件，可设置为你的QQ邮箱或者其他邮箱

title = 'IP地址更变'  			# 邮件主题
content = ''    				# 邮件内容

# 检查配置文件及其权限
def check_configfile_exist():
    file_exist = os.access(config_file_name, os.F_OK)
    file_read  = os.access(config_file_name, os.R_OK)
    file_write = os.access(config_file_name, os.W_OK)
    return{'file_exist':file_exist,'file_read':file_read,'file_write':file_write}

def generate_configfile(ip_addr):
    config_construct = {
        "ip_addr": ip_addr
    }
    with open(config_file_name, "w", encoding='utf8') as fp:
        fp.write(json.dumps(config_construct,indent=4, ensure_ascii=False))
    fp.close()

def sendEmail():

    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
    email_client.quit()



localtime = time.localtime(time.time()) # 打印本地时间
print("\n" + time.asctime(localtime))

# 通过两个网站获取ip地址
my_ip_1 = str(json.load(urlopen(ip_url_1))['ip'])
my_ip_2 = str(json.load(urlopen(ip_url_2))['ip'])

if (my_ip_1 == my_ip_2):
    ip_addr = my_ip_1
else:
    ip_addr = "ip_1 :" + my_ip_1 + "\n" + "ip_2 :" + my_ip_2

if(check_configfile_exist()['file_exist'] & check_configfile_exist()['file_write']):
    config_file = open(config_file_name,'r')
    read_context = json.load(config_file)
    old_ip = read_context['ip_addr']
    config_file.close()
    if (old_ip == ip_addr):
        print("ip address is up-to-date")
    else:
        content = "旧的IP地址 :  " + old_ip + '\n' + "新的IP地址 ： " + ip_addr
        sendEmail()
        generate_configfile(ip_addr)
else:
    generate_configfile(ip_addr)
    content = "new ip address is : " + ip_addr
    sendEmail()
