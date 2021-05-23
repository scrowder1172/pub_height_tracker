Single page application to track heights entered. Submission will return average heights and number of respondents.

Backend: app uses in memory sqlite database by default but includes optional postgres file. Postgres file references
a PATH variable DATABASE_URL which would point to the postgres instance and contain credentials in the connection
string. Another option would be to leverage a database.ini file with the postgres configurations. However, you would 
want to avoid using the same file for all environments or including the file in any publications as credentials could 
be exposed.

As always, any feedback is welcomed. I've added some basic error handling but additional checks should be added based 
off app requirements. 