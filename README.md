<p>Single page application to track heights entered. Submission will return average heights and number of 
respondents.</p>

<p>Concept: https://www.udemy.com/course/the-python-mega-course/</p>
<p>database.ini file example: https://www.postgresqltutorial.com/postgresql-python/connect/</p>
<p>HTML source: https://www.w3schools.com/html/html_responsive.asp</p>

<p>Backend: local sqlite database</p>

<p>Optional postgres sql file included. Postgres implementation will require small changes to height_tracker.py due to 
the differences in how sqlite and postgres handle parameters. Additionally, the postgres file references a PATH 
variable DATABASE_URL which would point to the postgres instance and could contain credentials in the connection 
string. Another option would be to leverage a database.ini file with the postgres configurations. However, care should 
be taken to avoid using the same file across multiple environments or publishing the file as it could contain 
credentials.</p>

<p>Method check: the two lines below can be used during debugging to check where the code is
during execution.
<br>Source: https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string

        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")</p>

<p>As always, any feedback is welcomed. I've added some basic error handling but additional checks should be added based 
off app requirements.</p> 