# log
## Project overview
- In this project, we will write some reporting tool inside a python code which fetches our required information from a given sql file.
## PreRequisites
- python 3
- vagrant
- virtual box
## set up
- Install Vagrant and VirtualBox
- Download the database setup: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
- Unzip the downloaded file after downloading it. The file inside is called newsdata.sql.
- Dump the data inside the sql file into our news database.
## Launching the virtual machine
- First, type the command "vagrant up"
- Next, type "vagrant ssh"
- The above command will log you into the virtual box.
- Change the directory to /vagrant.
- Dump the data from sql file into our database using "psql -d news -f newsdata.sql" command.
- Write a python file which includes reporting tools to fetch our required data.
- Run the python file using "python filename.py" command.
