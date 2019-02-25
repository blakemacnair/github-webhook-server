import subprocess


class PullRequest:

    def __init__(self, args):
        self.args = args

    def handle_request(self):
        pr = self.args['pull_request']
        title = pr['title']
        state = pr['state']
        merged = pr['merged']
        if merged:
            self.handle_pr_merged()

        return {'title': title, 'state': state, 'merged': merged}

    def handle_pr_merged(self):
        subprocess.run(["aplay", "sounds/airhorn.wav"])
