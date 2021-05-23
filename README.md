Single page application to track heights entered. Submission will return average heights and number of respondents.

Backend: "in memory" sqlite database
Optional postgres file included. Small changes to height_tracker.py will be required due to the differences in how 
sqlite and postgres handle parameters. Additionally, the postgres file references a PATH variable DATABASE_URL which 
would point to the postgres instance and could contain credentials in the connection string. Another option would be to 
leverage a database.ini file with the postgres configurations. However, care should be taken to avoid using the same
file across multiple environments or publishing the file as it could contain credentials.

As always, any feedback is welcomed. I've added some basic error handling but additional checks should be added based 
off app requirements. 