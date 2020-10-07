# enter your code below
from github import Github

g = Github('d128a45067400e6de1b02b3b039917553e581949')

for repo in g.get_user().get_repos():
    print(repo.name)
    
repo = g.get_repo('albertopformoso/datamex_082020')
print(repo)
