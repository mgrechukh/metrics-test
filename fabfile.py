from fabric.api import env, run, sudo, local, put, parallel, open_shell
from fabric.utils import abort
from boto import ec2
import datetime
import os

NAME="metric-test"
registry = "mgrechukh"

fabdir = os.path.dirname(env.real_fabfile)
tagfile = os.path.join(fabdir, '.tag-build')

def get_tag():
    print 'getting tag'
    with open(tagfile) as f:
        return f.readline().strip()

def save_tag(tag):
    with open(tagfile, 'w') as f:
        f.write('%s\n' % tag)

TODAY = datetime.datetime.now().strftime('%Y%m%d%H%M')

os.environ['DOCKER_BUILDKIT'] = "1"

def build_image(tag = TODAY):
    local("docker build -t {name}:{datetag} -f Dockerfile .".format(name = NAME, datetag = tag))
    local("docker tag {name}:{datetag} {name}:latest".format(name = NAME, datetag = tag))

def push_image(tag = TODAY):
    local("docker tag {name}:{datetag} {registry}/{name}:{datetag}".format(registry = registry, name = NAME, datetag = tag))
    local("docker push {registry}/{name}:{datetag}".format(registry = registry, name = NAME, datetag = tag))
    save_tag(tag)

