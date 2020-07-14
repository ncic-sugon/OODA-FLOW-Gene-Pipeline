class wgsind(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgsind, self).__init__(
            name='wgs-indel-1',
            image='10.18.101.90:80/library/wgs-indel:latest',
            command=['./root/app/wgs_indel1.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'ind': '/output.txt',
            })

