# from travel import vietnam
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
#
#
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

# *을 쓴다는 의미는 travel 패키지의 모든것을 가져온다는 말인데
# 실제로는 개발자가 공개범위를 설정해줘야한다.
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
#
#
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

from travel import *
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))
