# Git Project Automation
<img align = "right" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width = 100px></img>
Get started on your project with just 1 command

Here, I create a <b>shell script</b> and a <b>python script</b> for my terminal that will automate the process of creating new projects for me.
I created a custom command that
  1. creates a folder
  2. adds it to my desired directory
  3. Creates a new repository in my GitHub
  4. Adds the git remote to my local folder-
  5. Adds a README file
  6. Does `git add .`
  7. Makes an “Initial commit” and then pushes this to master.

Finally it opens the project folder in vs code.

### Install:

```
git clone https://github.com/saugaatallabadi/New-Project-Automation.git
cd New-Project-Automation
```

Then go to create.py and set the `username` and `password` to be your username and password.
Also make sure to change all directories to your directories so it should be '/Users/\<your username>/path/to/your/project'

```
cp create.py ~/
cp .my_commands.sh ~/
source ~/.my_commands.sh
```
  
### Usage:

To run the script type in 'create \<name of your folder>'
  
Please 🌟 the project and share it with your developer friends!
  
The inspiration for the project comes from [Kalle Hallden](https://github.com/KalleHallden/ProjectInitializationAutomation). I have instead used Github APIs instead of Selenium for web scrapping for a much better performance and scalability.
