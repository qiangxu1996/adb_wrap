import os
import subprocess
from enum import Enum


class Su(Enum):
    AOSP = 1
    MAGISK = 2


_su_variant = Su.MAGISK


def command(args, check=True, wait=True):
    cmd = ['adb'] + args
    if not wait:
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    else:
        return subprocess.run(cmd, capture_output=True, check=check, text=True)


def shell(args, root=False, check=True, wait=True):
    cmd = ['shell']
    if root:
        if _su_variant == Su.AOSP:
            cmd += ['su', 'root']
        elif _su_variant == Su.MAGISK:
            cmd += ['su', '-c']
    cmd += args
    return command(cmd, check, wait)


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


def su_variant(variant):
    global _su_variant
    _su_variant = variant
