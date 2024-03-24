# with and class (using magic method)

class Hello:
    
    def __init__(self) -> None:
        print('Hello 객체 생성')
    
    def __enter__(self):
        print('with 구문 진입')
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('with 구문 탈출')
        
with Hello():
    print('with 구문 내부')

import sys
print(sys.path[0])
