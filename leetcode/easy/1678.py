class Solution:
    def interpret(self,command:str)->str:
        return command.replace("()",'o').replace("(al)",'al')


sol=Solution()
print(sol.interpret("G()(al)"))