from __future__ import annotations


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, *kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    records = ['Jorge', 'Juan', 'Jose', 'Luis']

    def get_records(self):
        return self.records


def run():
    db1 = Database()
    db2 = Database()

    print(db1.get_records())

    if id(db1) == id(db2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


if __name__ == '__main__':
    run()
