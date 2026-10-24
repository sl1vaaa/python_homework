import logging
# Task 1

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = args if args else "none"
        keyword = kwargs if kwargs else "none"

        logger.log(logging.INFO, f"""function: {func.__name__}
        positional parameters: {positional}
        keyword parameters: {keyword}
        return: {result}
        """)
        return result
    return wrapper

@logger_decorator
def nothing():
    print("Hello World!")

@logger_decorator
def positional_function(*args):
    return True

@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator

nothing()
positional_function(105, 21, 333, "hellomonkeys")
keyword_function(name="Miroslav", age=17, prog_language="Python")