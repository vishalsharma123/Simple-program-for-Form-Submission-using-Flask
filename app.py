import json
import logging
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
import getpass
import requests
from flask import Flask, Blueprint, json, request, render_template, redirect, jsonify, url_for
from flask import make_response
from flask import send_file
from flask import send_from_directory
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

import flask_excel as excel
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from collections import OrderedDict
from flask import Flask, url_for,render_template,request
from flask_ldap3_login import LDAP3LoginManager,AuthenticationResponse
from flask_login import LoginManager, login_user, UserMixin, current_user
from flask import render_template_string, redirect
from flask_ldap3_login.forms import LDAPLoginForm
import os
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from flask_login import LoginManager

# Create and configure app
# [...]





app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
time_info = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# @app.route('/api/token')
# @auth.login_required
# def get_auth_token():
#     token = g.user.generate_auth_token()
#     return jsonify({ 'token': token.decode('ascii') })


import os
import fcntl



@app.route('/', methods=['GET', 'POST'])
def indexPage():



    f = open('hostlist_user.json', 'w')
    converlist = json.dump(request.form, f)

    if request.method == 'GET':
        print("Calling index.html")
        return render_template('/index.html', converlist=converlist )
    else:
        print("Calling submtiData")
        return redirect('/submitData')









@app.route('/submitData')
def my_link():
    # from ress_API.intregated_rest_api.restfullapi.testuser import gitclone_lockfile
    # p1 = gitclone_lockfile()
        k=open("hostlist_user.json","r")
        liver=json.load(k)
        c=(liver['Hostname'])
        lp = (liver['Status'])
        if lp == "OPEN SERVER":
           import subprocess
           print("inside My_link")

           command = 'mkdir {0}'.format(c)

           process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
           output = b''.join(process.stdout).decode('utf-8')
        # with open('/mnt/home/c_vishsh/Desktop/test179/hostlist_user.json', 'w') as f:
        #     json.dump(request.form, f)
           return output
        else:
            import subprocess

            print("inside My_link2")

            command = 'ls'

            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            output1 = b''.join(process.stdout).decode('utf-8')
            # with open('/mnt/home/c_vishsh/Desktop/test179/hostlist_user.json', 'w') as f:
            #     json.dump(request.form, f)
            return output1








if __name__ == "__main__":


    app.run(debug=True,port=5000, threaded=True)




