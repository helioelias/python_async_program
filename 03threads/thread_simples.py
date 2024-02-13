import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante', 10))
    
    th.start()
    print('program running')
    th.join()
    print('OK')
    
def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)
    
if __name__ == '__main__':
    main()