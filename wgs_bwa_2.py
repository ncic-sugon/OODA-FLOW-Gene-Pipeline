class wgsbwa1(dsl.ContainerOp):
    """test images-wgs-nfs:v1"""

    def __init__(self, validate=None):
        super(wgsbwa1, self).__init__(
            name='wgs-bwa-2',
            image='10.18.101.90:80/library/wgs-bwa:latest',
            command=['./root/app/wgs_bwa1.sh'],
            arguments=[
                '--validate', validate,
            ],
            file_outputs={
                'bwa': '/output.txt',
            })

