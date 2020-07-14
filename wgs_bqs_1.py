class wgsbqs(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgsbqs, self).__init__(
            name='wgs-bqsr-1',
            image='10.18.101.90:80/library/wgs-bqsr:latest',
            command=['./root/app/wgs_bqsr1.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'bqs': '/output.txt',
            })

