import numpy as np
import cv2


# Đọc và resize ảnh
bg1_image = cv2.imread('GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    # Chuyển ảnh về dạng grayscale
    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    input_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

    # Tính sự khác biệt tuyệt đối giữa hai ảnh
    difference = cv2.absdiff(bg_gray, input_gray)

    return difference


def compute_binary_mask(difference_single_channel):
    # Áp dụng ngưỡng để tạo mask nhị phân
    _, binary_mask = cv2.threshold(
        difference_single_channel, 50, 255, cv2.THRESH_BINARY)

    # Mở rộng mask để loại bỏ nhiễu
    kernel = np.ones((5, 5), np.uint8)
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, kernel)

    return binary_mask


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)

    # Tạo ảnh đầu ra với nền mới
    output = np.where(binary_mask[:, :, None] == 255, ob_image, bg2_image)

    return output


output_image = replace_background(bg1_image, bg2_image, ob_image)
# Sử dụng cv2.imshow('Output', output_image) nếu không sử dụng Google Colab
cv2_imshow(output_image)
