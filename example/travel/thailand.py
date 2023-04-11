class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (가격 50만)")


# 모듈 직접 실행
# 모듈이 직접 실행될때 변수 __name__은 '__main__'이다.

# 모듈이 임포트될 때 변수 __name__은 원래의 모듈 이름이다.
# 따라서 if __name__ == '__main__이라는 것은 이 모듈 내에서 직접 실행될때만 True라고 할 수 있다.

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
