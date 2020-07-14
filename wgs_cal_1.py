class wgscal(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgscal, self).__init__(
            name='wgs-call-1',
            image='10.18.101.90:80/library/wgs-call:latest',
            command=['./root/app/wgs_call1.sh'],
            arguments=['--validate', validate],
            file_outputs={
                'cal': '/output.txt',
            })

