#Задача 1
import logging
import logging.handlers
import inspect
test_log = logging.getLogger('test_log')
test_log.setLevel(logging.INFO)

fh = logging.FileHandler("test.log")
fh.setFormatter(logging.Formatter("%(asctime)s %(message)s"))

test_log.addHandler(fh)


enable_log = True

def log(func):
    if enable_log:
        def wrapper(*arg):
            try:
                test_log.info("Вызов функции %s с аргументом %s" % (func.__name__, *arg))
                r = func(*arg)
                print("%s умножить 1000 на равно %s" % (*arg, r))
                return r
            except:
                parent = inspect.stack()[1][3]
                test_log.info("Функция %s вызвана из функции %s" % (func.__name__, parent))
                
        return wrapper
    else:
        return func

@log
def thousand(a):
    a = a*1000
    return a

thousand(2)


#Задача 2
@log
def func_z():
    pass

def main():
    func_z()

main()
