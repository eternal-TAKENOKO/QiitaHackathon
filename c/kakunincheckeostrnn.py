import ctypes

libc = ctypes.cdll.LoadLibrary("./checkeostrnn.so")

def main():
	print(libc.check_eostr_nn("たけのこ"))

if __name__ == "__main__":
    main()