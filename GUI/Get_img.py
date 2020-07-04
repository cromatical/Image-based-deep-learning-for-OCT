from keras.models import load_model
from keras.preprocessing import image
import keras.backend as K
import numpy as np
import cv2
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

def image_processing(model, path):
    img = image.load_img(path, target_size=(model.input.shape[1], model.input.shape[2]))
    img = np.array(img)
    img_tensor = img.reshape((1, model.input.shape[1], model.input.shape[2], 3))
    img_tensor = img_tensor / 255
    return img_tensor


def Heatmap(model, path):
    img_tensor = image_processing(model, path)
    prediction = model.predict(img_tensor)
    y_pred = np.argmax(prediction)
    hypothesis = model.output[:,y_pred]
    Last_conv_Layer = model.get_layer('conv5_block16_2_conv')
    Gradients = K.gradients(hypothesis,Last_conv_Layer.output)[0]#Get y_predic gradi from Last_Layer
    pooled_grad = K.mean(Gradients,axis=(0,1,2))# Get gradients Average
    iterate = K.function([model.input],[pooled_grad,Last_conv_Layer.output[0]]) # Get output
    pooled_grad_value,conv_layer_value=iterate([img_tensor]) # input to original image-> get 2 numpy

    for i in range(pooled_grad.shape[0]):
        conv_layer_value[:,:,i] *= pooled_grad_value[i]# important feature square

    heatmap = np.mean(conv_layer_value,axis=-1) #average
    heatmap = np.maximum(heatmap,0)
    heatmap /= np.max(heatmap)
    return prediction, y_pred, heatmap


def get_Heatmap(path, filename, heatmap):
    img = cv2.imread(path)
    heatmap = cv2.resize(heatmap, (img.shape[1], img.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    Finist = heatmap * 0.3 + img
    cv2.imwrite('C:/Medical AI/heatmap list/{}'.format(filename), Finist)
    return "C:/Medical AI/heatmap list/{}".format(filename)

# if __name__=='__main__':

#     model = load_model('C:/Users/croma/Desktop/DenseNet121_allfine_5.h5')
#     path = 'C:/Users/croma/Desktop/fold/apple.png'
#     filename = 'aaa.png'

#     prediction, y_pred, heatmap = Heatmap(model, path)
#     heatmap_path = get_Heatmap(path, filename, heatmap)