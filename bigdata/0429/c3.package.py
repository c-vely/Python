'''
# echo 모듈을 import하여 실행하는 방법 1
import game.sound.echo
game.sound.echo.echo_test()


# echo 모듈을 import하여 실행하는 방법 2
from game.sound import echo
echo.echo_test()


# echo 모듈을 import하여 실행하는 방법 3
from game.sound.echo import echo_test
echo_test()


# 다음과 같이 echo_test 함수를 사용하는 것은 불가능 1
import game #game 디렉터리의 __init__.py에 정의한 것만 참조
game.sound.echo.echo_test()


# 다음과 같이 echo_test 함수를 사용하는 것은 불가능 2
import game.sound.echo.echo_test
echo_test()

'''


