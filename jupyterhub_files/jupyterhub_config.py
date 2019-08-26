# By default Jupyter Notebook images still use the classic web interface by default. If you want to enable the newer
# JupyterLab web interface set the JUPYTER_ENABLE_LAB environment variable.

c.KubeSpawner.environment = { 'JUPYTER_ENABLE_LAB': 'true' }


# When a notebook instance is created and a user creates their own notebooks if the instance is stopped they will loose
# any work they have done. To avoid this, you can configure JupyterHub to make a persistent volume claim and mount
# storage into the containers when a notebook instance is run. For the S2I enabled notebook images built, where the
# working directory when the notebook is run is /opt/app-root/src, you can add the following to the JupyterHub
# configuration. If you want to be able to pre-populate the persistent volume with notebooks and other files from the
# S2I built image, you can use the following configuration. This will also preserve additional Python packages which
# you might install.

c.KubeSpawner.user_storage_pvc_ensure = True

c.KubeSpawner.pvc_name_template = '%s-nb-{username}' % c.KubeSpawner.hub_connect_ip
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
        'mountPath': '/opt/app-root',
        'subPath': 'app-root'
    }
]

c.KubeSpawner.singleuser_init_containers = [
    {
        'name': 'setup-volume',
        'image': 's2i-minimal-notebook:3.6',
        'command': [
            'setup-volume.sh',
            '/opt/app-root',
            '/mnt/app-root'
        ],
        'resources': {
            'limits': {
                'memory': '256Mi'
            }
        },
        'volumeMounts': [
            {
                'name': 'data',
                'mountPath': '/mnt'
            }
        ]
    }
]