Parser will fetch data for all recordings, look to use SQL for parsing/and viewing. Recommend using SQLITE DB Browser/Viewer for seeing full tables.


For usage instructions:

	readScript.py
		this script will parse out NOAA's full txt file for 			Radiosonde recordings. this is the optimatization 			script, ori_radP is the original script.

	-- BE SURE TO BE WITHIN THE DIR. THAT HOLDS THE 			NECESSARY TEXT FILE.

	TO CHANGE INTO THE DIRECTORY:
	(ADD THIS PYTHONIC CODE TO LINE 4)

		OS.CHDIR('path_specifying_directory')


	-- run the scripts, database will hold data regardless if 		fully complete, can check by running sql commands when in 		DB.
	-- if certain breaks occur during writing
	delete old --journal file & delete database name
	to find database name see line 7, can also modify name


	ori_radP.py
		this script is the original parser, its works better 			readScript.py, for the fact that a user can manually 			set the dates (YEAR, MONTH, DAY) while python runs 			the code.
	
	-- FOLLOW THE STEPS LISTED ABOVE FOR TROUBLESHOOTING.
	-- CRITICAL EVERYTHING IS HELD IN ONE LOCATION.



	readClass.py
		this class follows readClass.py logic, except there 			is no push to a SQLITE Database.
	
	-- FOLLOW THE STEPS LISTED ABOVE FOR TROUBLESHOOTING.
	-- CRITICAL EVERYTHING IS HELD IN ONE LOCATION.