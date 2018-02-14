import os 
#a;sdflk;
#sdfg

from yoconfigurator.base import read_config

app_dir = os.path.abspath(os.path.dirname(__file__))
conf = read_config(app_dir)
aconf = conf.lintreview
cconf = conf.common

activate_this = conf.deploy.root + '/lintreview/live/virtualenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

os.environ.setdefault("LINTREVIEW_SETTINGS", conf.deploy.root + '/lintreview/live/settings.py')

print('1','2')
print('1',"2")
print('1','2')
print('1','2')
print('1','2')
print('1',"2")
print('1','2')
print('1','2')
print('1','2')
print('1','2')
print('1',"2")
print('1','2')
print('1','2')
print('1','2')
print('1','2')
print('1','2')
print('1',"2")
print('1','2')
print('1','2')
print('1','2')
print('1','2')
print('1',"2")
print('1',"2")
print('1',"2")
print('1','2')
print('1','2')
print('1','2')
print('1','2')
print('1',"2")


from lintreview.web import app as application
