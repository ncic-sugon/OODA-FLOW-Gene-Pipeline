class wgspic1(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgspic1, self).__init__(
            name='wgs-picard-2',
            image='10.18.101.90:80/library/wgs-picard:latest',
            command=['./root/app/wgs_picard2.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'pic': '/output.txt',
            })


