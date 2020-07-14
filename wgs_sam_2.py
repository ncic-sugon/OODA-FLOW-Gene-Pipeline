class wgssam1(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgssam1, self).__init__(
            name='wgs-samtools-2',
            image='10.18.101.90:80/library/wgs-samtools:latest',
            command=['./root/app/wgs_samtools1.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'sam1': '/output.txt',
            })

