class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #let us create a hashmap first
        email_to_account=defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email_to_account[accounts[i][j]].append(i)
        print(email_to_account)
        
        seen=set()
        
        def dfs(i,set_of_emails):
            # print(i,set_of_emails)
            # print(seen)
            if i in seen:
                return 
            seen.add(i)
            for j in range(1,len(accounts[i])):
                
                # print(i,accounts[i][j])
                set_of_emails.add(accounts[i][j])
                for nei in email_to_account[accounts[i][j]]:
                    dfs(nei,set_of_emails)
            return set_of_emails
            
        
        res=[]
        for ind,emails in enumerate(accounts):
            if ind in seen:
                continue
            # print('------',ind)
            
            sorted_emails=sorted(list(dfs(ind,set())))
            res.append([emails[0]]+sorted_emails)
        # print(res)
        return res
            
        