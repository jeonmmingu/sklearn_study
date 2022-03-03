# xlim(), ylim(), axis() method를 사용하여 X, Y축이 표시되는 범위를 지정할 수 있다.
import matplotlib.pyplot as plt

# [1] Basic Usage
# X,Y축의 범위 설정 / list 또는 tuple의 형태로 입력하면 됨
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xlim([0, 5])      # X축의 범위: [xmin, xmax]
plt.ylim([0, 20])     # Y축의 범위: [ymin, ymax]
plt.show()


# [2] Option Setting
# 'on' | 'off' | 'equal' | 'scaled' | 'tight' | 'auto' | 'normal' | 'image' | 'square' 옵션이 존재한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis('square')
# plt.axis('scaled')
plt.show()


# [3] Get the ranges of Axis
# xlim(), ylim() 함수는 그래프 영역에 표시되는 X축, Y축의 범위를 각각 반환한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# 축 별로 범위를 얻은 후 출력
x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)
# 그래프 상에서 한번에 얻은 후 출력
axis_range = plt.axis('scaled')
print(axis_range)
plt.show()