# `ec2.DescribeSubnets` issue

Steps to repro:

1) Install dependencies: `pip install pulumi pulumi-aws`
2) Start localstack: `docker run -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN} -e LS_LOG=debug -p 4566:4566 localstack/localstack-pro:3.8.0`
3) Run Pulumi program against localstack: `pulumi -s gst preview`

You'll notice the Pulumi command hangs, and the reported errors show up in the localstack logging.
