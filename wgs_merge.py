class wgsmer(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None, validate1=None):
        super(wgsmer, self).__init__(
            name='wgs-merge-first',
            image='10.18.101.90:80/library/wgs-merge:latest',
            command=['./root/app/merge.sh'],
            arguments=[
                '--validate', validate,
                '--validate1', validate1,
            ],
            file_outputs={
                'mer': '/output.txt',
            })

