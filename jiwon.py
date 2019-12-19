from classification_util import ClassificationUtil as cfu
from prediction_util import PredictionUtil as pu
from sensor_util import MyClassifier as su
import pandas as pd

gildong = pu()
gildong.read('jejuvisit2.csv')
gildong.show_unique_column()

gildong.df = pd.get_dummies(gildong.df)

#gildong.lmplot('date','visit','holiday')
#gildong.boxplot('day','visit')
#gildong.plot_3d('date','holiday','visit')
#gildong.heatmap(['date','holiday','visit'])
gildong.run_all(['date'],'visit')