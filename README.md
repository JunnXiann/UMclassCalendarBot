PROJECT: UMclassCalendarBot

===============================================================================================================
DESCRIPTION:
===============================================================================================================
This is an automation bot that scrapes class data from a MAYA account (University Malaya's student portal)
and create an ICS file that automatically add them as events into a calendar app.

For now this is only mac-friendly and the chromedriver may differ due to different versions of chrome browser, 
and this may cause the bot to experience failure when trying to use python selenium to scrape data.

===============================================================================================================
HOW TO USE:
===============================================================================================================
1. In terminal, go to the directory where you've cloned the project
2. Run pip install requirements.txt
3. Run the Scraper.py file
4. Enter your MAYA credentials
3. Click on the ICS file created by the bot (should be at desktop)
4. Your calendar app should be prompted, alter your customized settings that is necessary.

