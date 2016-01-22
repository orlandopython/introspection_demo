import glob, re, imp, re, inspect, os


def load_test_modules():
    """
    Imports modules that start with "test"

    Creates objects from classes with "Test"

    Run instance methods that start with "test"
    """

    # get the test moduels from package and import the module
    for module in glob.glob("test*.py"):
        name, ext = os.path.splitext(module)
        m = imp.load_source(name, module)

        # get test classes from module
        for attribute in dir(m):
            if re.match("Test.*", attribute):

                # import the class and create an instance
                klass = getattr(m, re.match("Test.*", attribute).group(0))
                instance = klass()
                methods = inspect.getmembers(instance, predicate=inspect.ismethod)

                # call methods have contain the word test
                for method in methods:
                    if re.match("test", method[0]):
                        method[1]()

if __name__ == '__main__':
    load_test_modules()
