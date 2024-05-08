# this directory is created to just save commands. how to run commands

# run all features file under features directory
# behave

# will show print statements also
# behave --no-capture

# will run particular feature file
# behave .\features\ReqresPostParameterization.feature

# runs scenario with tag=smoke
# behave --tags=smoke


# run particular feature file, also runs only scenario with tag=smoke in that feature file
# behave .\features\ReqresPostParameterization.feature --no-capture --tags=smoke

# to run allure reporting. -o is folder where u want to create report. in our case it is AllureReports
# behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports
