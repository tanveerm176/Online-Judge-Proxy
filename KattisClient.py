
import submit 
import sys

#define class to handle kattis login
class KattisClient:

    # studentConfig : configparser = get_config()


    def __init__(self) -> None:
        #store student username, token at the init of class
        self.studentConfig = submit.get_config()
        self.token = self.studentConfig.get("user", "token")
        self.userName = self.studentConfig.get("user", "username")
        self.hostName = self.studentConfig.get("kattis", "hostname")
        self.loginUrl = self.studentConfig.get("kattis", "loginurl")
        self.singleSubmissionUrl = self.studentConfig.get("kattis", "submissionurl")
        self.multiSubmissionUrl = self.studentConfig.get("kattis", "submissionsurl")
        self.cookies = self.__getCookies()

    def __getCookies(self):
        #get cookies form successful login to be used in submission
        response = submit.login_from_config(self.studentConfig)

        # if err != None:
        #     print(err)
        #     raise SystemExit(1)
        
        return response.cookies
