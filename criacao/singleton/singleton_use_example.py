from criacao.singleton.Singleton import Singleton

test1 = Singleton()
test1.id = 12
print(test1.id)
print(test1)

test2 = Singleton.get_instance()
test2.id = 154
print(test2.id)
print(test1.id)
print(test2)