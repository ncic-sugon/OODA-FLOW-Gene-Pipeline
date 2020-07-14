class wgssam(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgssam, self).__init__(
            name='wgs-samtools-1',
            image='10.18.101.90:80/library/wgs-samtools:latest',
            command=['./root/app/wgs_samtools.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'sam': '/output.txt',
            })

