class wgsstart(dsl.ContainerOp):
    """validation for file"""

    def __init__(self):
        super(wgsstart, self).__init__(
            name='time-start',
            image='10.18.101.90:80/library/wgs-start-end:latest',
            command=['./root/app/start.sh'],
            file_outputs={
                'start': '/output.txt',
            })


