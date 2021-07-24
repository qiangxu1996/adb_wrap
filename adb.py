import os
import subprocess


def command(args, test=False):
    cmd = ['adb']
    cmd += args
    if test:
        return subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode
    else:
        return subprocess.run(cmd, check=True,
                              stdout=subprocess.PIPE, encoding='utf-8'
                              ).stdout


def shell(args, root=False, wait=True, test=False):
    cmd = ['adb', 'shell']
    if root:
        cmd += ['su', 'root']
        # cmd += ['su', '-c']
    cmd += args
    if wait:
        if test:
            return subprocess.run(cmd, stdout=subprocess.DEVNULL).returncode
        else:
            return subprocess.run(cmd, check=True,
                                  stdout=subprocess.PIPE, encoding='utf-8'
                                  ).stdout
    else:
        return subprocess.Popen(cmd)


def pull(file, dest=None):
    cmd = ['pull', str(file)]
    if dest:
        cmd.append(str(dest))
    command(cmd)


def push(file, dest, sync: bool = False):
    cmd = ['push']
    if sync:
        cmd.append('--sync')
    cmd.append(str(file))
    cmd.append(str(dest))
    command(cmd)


def default_device(serial: str):
    os.environ['ANDROID_SERIAL'] = serial
