# **Apple MachineLearning Guide**

---
# Index
   1. Core ML 2
   2. 计算机视觉-Vision
   3. 自然语言处理-Natural Language
   4. Create ML
   5. 其他
---- 

1. Core ML 2 - 如何集成机器学习的模型到你的app [Introduction][1]

	 1. 通过Python的第三方框架训练你的模型
		* 超过30层的DeepLearning的神经网络模型
		* 决策树聚合-tree ensembles
		* 支持向量机-SVMs
		* 广义线性模型 - generalized linear models

	 2. 使用转化工具
		1. 官方工具 [Core ML Tools][2] 以及支持的类似[ 表格][3]
		2. Apache MXNet[MXNet converter][4]
		3. TensorFlow[ TensorFlow converte][5]
		4. ONNX [Get ONNX model converter][6]
		5. 创建自定义的转化工具 [Core ML Model Specification.][7]

	 3. 集成进你的app并使用该模型
		* 使用第一步训练好的模型通过第二步转化成CoreML类型的模型文件
		* 或者直接使用已经训练好并转化好的模型
		   * 识别超过1000种类别图片的轻量级卷积神经网络模型[MobileNet][8] 和[使用简介][9]
		   * 仅仅5M大小的可识别1000中类别图片的模型[SqueezeNet][10] 和 [使用简介][11]
		   * 识别超过205种类似飞机场出口，卧室，森林，海岸线等的模型[Places205-GoogLeNet][12]  和[使用简介][13]
		   * 识别超过1000种类别图片的模型[ResNet50][14] 和 [使用简介][15]
		   * 识别超过1000种类别图片的模型[Inception v3][16]  和[使用简介][17]
		   * 识别超过1000种类别图片的模型[VGG16][18] 和 [使用简介][19]

	 4. 代码示例
		1. 模型集成 [demo][20]
		2. 使用Vision处理，Core ML图片识别 [demo][21]

	 5. App-size 体积管理 [Management Reducing the Size of Your Core ML App][22]
	 6. Core ML 2 API Refrence [Core ML API][23]

2. 苹果计算机视觉框架-Vision(beta)
   1.  Vision框架的功能介绍 [link][24]
   2.  使用Vision框架实时识别的ARKit [demo][25]

3. 苹果自然语言处理框架-Natural Language(beta)
   1. 使用Natural Language框架和[Create ML][26] 来自定义NLP的模型

4. 苹果的Create ML框架
   1. [Create ML][27]

5. 其他

	[苹果 ML 首页][28]

	[苹果ML工程师博客][29]


[1]:	https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml
[2]:	https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml
[3]:	https://developer.apple.com/documentation/coreml/converting_trained_models_to_core_ml#2953557
[4]:	https://github.com/apache/incubator-mxnet/tree/master/tools/coreml
[5]:	https://github.com/tf-coreml/tf-coreml
[6]:	https://github.com/onnx/onnx-coreml
[7]:	https://apple.github.io/coremltools/coremlspecification/
[8]:	https://docs-assets.developer.apple.com/coreml/models/MobileNet.mlmodel
[9]:	https://developer.apple.com/machine-learning/model-details/MobileNet.txt
[10]:	https://docs-assets.developer.apple.com/coreml/models/SqueezeNet.mlmodel
[11]:	https://developer.apple.com/machine-learning/model-details/SqueezeNet.txt
[12]:	https://docs-assets.developer.apple.com/coreml/models/GoogLeNetPlaces.mlmodel
[13]:	https://developer.apple.com/machine-learning/model-details/Places205-GoogLeNet.txt
[14]:	https://docs-assets.developer.apple.com/coreml/models/Resnet50.mlmodel
[15]:	https://developer.apple.com/machine-learning/model-details/ResNet50.txt
[16]:	https://docs-assets.developer.apple.com/coreml/models/Inceptionv3.mlmodel
[17]:	https://developer.apple.com/machine-learning/model-details/ResNet50.txt
[18]:	https://docs-assets.developer.apple.com/coreml/models/VGG16.mlmodel
[19]:	https://developer.apple.com/machine-learning/model-details/VGG16.txt
[20]:	https://docs-assets.developer.apple.com/published/83f5575193/IntegratingACoreMLModelIntoYourApp.zip
[21]:	https://developer.apple.com/documentation/vision/classifying_images_with_vision_and_core_ml
[22]:	https://developer.apple.com/documentation/coreml/reducing_the_size_of_your_core_ml_app
[23]:	https://developer.apple.com/documentation/coreml/core_ml_api
[24]:	https://developer.apple.com/documentation/vision
[25]:	https://docs-assets.developer.apple.com/published/7da9756a21/UsingVisionInRealTimeWithARKit.zip
[26]:	https://developer.apple.com/documentation/create_ml
[27]:	https://developer.apple.com/documentation/create_ml
[28]:	https://developer.apple.com/machine-learning/
[29]:	https://machinelearning.apple.com