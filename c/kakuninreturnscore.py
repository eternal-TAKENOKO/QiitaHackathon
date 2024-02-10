import ctypes

libc = ctypes.cdll.LoadLibrary("./returnscore.so")
libc.return_score.restype = ctypes.c_long

def main():
	print(libc.return_score(2147483647))

if __name__ == "__main__":
    main()