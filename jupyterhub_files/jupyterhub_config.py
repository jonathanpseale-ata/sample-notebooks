#If you have many more users using the JupyterHub instance than you have memory and CPU resources, but you know not all
# users will use it at the same time, that is okay, so long as you shut down notebook instances when they have been
# idle, to free up resources.

c.JupyterHub.services = [
    {
        'name': 'cull-idle',
        'admin': True,
        'command': ['cull-idle-servers', '--timeout=300'],
    }
]




c.KubeSpawner.user_storage_pvc_ensure = True

c.KubeSpawner.pvc_name_template = '%s-nb-{username}' % application_name
c.KubeSpawner.user_storage_capacity = '1Gi'

c.KubeSpawner.volumes = [
    {
        'name': 'data',
        'persistentVolumeClaim': {
            'claimName': c.KubeSpawner.pvc_name_template
        }
    }
]

c.KubeSpawner.volume_mounts = [
    {
        'name': 'data',
        'mountPath': '/opt/app-root/src'
    }
]

print('#################################')
print('THIS IS THE PVC NAME TEMPLATE: %s' % c.KubeSpawner.pvc_name_template)
print('#################################')
print('THIS IS THE hub_connect_ip: %s' % str(c.KubeSpawner.hub_connect_ip))
print('#################################')
print('THIS IS THE APPLICATION_NAME: %s' % os.environ.get('APPLICATION_NAME', 'unknown'))
print('#################################')
print('THIS IS THE JUPYTERHUB_SERVICE_NAME: %s' % os.environ.get('JUPYTERHUB_SERVICE_NAME', 'unknown'))
