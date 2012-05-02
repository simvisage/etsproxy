*********
ETS-Proxy
*********

Usage and Functions
-------------------
	With the Release of ETS 4 their was a common change in the Namespaces.
	For an independent development we created the ETS-Proxy, which will
	automatically take the right namespace, dependent on the local working
	ETS version.
	ETS-Proxy is based on the Namespaces of ETS 3, only *enthought.* is now
	changed to *etsproxy.*
	
	e.g.::

		#ETS 3: 		
			from enthought.traits.api import *
		#ETS-Proxy:
			from etsproxy.traits.api import * 

	You can load the etsproxy Repository under this URI to your Eclipse:
		
		https://github.com/simvisage/etsproxy.git
		
	For details on loading a Repository to Eclipse see *Use Github with Eclipse*.
	  	  
	To use ETS-Proxy you have to implement the package *etsproxy* to your project:
	
		- select the project and click right
		- choose Properties>Project References
		- select etsproxy and click OK
	
	ETS-Proxy has only the modules implemented, which are used in Simvisage
	and Oricrete, but it could be easily upgraded_.

New Project with ETS-Proxy
--------------------------
	Create a new project as usual and implement the *etsproxy* package to your
	new project:
	
		- select the project and click right
		- choose Properties>Project References
		- select etsproxy and click OK
		
	Now you can use ETS-Proxy in your project.
	ETS-Proxy is based on the Namespaces of ETS 3, only *enthought.* is now
	changed to *etsproxy.*.
	
	e.g.::

		#ETS 3: 		
			from enthought.traits.api import *
		#ETS-Proxy:
			from etsproxy.traits.api import * 

Convert old projects to ETS-Proxy
---------------------------------
	At first implement ETS-Proxy to your Project.
	
		- select your project and click right
		- choose Properties>Project References
		- select etsproxy and click OK
		
	Now you have to change all old namespaces. With Eclipse you can do this
	easily with the search function:
	
		- select all projects and/or files you want to change
		- click on Search>Search... in the Menubar (Ctrl+H)
		- choose the flag *File Search*
		- type **enthought.** on containing text field (don't forget the dot at the end)
		- under scope choose selected resources
		- now click on the *replace* Button
		- type **etsproxy.** on *With:*-field (don't forget the dot at the end)
		- With OK you change all old namespaces to *etsproxy.*
		
	Now your project is using ETS-Proxy

.. _upgraded:
		
Upgrade ETS-Proxy
-----------------
	If you want to use an ETS Module, which is not implemented in ETS Proxy, 
	you can implement it easily by yourself.
	ETS-Proxy use the same structure as ETS 3, only the *enthought.* namespace is 
	changed to *etsproxy.*
	If you want to add a new modul to ETS-Proxy you have to create a new PyDev Module as <Empty> 
	on the path where the needed module lays. Maybe you have also to create some new PyDev Packages.
	The name for the new PyDev Module is the name of the Module you want to
	load. Now you should have a path like on ETS 3, only with an other namespace.
	Copy the following code to the new Module.::

		#-------------------------------------------------------------------------------
		#
		# Copyright (c) 2012
		# IMB, RWTH Aachen University,
		# ISM, Brno University of Technology
		# All rights reserved.
		#
		# This software is provided without warranty under the terms of the BSD
		# license included in the Spirrid top directory "licence.txt" and may be
		# redistributed only under the conditions described in the aforementioned
		# license.
		#
		# Thanks for using Simvisage open source!
		#
		#-------------------------------------------------------------------------------
	
		# ETS 3
		try:
 		   from enthought.<modul you want to use> import *
		# ETS 4
		except ImportError:
		    from <modul under ETS 4> import *

	Now you have to fill in the correct Importpathes. On # ETS 3 you have
	to choose the path with the old namespace. On # ETS 4 you have to
	choose the Path ETS 4 is now using. 
	**ATTENTION:** ETS 4 has not only be
	reduced by the *enthought* namespace. Some other namespaces where changed too.
	(e.g.: enthought.traits.ui.api => traitsui.api)
	You can look for the new namespaces on this link:
	
		https://github.com/enthought/etsproxy/tree/master/enthought
	
	This is an ETS-Proxy created by Enthought, but it is only bridging till
	your code has finally changed to ETS 4.
	The structure of Enthoughts ETS-Proxy is also oriented on ETS 3 and in every
	Module-File lays the import-path for this module in ETS4.
	