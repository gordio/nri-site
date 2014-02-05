from fabric.decorators import task
from fabric.context_managers import settings
from fabric.api import require, env, local, abort, run as frun
from fabric.contrib.console import confirm
from fabric.colors import green, red


@task
def build():
    """
    Build project environment.
    """
    stage('Updating virtual environment...')
    do('[ -e venv ] || virtualenv venv --no-site-packages --python=python3.3')
    do('venv/bin/pip install --upgrade -r requirements.txt')

    stage('Update assets...')
    manage('compilemessages')
    manage('collectstatic -c --noinput -v 0')

    stage('Updating database...')
    manage('syncdb --noinput')
    manage('migrate --noinput')


@task
def run():
    """
    Start project in debug mode (for development).
    """
    do('venv/bin/python ./manage.py runserver')


@task
def manage(cmd):
    """
    Run django manage `cmd`
    """
    return do('venv/bin/python ./manage.py {0}'.format(cmd))


def stage(message):
    """
    Show `message` about current stage
    """
    print(green("\n *** {0}".format(message), bold=True))


def do(*args):
    """
    Runs command locally or remotely depending on whether a remote host has
    been specified and ask about continue on fail.
    """
    with settings(warn_only=True):
        if env.host_string:
            with settings(cd(config.remote_path)):
                result = frun(*args, capture=False)
        else:
            result = local(*args, capture=False)

    if result.failed:
        if result.stderr:
            print(red(result.stderr))
        if not confirm("Continue anyway?"):
            abort('Stopped execution per user request.')
