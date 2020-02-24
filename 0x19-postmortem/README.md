# holberton-system_engineering-devops
## 0x19-postmortem

Document PostMorten

The Holberton page to make the qualification of the projects that are assigned to the students must consume an internal api, which I can use to review each of the criteria defined to qualify the projects of each cohort, but when it is requested to check the page it presents an error with the message "500- Internal Server". The checker was down throughout the day and affection about 300 students from different cohorts.

How to diagnose the problem.

Log in as superuser and execute the command:
ps -fea | grep java

Note: The text "java" is placed, since the checker executable is a java process.

When executing this command it is observed that the application is running correctly, so we discard the idea that the application is down.

You should read the application log, which is in the path "/ etc / jboss / checkcer / log" and the file is called logChecker.log
When reading the log you can find the following error:
.... file system full

Since this error was found, the command must be executed.
df -h FileSystem

It was found that the FileSystem is at 99% and only has 200Kb free and at the moment that it is validating all the checks of a project it is required to store a file that weighs 1MB.

You must go to the root of the FileSystem that presents the space problem and perform an analysis of the possible files to be deleted. Once you find the files that can be debugged, you must execute the command:
rm -rf /fileSystema/.../file.ext

When deleting previously identified files, the command must be re-executed to validate the status of the FileSystem, in order to validate the success of the problem solution. 
