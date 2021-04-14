#모듈이란? 미리 만들어 놓은 py 파일을 함수 변수 클래스를 쓰겠다
# seems like 라이브러리?

#만약 다른 폴더에 모듈이 있을경우 sys 에 경로를 추가해주고 from 으로 가져온다.

import sys
sys.path.append("C:\\Users\\dkrle\\Desktop\\project\\python\\subfolder")
from mod2 import add
from mod1 import sum

#이렇게 모드1 안에 있는 함수임을 명시해줘야하나 보다.
#import mod1 이라고 해줄때는 밑과 같이 적는다.
#print(mod1.sum(4,5))

#from mod1 import sum 이라고 해주면 밑과 같이 해준다.
print(sum(4,5))
print(add(4,5))

#모듈에 print 해주니까 print 도 불러오고 sum도 불러옴

# 만약 패키지 이면 이게 진짜 라이브러리랑 비슷 ㅇㅇ
# game/
#   __init__.py
#   sound/
#       __init__.py
#       echo.py
#   graphic/
#       __init__.py
#       render.py
# 위와 같이 폴더가 구성되어 있다면
# from game.sound import echo
# echo.loud() 어쩌구 이렇게 쓸 수 있고

# import game.sound.echo 이렇게 쓰면
# game.sound.echo.loud() 이런 식으로 써야한다.

# 귀찮을 때는 define 처럼 as 를 사용할 수 있다.
# from game.sound.echo import loud as lo
# lo() 이렇게 써버릴 수 있다.

# from game.sound import * 을 쓸 수 있다.
# 대신 sound 폴더의 __init__.py 안에 들어가서
# __all__ = ['echo'] 라고 all 을 설정해주어야한다.

# render.py 안에서 echo 에 있는 함수를 사용하고 싶을 경우에는
# from ..sound.echo import echo_test as echo 라고 해주면된다.
# ..은 상위폴더로 가는 것을 의미한다.
# .. 으로 game 폴더에 가서 sound 로 가고 echo 로 들어감이다.