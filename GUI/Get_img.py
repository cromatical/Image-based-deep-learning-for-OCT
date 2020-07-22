from keras.models import load_model
import keras.backend as K
import numpy as np
import cv2
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

def img_crop(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    crop_img = img[:, 500:]
    crop_img = cv2.resize(crop_img, dsize=(299, 299))
    crop_img = crop_img.reshape((1, 299, 299, 3)) / 255
    return crop_img

def h_step1(value):
    heatmap = np.mean(value, axis=-1)  # average
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)
    return heatmap

def h_step2(value, img):
    heatmap = cv2.resize(value, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    Finist = heatmap * 0.3 + img
    return Finist


def Heatmap(model, path):
    crop_img = img_crop(path)
    prediction = model.predict(crop_img)
    y_pred = np.argmax(prediction)
    hypothesis = model.output[:,y_pred]
    Last_conv_Layer = model.get_layer('conv5_block16_2_conv')
    Gradients = K.gradients(hypothesis,Last_conv_Layer.output)[0]#Get y_predic gradi from Last_Layer
    pooled_grad = K.mean(Gradients,axis=(0,1,2))# Get gradients Average
    iterate = K.function([model.input],[pooled_grad,Last_conv_Layer.output[0]]) # Get output
    pooled_grad_value,conv_layer_value=iterate([crop_img]) # input to original image-> get 2 numpy

    for i in range(pooled_grad.shape[0]):
        conv_layer_value[:,:,i] *= pooled_grad_value[i]# important feature square
    heatmap = h_step1(conv_layer_value)
    return prediction, y_pred, heatmap


def get_Heatmap(path, filename, heatmap):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    crop_img = img[:, 500:]
    Finist = h_step2(heatmap, crop_img)
    cv2.imwrite('C:/Medical AI/heatmap list/{}'.format(filename), Finist)
    return "C:/Medical AI/heatmap list/{}".format(filename)


# img = img_crop('C:\Medical AI\image list\Anton_Harisov,_2020_년,_미용_모델,_HD,_사진벽지_1680x1050[10wallpaper.com].jpg')
# # print(img)
# img = cv2.imread(r'C:\Medical AI\image list\test11.jpg', cv2.IMREAD_COLOR)
# print(img)
# crop_img = img[:, 500:]


# model = load_model(r'C:\Medical AI\load model\DenseNet121_allfine_5.h5')
# prediction, y_pred, heatmap = Heatmap(model, r'C:\Medical AI\image list\Anton_Harisov,_2020_년,_미용_모델,_HD,_사진벽지_1680x1050[10wallpaper.com].jpg')
# get_Heatmap(r'C:\Medical AI\image list\Anton_Harisov,_2020_년,_미용_모델,_HD,_사진벽지_1680x1050[10wallpaper.com].jpg', 'aaa.png', heatmap)