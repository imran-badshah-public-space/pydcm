def error(prt):
    print(f"\033[91m{prt}\033[00m")

def success(prt):
    print(f"\033[92m{prt}\033[00m")

def warning(prt):
    print(f"\033[93m{prt}\033[00m")

def info(prt):
    print(f"\033[96m{prt}\033[00m")

def subInfo(prt):
    print(f"\033[97m{prt}\033[00m")

def black(prt):
    print(f"\033[98m{prt}\033[00m")

def reset(prt):
    print(f"\033[0m{prt}\033[00m")
