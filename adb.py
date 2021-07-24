import os
import subprocess


def command(args, wait=True, test=False):
    cmd = ['adb'] + args
    if not wait:
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    elif test:
        return subprocess.run(cmd, capture_output=True).returncode
    else:
        return subprocess.run(cmd, capture_output=True, check=True, text=True).stdout


def shell(args, root=False, wait=True, test=False):
    cmd = ['shell']
    if root:
        cmd += ['su', 'root']
        # cmd += ['su', '-c']
    cmd += args
    return command(cmd, wait, test)


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
