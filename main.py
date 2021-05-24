from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from wtforms.validators import InputRequired, Length, NumberRange
import types
from typing import cast
import inspect

from height_tracker import HeightTracker

app = Flask(__name__)


class HeightTrackerPage(MethodView):

    def get(self):
        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")
        height_tracker_form = HeightTrackerForm()
        return render_template('height_tracker.html', height_tracker_form_html=height_tracker_form)

    def post(self):
        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")
        height_tracker_form = HeightTrackerForm(request.form)
        height_tracker = HeightTracker()
        result = height_tracker.add_height(name=height_tracker_form.name.data,
                                           height=height_tracker_form.height.data)
        if result:
            return render_template('height_tracker.html',
                                   height_tracker_form_html=height_tracker_form,
                                   average_height=height_tracker.average_height(),
                                   respondents=height_tracker.count_of_respondents(),
                                   error_message="",
                                   result=True)
        else:
            return render_template('height_tracker.html',
                                   height_tracker_form_html=height_tracker_form,
                                   average_height="",
                                   respondents="",
                                   error_message="An error occurred adding your height. Please try again later.",
                                   result=True)


class HeightTrackerForm(Form):
    """Bug: Length and NumberRange do not seem to working at the moment. Based off recent web searches, I may
    have to modify these lines slightly.
    """
    name = StringField("Name: ", validators=[InputRequired(), Length(min=2, max=50, message="Length out of range")])
    height = StringField("Height (inches): ",
                         validators=[InputRequired(),
                                     NumberRange(min=15, max=96, message="Number out of range")])
    button = SubmitField("Add Entry")


app.add_url_rule('/', view_func=HeightTrackerPage.as_view('height_tracker'))

if __name__ == '__main__':
    app.run()
