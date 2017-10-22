#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。'

'''
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


# 编写了一个函数_format_addr()来格式化一个邮件地址。注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

# 构造一个最简单的纯文本邮件，注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 发件人
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
# 收件人，msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# 邮件主题
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

'''
如果我们查看Email的原始内容，可以看到如下经过编码的邮件头：
----------------------------------------------------------------------
From: =?utf-8?b?UHl0aG9u54ix5aW96ICF?= <xxxxxx@163.com>
To: =?utf-8?b?566h55CG5ZGY?= <xxxxxx@qq.com>
Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmeKApuKApg==?=
----------------------------------------------------------------------

这就是经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本。如果我们自己来手动构造这样的编码文本，显然比较复杂。
'''

# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)
# 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)
# login()方法用来登录SMTP服务器
server.login(from_addr, password)
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
