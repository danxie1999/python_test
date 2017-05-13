from urllib import request


##Get URL
#with request.urlopen('https://www.baidu.com/') as f:
#	data=f.read()
#	print("Status:{},{}".format(f.status,f.reason))
#	for k,v in f.getheaders():
#		print("{}:{}".format(k,v))
#	print('Data:{}'.format(data.decode('utf-8')))

##Get by simulating the browser's behavior 
#req=request.Request('http://www.douban.com/')

#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0')

#with request.urlopen(req) as f:
#	print("Data: {}".format(f.read().decode('utf-8')))


from urllib import request, parse

print('Login to weibo.cn...')
#email = input('Email: ')
passwd = input('Password: ')
email='xiedan199@163.com'


login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
input('')