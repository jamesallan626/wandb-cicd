# wandb-cicd

This repository contains resources for W&B course "CI/CD for ML". Primarily we learn about GitHub Actions.<br>

James Allan (Mar. 17, 2023)

<b>Course References</b>:<br>
https://www.wandb.ai/<br>
https://www.wandb.courses/<br>
https://github.com/jacopotagliabue/you-dont-need-a-bigger-boat<br>
https://github.com/hamelsmu/wandb-cicd<br>
https://pypi.org/project/wandb/<br>
https://github.com/fastai/fastai<br>

<b>Code in Repo</b>:<br>
ci.yaml      - default 'Hello World'<br>
secret.yml   - looks at encrypted secrets &#128064;<br>
trigger.yaml - looks at event triggers (push, pull_request, workflow_dispatch)<br>
vars.yaml    - looks at special variables : github contexts and their properties, default environment variables<br>
io.yaml      - looks at creating variables dynamically and using them across steps<br>

<b>Other References (useful for code above)</b>:<br>
https://docs.github.com/en/actions<br>
https://docs.github.com/en/actions/quickstart<br>
https://github.com/actions/checkout<br>
https://docs.github.com/en/actions/learn-github-actions/contexts<br>
https://docs.github.com/en/actions/learn-github-actions/contexts#github-context<br>
https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables<br>
https://docs.github.com/en/actions/security-guides/encrypted-secrets &#128064;<br>
https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows<br>
https://docs.github.com/en/actions/using-jobs/defining-outputs-for-jobs<br>
https://stackoverflow.com/questions/59191913/how-do-i-get-the-output-of-a-specific-step-in-github-actions<br>
https://docs.python.org/3/library/os.html#os.environ<br>
https://github.com/community/community/discussions/28146 (setting output from a python script in GitHub Workflow)<br>
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests<br>
https://github.com/hamelsmu/wandb-cicd/blob/main/.github/workflows/chatops.yml<br>



<br>
<br>
End of README.MD
