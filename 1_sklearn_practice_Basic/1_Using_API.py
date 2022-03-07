# API 사용 방법
# 1. Scikit-Learn으로부터 적절한 estimator class를 import해서 model의 class 선택
# 2. Class를 원하는 값으로 인스턴스화해서 모델의 하이퍼파라미터 선택
# 3. Data를 특징 배열과 대상 벡터로 배치
# 4. 모델 인스턴스의 fit() 메서드를 호출해 모델을 데이터에 적합하도록 함
# 5. 모델을 새 데이터에 대해서 적용
#   - 지도 학습: 대체로 predict() 메서드를 사용해 알려지지 않은 데이터에 대한 레이블을 예측
#   - 비지도 학습: transform()이나 predict() 메서드를 사용해 데이터의 속성을 변환하거나 추론

import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['seaborn-whitegrid'])

# numpy, matplotlib (예시)
# y값이 x값의 2배가 되도록 설정
x = 10 * np.random.rand(50)
y = 2 * x + np.random.rand(50)
 
# plt.scatter(x, y)  # scatter : 산점도 그리기 (점으로 분포를 나타내는 방법)
# plt.show()

# 1. Scikit-Learn으로부터 적절한 estimator 클래스를 임포트해서 모델의 클래스 선택
from sklearn.linear_model import LinearRegression

# 2. 클래스를 원하는 값으로 인스턴스화해서 모델의 하이퍼파라미터 선택
#       <<인자 값들의 의미>>
#       copy_X : 입력 데이터를 복사해서 사용할 것인가? (Default : True)
#       fit_intercept : 상수 형태의 값을 사용할 것인가? (Default : True)
#       n_jobs : 여러 가지 수행을 병렬적으로 사용할 것인가? (Default : None),
#       n ormalize : 값을 정규화해서 사용할 것인가? (Default : False)
model = LinearRegression(fit_intercept=True)

# 3. 입력 데이터를 특징 배열과 대상 벡터로 배치
#       기존의 배열에 축을 추가함으로써 데이터를 특징 배열로 변환함
X = x[:, np.newaxis]
# print(y)

# 4. 모델 인스턴스의 fit() 메서드를 호출해 모델을 데이터에 적합하도록 함
model.fit(X, y)

# 5. 모델을 새 데이터에 대해서 적용
#       linspace를 이용하여 새로운 데이터를 생성 (np.linspace -> np.linspace(start, stop, num=50 [Default], endpoint=True, retstep=False, dtype=None, axis=0))
#       그 후 특징 벡터로 만든 후 예측까지 진행

xfit = np.linspace(-1, 11)
# 입력 값이기 때문에 특징 벡터로 변환 -> 모델에 넣을 때는 축이 존재하는 형태로 넣어야 하는 듯
Xfit = xfit[:, np.newaxis]
# 훈련된 모델에 test 입력 값을 넣어 예측 값을 저장
yfit = model.predict(Xfit)
# test한 결과 값 확인
print("x: ", xfit, "\n y: ", yfit)

plt.scatter(x, y)
plt.plot(xfit, yfit, '--r')  # Linear Regression 이기 때문에 축을 2개로 설정. '--' : 점선 으로 지정
plt.show()
