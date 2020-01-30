
from locust import HttpLocust,between,TaskSet,task

class Recommend_keywords(TaskSet):

    @task(1)
    def get_recommend_keywords(self):
        header=dict(
            cookie = ''
        )
        resp = self.client.get(
            '',
            params = dict(dimension='desc',
            words='运动,音乐'
            ),
            headers=header
        )
        print('success') if resp.status_code == 200 else print('fails')
    
class WebsiteUser(HttpLocust):
    task_set = Recommend_keywords
    wait_time=between(3,5)

if __name__ == "__mian__":
    'locust -f file.py --no-web -c 1 -r 1 --run-time 10s --host=http:..'