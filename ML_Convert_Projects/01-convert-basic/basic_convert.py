import coremltools
from sklearn.linear_model import LinearRegression
import pandas as pd

print(' ')
print('*********************  sckit-learn model convert .mlmodel  *********************')
print(' ')

# 1 load data
data = pd.read_csv('housing.csv')

# 2 train a model
model = LinearRegression()
model.fit(data[['RM','LSTAT','PTRATIO']],data['MEDV'])

# convert and save the scikit-learn model
coreml_model = coremltools.converters.sklearn.convert(model,['RM','LSTAT','PTRATIO'],'MEDV')
coreml_model.save('HousePricer.mlmodel')





print(' ')
print('*********************  caffe model convert  *********************')
print(' ')

# step1--my_caffe_model.caffemodel 这里的 .caffemodel格式的模型文件，是先使用caffe框架训练出来的保存的，
# step2--使用coremltools。converters里面对应的框架来转化成coreml格式的model
# step3--保存成 modelname.mlmodel的格式，然后就可以拖到Xcode里面直接使用了

# coreml_model = coremltools.converters.caffe.convert('my_caffe_model.caffemodel')
# coremltools.utils.save_spec(coreml_model,'my_model.mlmodel')


