***********************
Use Github with Eclipse
***********************

Install required Eclipse Plugins:
---------------------------------

  To get Eclipse running with Github.com, you have to add two plugins:
  
    - PyDev (Handles the Python Syntax)
    - EGit  (Handles the github.com Repositories)

Install  PyDev Plugin
=====================
  
    * Open Eclipse
    * click Help>Install new Software
    * copy the following link to the *Work with* textbox and press enter
			http://pydev.org/updates
    * now their are all available Plugins displayed, choose only **PyDev** and press next
    * Install wizard should guide you through the Installation

Install EGit Plugin
===================
  
    * click Help>Install new Software
    * copy the following link to the *Work With* textbox and press enter
			http://download.eclipse.org/egit/updates 
    * now their are all available Plugins displayed, under *Eclipse Git Team Provider*
      choose all, **without EGit Mylyn** and **don't** choose **JGit**
    * Install wizard should guide you through the Installation

Initialize an existing repository:
----------------------------------

  At first you have to register on github.com . If you want to make changes on an Repository
  you have to be added as collaborator by an Admin.

Get an existing Repository
==========================
  
    * Find out the Repository Path:
    
      - go on github.com, login, search for the Repository you need and choose it
      - if you have clicked on the Repository you'll see a link in the middle
      - left of this link you can choose HTTP, click this Button and copy the link 
      	(this is the URI of this Repository)
      
    * open Eclipse and go to PyDev (Window>"Open Perspective">Other>PyDev)
    * right click in *PyDev Package Explorer* click and then click *Import*
    * choose Git>"Projects from Git">URI
    * copy the link of your Repository to the URI textbox (EGit will autocatch it, if it is in the buffer)
    * EGit should now have everything filled in but one left, your github password. Enter it and press next
    * Now you should choose the branches you need (default is master Branch), press next
    * next window wants a directory for the repository, let it all on default, press next
    * Import existing Projects, press next
    * select all Projects you need and press finish

Create a new repository:
------------------------

  You could also create an own repository like a scratch on your own github account.

  * open www.github.com, login your account, click on your name
  * click *New repository* Button, fill in all asked Information and click *create repository*
  
  Now you have your own repository on github.com . To reach this repository you need the URI.
  They have all the same scheme:
  
    	https://github.com/<Username>/<Repositoryname>.git
    	
  As long as theirs no project existing in the repository you can't load it to Eclipse via Import!

Import new empty repository to Eclipse:
=======================================

    * Open Eclipse and go to *Git Repository Explorer*
    * right click in this Explorer and choose *Paste Repository Path or URI*
    * put in the URI of your new Repository from above and type in your github username and password
    * press Next, Next and Finish
    
Create a new Project for the new Repository
===========================================

  	* Open PyDev view on Eclipse and click File>New>Project>PyDev Project, and create a new Project
  	* on the *PyDev Package Explorer*, right click on the new Project Team>"Share Project"
  	* select Git and click next
  	* on *Repository:* choose the Repository we created on github.com and load to *Git Repositrory Explorer*
  	* select the Project and click Finish
  	
Upload your new Project to Github.com
=====================================

  	* right click the new Project and choose Team>Commit and commit window will open
    * enter your commit message (e.g. Initialize new Project) and select all files to commit
    * you should also check whether you are selected as committer, then press Commit
    * right click the new Project and choose Team>Push to Upstream
    * you'll get a confirmation of your uploads




Usage of Github.com Repositories:
---------------------------------

Commit:
=======
  
    If you have changed some files in your repository and want to upload them, you first have
    to commit them. Committing is only local. For an upload to the github server you have
    also to make a push to upstream
    
    * right click the Project and choose Team>Commit, commit window will open
    * enter your commit message and select all files which should be committed
    * you should also check whether you are selected as committer, then press Commit

Push to Upstream:
=================
  
    To upload your commits on the github server, you have to push them to upstream.

    * right click the Project and choose Team>Push to Upstream
    * you'll get a confirmation of your uploads

