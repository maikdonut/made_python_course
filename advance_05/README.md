### Создадим классы
```py
class Employee:  
    def __init__(self, name, experience, salary):  
        self.name = name  
        self.experience = experience
        self.salary = salary 
        
class SlotEmployee: 
    __slots__ = ('name', 'experience', 'salary')
    def __init__(self, name, experience, salary):  
        self.name = name  
        self.experience = experience
        self.salary = salary 
```
### Сгенерируем переменные
```py
def generate_params(n:int)-> list:
    names = ['Alice', 'Bob', 'Peter']
    experience = [1, 2, 5, 10]
    salary = [sal for sal in range(1, n, 10)]
    params = list(itertools.product(names, experience, salary)) 
    return params

N = 10_000_000
empl_params = generate_params(N) # 12000000 emploees
```
### Время создания
```

```
