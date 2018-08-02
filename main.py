# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
        
class GenerateMeme(webapp2.RequestHandler):
    def get(self):
        meme_template = the_jinja_env.get_template('templates/meme.html')
        variable_text = {
            'tomText':'Me', 
            'jerryText':'The urge to eat', 
            'img_url':'https://i.redd.it/1rm0s5l6uyc11.png'}
        self.response.write(meme_template.render(variable_text))
        
    def post(self):
        results_template = the_jinja_env.get_template('templates/result.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        image_url = self.request.get('meme-type')
        username = self.request.get('username')
        
        the_variable_dict = {'topText': meme_first_line, 'bottomText': meme_second_line, 'img_url': image_url, 'username':username}
        self.response.write(results_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', GenerateMeme)
], debug=True)
