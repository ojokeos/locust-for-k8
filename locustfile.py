from wsgiref import headers
from locust import between, task, FastHttpUser
import json


class WebsiteUser(FastHttpUser):
    wait_time = between(5, 15)
# http://5.161.66.169/
# http://5.161.161.219:9000
    @task
    def on_start(self):
        self.client.get("http://google.com")

        # self.client.post(
        #     "/workload-test/public/default/debug-msg", 
        #     # "/webhook/test/public/default/debug-msg?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9qb3hkYW5AZ21haWwuY29tIiwicm9sZSI6InVzZXIiLCJpZCI6IjY0ZDdkMDMwMGQ3ODljZmEyYzAxY2NkOSIsImlhdCI6MTY5MzIxODE3Mn0.YtszjWjeKuv5xvJ_pa3EnTVOuGuiP1hIXCErAcIUS9s", 
        #     # "/encrypt", 
        #                  data=json.dumps({
        # "subject": "now",
        # "content_type": "plain",
        # "body": "hello sms for you.",
        # "recipients": [
        #     {
        #     "uuid": "a9378c73-87e1-4020-99e7-ca2dc1820482",
        #     "email": "john@example.com",
        #     "name": "John Doe",
        #     "attribs": {
        #         "phone": "573046660189"
        #     },
        #     "status": "enabled"
        #     }
        # ],
        # "campaign": {
        #     "from_email": "listmonk <noreply@listmonk.yoursite.com>",
        #     "uuid": "40a1b2d8-f3e9-4e42-8dc4-a6b57aaafdd8",
        #     "name": "sms",
        #     "headers": [],
        #     "tags": None
        # },
        # "extra_detail": {
        #     "template_image_url": "",
        #     "type_of_file": "",
        #     "status": "",
        #     "tenant_id": 0,
        #     "cost_center_id": 0,
        #     "cost_center_group": 0,
        #     "user_id": 0,
        #     "is_shared_short_code": 0,
        #     "campaign_id": 1
        # },
        # "attachments": None
        # }), headers={"Content-Type":"application/json"})