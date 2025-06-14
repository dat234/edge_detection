import cv2
import numpy as np

# Đọc ảnh và chuyển sang ảnh xám
image = cv2.imread('D:\download\image (2).png', cv2.IMREAD_GRAYSCALE)

# Bước 1: Làm mượt ảnh bằng bộ lọc Gaussian để giảm nhiễu
blurred_image = cv2.GaussianBlur(image, (5, 5), 1)

# Bước 2: Phát hiện cạnh bằng thuật toán Canny
# Ngưỡng thấp và ngưỡng cao để phân loại các điểm biên
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

# Hiển thị kết quả phát hiện cạnh
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
