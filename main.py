import rstr, sys
 
def gen(key='generate'):
    password = rstr.xeger(r"/^(?=.*[A-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[*_%$@])(?!.*[pPoO])\S{6,}$/")
    passwords = password.split()
    strong = max(passwords)
    if len(strong) < 8:
        gen()
    return strong

if __name__ == "__main__":
    if 'generate' in sys.argv[1:]:
        print(gen())