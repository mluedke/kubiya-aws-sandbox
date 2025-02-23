from kubiya_sdk.tools import Arg
from .base import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

list_sandboxes = AWSCliTool(
    name="list_sandboxes",
    description="List sandbox accounts",
    content="aws organizations list-children --child-type ORGANIZATIONAL_UNIT --parent-id $SANDBOX_OU_ID",
    args=[],
    mermaid_diagram=""
)

create_account = AWSCliTool(
    name="create_account",
    description="Create AWS account to add to the pool of available sandboxes",
    content="aws organizations create-account --email mike.luedke+sandbox-aardvark@sysdig.com --account-name sandbox-aardvark —-tags Key=leased,Value=19700101",
    args=[],
    mermaid_diagram=""
)

check_account_status = AWSCliTool(
    name="check_account_status",
    description="Check the creation status of an account",
    content="aws organizations describe-create-account-status --create-account-request-id $request_id",
    args=[
        Arg(name="request_id", description="Id of request from create account step", required=True)
    ],
    mermaid_diagram=""
)

tool_registry.register(list_sandboxes)
tool_registry.register(create_account)
tool_registry.register(check_account_status)