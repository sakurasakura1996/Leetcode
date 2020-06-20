class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_pos = 0



    def visit(self, url: str) -> None:
        for i in range(1, len(self.history)-self.cur_pos):
            self.history.pop(-1)
        # self.history.remove(self.history[self.cur_pos+1,len(self.history)])
        self.history.append(url)
        self.cur_pos += 1




    def back(self, steps: int) -> str:
        if steps > self.cur_pos:
            self.cur_pos = 0
        else:
            self.cur_pos -= steps

        return self.history[self.cur_pos]


    def forward(self, steps: int) -> str:
        if self.cur_pos+steps > len(self.history)-1:
            self.cur_pos = len(self.history)-1
        else:
            self.cur_pos += steps
        return self.history[self.cur_pos]


obj = BrowserHistory("leetcode")
obj.visit("google")
obj.visit("facebook")
obj.visit("youtube")
param_1 = obj.back(1)
param_2 = obj.back(1)
param_3 = obj.forward(1)
obj.visit("linked")
param_4 = obj.forward(2)
param_5 = obj.back(2)
param_6 = obj.back(7)
print(param_1,param_2,param_3,param_4,param_5,param_6)