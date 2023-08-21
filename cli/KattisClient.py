
from . import submit 
import sys
from requests import cookies
import os

#define class to handle kattis login
class KattisClient:

    def __init__(self) -> None:
        self.studentConfig = submit.get_config()
        self.token = self.studentConfig.get("user", "token")
        self.userName = self.studentConfig.get("user", "username")
        self.hostName = self.studentConfig.get("kattis", "hostname")
        self.loginUrl = self.studentConfig.get("kattis", "loginurl")
        self.singleSubmissionUrl = self.studentConfig.get("kattis", "submissionurl")
        self.multiSubmissionUrl = self.studentConfig.get("kattis", "submissionsurl")
        self.cookies = self.__getCookies()

    #get cookies form successful login to be used in submission
    def __getCookies(self) -> cookies:
        response = submit.login_from_config(self.studentConfig)
        
        return response.cookies

    def get_problem_id(self, files) -> str:
        problemID, ext = os.path.splitext(os.path.basename(files[0]))

        file_language = submit.guess_language(ext, files=files)
        file_mainclass = submit.guess_mainclass(file_language, files)

        problemID = problemID.lower()

        return problemID
    
    #TODO: remove language param from submit_problem and set language default in submit functions
    #TODO: implement problem exists check?
    def submit_problem(self, problemID, files, language = "Python 3"):

        submit.confirm_or_die(problem=problemID, language=language, files=files, mainclass='', tag='')

        result = submit.submit(submit_url=self.singleSubmissionUrl, cookies=self.cookies, problem=problemID, 
                      files=files, language=language)
    
        plain_result = result.content.decode('utf-8').replace('<br />', '\n')

        submission_url = submit.get_submission_url(plain_result, self.studentConfig)
        if submission_url == None:
            sys.exit("Problem Not Found")
        
        print(f"Submission URL: {submission_url}")
    
        judgement=submit.show_judgement(submission_url, self.studentConfig)
        
        return

