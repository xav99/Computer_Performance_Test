from time_decorator import timer

for i in range(5):
    @timer
    def x():
            for _ in range(999999999):
                pass
      

