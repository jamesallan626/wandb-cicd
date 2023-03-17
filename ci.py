import wandb
print(f'The version of wandb is: {wandb.__version__}')

# will not pass
assert wandb.__version__ == '2.1.01', f'Expected version 2.1.01, but got {wandb.__version__}'

# will pass
# assert wandb.__version__ == '0.14.0', f'Expected version 0.14.0, but got {wandb.__version__}'
