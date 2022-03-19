from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
'''
set FLASK_APP=run.py
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
set FLASK_DEBUG=1
flask run


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zgyrldjf:ngcUoDi8jpQyKMP8I5QHBTRK16ja6pfy@castor.db.elephantsql.com/zgyrldjf'

db = SQLAlchemy(app)

db.init_app(app)
db.Model.metadata.reflect(db.engine)
migrate = Migrate(app, db)
'''
def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET','POST'])
    def make_prediction():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':
            # 인코더 정의
            import pandas as pd
            from category_encoders import OrdinalEncoder
            from sklearn.preprocessing import LabelEncoder
            from imblearn.over_sampling import SMOTE
            from lightgbm import LGBMClassifier
            import lightgbm as lgb
            import warnings
            warnings.simplefilter(action='ignore', category=FutureWarning)

            df = pd.read_csv("/Users/dabbi/Section3/project3/flask_app/datacsv.csv")
            df_m = df[['category_dic','rev','rating','sub']]
            X = df_m.drop(columns=['sub'])
            y = df_m['sub']
            
            # smote오버샘플링을 위한 전처리
            encoder = OrdinalEncoder()
            le = LabelEncoder()

            X_encoded = encoder.fit_transform(X)
            le.fit(y)
            y_encoded= le.transform(y)

            smote = SMOTE(random_state=0)
            X_over, y_over = smote.fit_resample(X_encoded, y_encoded)
            
            
            model = LGBMClassifier(random_state=2
                        , n_jobs=-1
                        , learning_rate=0.2
                        , boost_from_average=False
                        )
            model.fit(X_over, y_over)

            # 벨류값 가져오기.

            category_dic = request.form.get('category_dic')
            rev = request.form.get('rev')
            rating = request.form.get('rating',type=int, default=None)
           

            final_features = pd.DataFrame({"category_dic":[category_dic],"rev":[rev],"rating":[rating]})
            
            X_pred = encoder.transform(final_features) 
            fitt = le.inverse_transform(model.predict(X_pred))

            return render_template('index.html', fitt = fitt)
    
    @app.route('/list', methods = ['GET', 'POST'])
    def list_result():
       import pandas as pd
       import folium
       from folium.plugins import MarkerCluster
       df = pd.read_csv("/Users/dabbi/Section3/project3/flask_app/datacsv.csv")
       sub_name='광화문역'
       

       if sub_name is None:
            return "이름을 입력하세요", 400


       else:
        # 음식점 지도 생성
            df = df[df['sub'] == sub_name]

            map = folium.Map(location=[37.541, 126.986], zoom_start=12)
            marker_cluster = MarkerCluster().add_to(map)

            for index, a in df.iterrows():
                if float(a["rating"]) >= 4:#평점 4점 이상 빨간색
                    color = "red"

                elif float(a["rating"]) >= 3:#평점 3점 이상 주황색
                    color = "orange"

                else:#평점 3점 미만
                    color = "lightgreen"

                print_popup = str(a["name"]) + "<br> 카테고리 : " + str(a["category"]) + "<br> 평점 : " + str(a["rating"]) + \
                              " <br> 리뷰수 : " + str(a["rev"]) + "<br> 주소 : " + str(a["add"]) + "<br>" + '<a href="' + str(a["link"]) + '" target="_self">' + str(a["link"]) + '</a>'

                folium.Marker(location=[a["lat"], a["lng"]],
                              popup=print_popup, icon=folium.Icon(color=color)).add_to(marker_cluster)
            map.save('/Users/dabbi/Section3/project3/flask_app/templates/map.html')
            return render_template('map.html')

    return app




if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)