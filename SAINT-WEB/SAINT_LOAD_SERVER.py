# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
from tensorflow.python.keras.models import load_model
import tensorflow as tf
import numpy as np
import cv2
from keras.preprocessing import image
from tensorflow.python.keras.backend import set_session
import keras.backend as K
import os
import time

tf_config =  os.environ.get('TF_CONFIG')
sess = tf.Session(config=tf_config)
graph = tf.get_default_graph()
set_session(sess)
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	if request.method=='GET':

		return render_template('donghwi.html')
	if request.method=='POST':
		real = time.strftime('%m-%d', time.localtime(time.time()))
		file = request.files['image_uploads']
		hit=float(request.form['heat'])
		files = '{}'.format(file)
		l = []
		m = []
		for i in range(len(files)):
			l.append(files[i])
			for j in range(len(l)):
				if l[j] == '\'':
					aa = l.index('\'')
					l.remove('\'')
					m.append(aa)
				elif l[j] == '.':
					bb = l.index('.')
					l.remove('.')
					m.append(bb)
		original_name = files[m[0] + 1:m[1] + 1]
		print(original_name)
		original_Image=real+original_name+'.jpg'
		img = image.load_img(file, target_size=(model.input.shape[1], model.input.shape[2]))
		img = np.array(img)
		asdf=os.getcwd()
		cv2.imwrite(asdf+'/static/save_img/{}'.format(original_Image), img)
		original_Path='/static/save_img/'+original_Image
		img_tensor = img.reshape((1, model.input.shape[1], model.input.shape[2], 3))
		img_tensor = img_tensor / 255
		global sess
		global graph
		with graph.as_default():
			set_session(sess)
			prediction = model.predict(img_tensor)

		y_pred = np.argmax(prediction)  # Get_Image_Predic
		hypothesis = model.output[:, y_pred]
		Last_conv_Layer = model.get_layer('conv5_block16_2_conv')  # Get Last Layer
		Gradients = K.gradients(hypothesis, Last_conv_Layer.output)[0]  # Get y_predic gradi from Last_Layer
		pooled_grad = K.mean(Gradients, axis=(0, 1, 2))  # Get gradients Average
		with graph.as_default():
			set_session(sess)
			iterate = K.function([model.input], [pooled_grad, Last_conv_Layer.output[0]])  # Get output
			pooled_grad_value, conv_layer_value = iterate([img_tensor])  # input to original image-> get 2 numpy
		for i in range(pooled_grad.shape[0]):
			conv_layer_value[:, :, i] *= pooled_grad_value[i]  # important feature square
		heatmap = np.mean(conv_layer_value, axis=-1)  # average
		heatmap = np.maximum(heatmap, 0)
		heatmap /= np.max(heatmap)

		imag = image.load_img(file, target_size=(model.input.shape[1], model.input.shape[2]))
		imag=np.array(imag)
		heatmap = cv2.resize(heatmap, (imag.shape[1], imag.shape[0]))

		heatmap = np.uint8(255 * heatmap)
		heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
		Finist = heatmap * hit + imag
		heat_name='Heat'+real+original_Image

		heat_path='/static/save_img/'+heat_name

		cv2.imwrite(asdf+'/static/save_img/{}'.format(heat_name), Finist)

		if y_pred==0:
			result='CNV'
		elif y_pred==1:
			result='DME'
		elif y_pred==2:
			result='DRUSEN'
		elif y_pred==3:
			result='NORMAL'
		cnv=round(prediction[0][0],4)
		dme=round(prediction[0][1],4)
		dru=round(prediction[0][2],4)
		nor=round(prediction[0][3],4)
		return render_template('donghwi.html',send=heat_path,gor=original_Path,price=result,cnv=cnv,dme=dme,dru=dru,nor=nor)
if __name__=='__main__':
	graph = tf.get_default_graph()
	model = load_model('DenseNet121_allfine_5')
	# model = keras.models.load_model()  # DenseNet121_allfine_5
	app.run(debug=False)

