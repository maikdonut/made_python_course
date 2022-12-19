### Создадим классы
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
```
### Сгенерируем переменные
```py
def generate_params(n:int)-> list:
    names = ['Alice', 'Bob', 'Peter']
    experience = [1, 2, 5, 10]
    salary = list(range(1, n, 10))
    params = list(itertools.product(names, experience, salary)) 
    return params

N = 10_000_000
empl_params = generate_params(N) # 12000000 emploees
```
### Время создания
![image](https://user-images.githubusercontent.com/73718190/208393024-4ea46e81-b69f-4da9-9c25-fc671ec1114a.png)
### Время доступа
![image](https://user-images.githubusercontent.com/73718190/208393173-02bdcef7-a243-4361-b830-5572c709f7bb.png)
### Время изменения
![image](https://user-images.githubusercontent.com/73718190/208393263-9e11d0e1-375d-4c38-bbfb-c747e2ffa279.png)
### Время удаления
![image](https://user-images.githubusercontent.com/73718190/208393290-a11fbee8-03ed-497b-9b4f-c55c2c2094d7.png)



