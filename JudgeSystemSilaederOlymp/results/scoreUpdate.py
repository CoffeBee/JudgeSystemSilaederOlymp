import random
import threading
import time
import hashlib
import requests
from .codeforcesApi import call
from .models import CTFScore, MathScore, ProgScore
from programming.models import ProgrammingSubmits
import sys
import json

class ScoreUpdate():
    def __init__(self, CTFstdScore, MathstdScore, ProgstdScore, CTFstdPlusser, MathstdPlusser, ProgstdPlusser, apiKey, apiSecret, contestId):
        self.CTFstdScore = CTFstdScore
        self.MathstdScore = MathstdScore
        self.ProgstdScore = ProgstdScore
        self.CTFstdPlusser = CTFstdPlusser
        self.MathstdPlusser = MathstdPlusser
        self.ProgstdPlusser = ProgstdPlusser
        self.lastSubmitId = 1
        self.contestId = contestId
        self.apiKey = apiKey
        self.apiSecret = apiSecret

    def setToStd(self):
        for i in CTFScore.objects.all():
            i.score = self.CTFstdScore
            i.pluser =  self.CTFstdPlusser

        for i in MathScore.objects.all():
            i.score = self.MathstdScore
            i.pluser = self.MathstdPlusser

        for i in ProgScore.objects.all():
            i.score = self.ProgstdScore
            i.pluser = self.ProgstdPlusser

    def startMonitor(self, timeInterval, lastSubmitId, contestId):
        self.MonitorThread = threading.Thread(target=self.Monitor, args=(timeInterval, lastSubmitId, contestId,))
        self.MonitorThread.run()

    def Update(self):
        self.UpdateProg()
        self.UpdateMath()
        self.UpdateCTF()

    def UpdateProg(self):
        print("fuck")

        newSubmits = call('contest.status', lastSubmit=self.lastSubmitId, key=self.apiKey, secret=self.apiSecret, contestId=self.contestId)

        if (newSubmits == "Codeforces Api error"):
            sys.exit('Codeforces Api error')
        else:
            print(newSubmits)
            self.lastSubmitId += len(newSubmits)

            for submit in newSubmits:
                print(json.dumps(submit, indent=4, sort_keys=True))



    def UpdateMath(self):
        """
        for i in MathScore.objects.all():
            i.score += i.pluser
        """

    def UpdateCTF(self):
        """
        for i in MathScore.objects.all():
            i.score += i.pluser
        """

