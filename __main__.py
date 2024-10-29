import pulumi
from pulumi import Output
from pulumi_aws import ec2, vpc

default_vpc = ec2.DefaultVpc("default")
res = ec2.get_subnets(
    filters=[
        ec2.GetSubnetsFilterArgs(name="vpc-id", values=[default_vpc.id]),
        ec2.GetSubnetsFilterArgs(name="map-public-ip-on-launch", values=[True]),
    ]
)
pulumi.export("vpc-ids", res.ids)
