### 1. Сравнение использования weakref и слотов
#### Создадим классы
```py
class Employee:
    def __init__(self, name:str, experience:int, salary:int):
        self.name = name
        self.experience = experience
        self.salary = salary


class SlotEmployee:
    __slots__ = ("name", "experience", "salary")

    def __init__(self, name:str, experience:int, salary:int):
        self.name = name
        self.experience = experience
        self.salary = salary
        
class WeakRefEmployee: 
    __slots__ = ('name', 'experience', 'salary', '__weakref__')
    def __init__(self, name, experience, salary):  
        self.name = name  
        self.experience = experience
        self.salary = salary
```
#### Сгенерируем переменные
```py
def create_params(amount:int):
    names = ['Alice', 'Bob', 'Peter']
    experience = [1, 2, 5, 10]
    salary = list(range(1, amount, 10))
    params = list(itertools.product(names, experience, salary)) 
    return params

N = 10_000_000
empl_params = create_params(N) # 12000000 emploees
```
#### Время создания
![время_создания](https://user-images.githubusercontent.com/73718190/209364723-cba3179c-de94-4d62-aaa4-7d12fad00c17.png)
#### Время доступа
![время_доступа](https://user-images.githubusercontent.com/73718190/209364744-e4c767a3-b6ad-4669-8236-e3d35b04b360.png)
##### Время изменения
![время_изменения](https://user-images.githubusercontent.com/73718190/209364757-48058524-bf2f-4c16-b5b3-59f9198f3b32.png)
#### Время удаления
![время_удаления](https://user-images.githubusercontent.com/73718190/209364773-3e143966-6d16-49d0-ad75-459f17614559.png)

### 2. Профилирование
#### Профилирование вызовов
```py
import cProfile, pstats, io


pr = cProfile.Profile()
pr.enable()


def run(params):
    lst_a = [Employee(*i) for i in params]
    lst_slot = [SlotEmployee(*i) for i in params]
    lst_weak = [WeakRefEmployee(*i) for i in params]

    del lst_a
    del lst_slot
    del lst_weak


run(empl_params)  # 12000000 emploees
pr.disable()

s = io.StringIO()
sortby = "cumulative"
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
```
![профилирование_вызовов](https://user-images.githubusercontent.com/73718190/209364901-265279cb-e5ba-47e1-8fa0-da6ad8134a9d.png)
#### Профилировние памяти реализовно в profile_memory.py
![профилирование_памяти](https://user-images.githubusercontent.com/73718190/209364939-f79d8765-c3a6-4b1b-a7af-17b757e80059.png)
### 3. Декоратор профилирования реализован в deco_profile.py
Один вызов функции run()
![декоратор_профилирования_1](https://user-images.githubusercontent.com/73718190/209364996-c6834f8b-21e2-4567-bc6f-c7af878fce96.png)
Три вызова функции run() с разными параметрами
![декоратор_профилирования_2](https://user-images.githubusercontent.com/73718190/209365113-30361cae-aa06-4f8f-96ea-5da9adea01f1.png)


