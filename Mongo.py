# Copyright 2015 IBM Corp. All Rights Reserved.
#python 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from flask import Flask, render_template,request
from flask.ext.pymongo import PyMongo,ReadPreference


app = Flask(__name__)


# connect to another MongoDB server altogether
app.config['MONGO_HOST'] = 'aws-us-east-1-portal.16.dblayer.com'
app.config['MONGO_PORT'] = 10304
app.config['MONGO_DBNAME'] = 'IDFish'
app.config['MONGO_USERNAME'] = 'vanprz'
app.config['MONGO_PASSWORD'] = 'IBM311342233'
mongo = PyMongo(app, config_prefix='MONGO')



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        m = u+"'"+request.form['phone']+"'"
        r = mongo.db.user.find_one({'phone':m})
	if r != None:
	    if request.form['password']== r[u'password']:
		return redirect(url_for('start'))
	    else:
		error ='Password or Code Invalid'

        else:
            error ='User no Exist '
            
    return render_template('login.html', error=error)

@app.route('/start')
def start():

    return render_template('start.html', error=error)
    


#if __name__ == '__main__':
#    app.run()


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
