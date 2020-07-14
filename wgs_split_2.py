class wgssplit1(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgssplit1, self).__init__(
            name='wgs-split-second',
            image='10.18.101.90:80/library/wgs-split-bam:latest',
            command=['./root/app/split.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'split': '/output.txt',
            })

