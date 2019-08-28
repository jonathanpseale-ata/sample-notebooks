# this is a comment
# so is this

c.KubeSpawner.environment = { 'JUPYTER_ENABLE_LAB': 'true' }



c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': ['cull-idle-servers', '--timeout=30'],
    }
]