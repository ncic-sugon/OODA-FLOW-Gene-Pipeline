class wgsend(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None, validate1=None):
        super(wgsend, self).__init__(
            name='time-end',
            image='10.18.101.90:80/library/wgs-start-end:latest',
            command=['./root/app/end.sh'],
            arguments=['--validate', validate,
                       '--validate1', validate1,
                       ],
            file_outputs={
                'end': '/output.txt',
            })

