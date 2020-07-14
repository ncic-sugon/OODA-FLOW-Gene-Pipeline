class wgsind1(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgsind1, self).__init__(
            name='wgs-indel-2',
            image='10.18.101.90:80/library/wgs-indel:latest',
            command=['./root/app/wgs_indel2.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'ind': '/output.txt',
            })
