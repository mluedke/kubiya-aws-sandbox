from kubiya_sdk.tools import Arg
from .base import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

list_sandboxes = AWSCliTool(
    name="list_sandboxes",
    description="List sandbox accounts",
    content="aws organizations list-children --child-type ACCOUNT --parent-id $SANDBOX_OU_ID",
    args=[],
    mermaid_diagram=""
)

create_account = AWSCliTool(
    name="create_account",
    description="Create AWS account to add to the pool of available sandboxes",
    content="aws organizations create-account --email mike.luedke+$account_name@sysdig.com --account-name $account_name",
    args=[
        Arg(name="account_name", description="Name of AWS account", required=True)
    ],
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

get_org_root_id = AWSCliTool(
    name="get_org_root_id",
    description="Get the id of the org root",
    content="aws organizations list-roots --query \"Roots[0].Id\"",
    args=[],
    mermaid_diagram=""
)

move_account_to_sandbox_ou = AWSCliTool(
    name="move_account_to_sandbox_ou",
    description="Move AWS account to the Sandbox OU",
    content="aws organizations move-account --account-id $account_id --source-parent-id $root_id --destination-parent-id $SANDBOX_OU_ID",
    args=[
        Arg(name="account_id", description="Id of account to move from check account status step", required=True),
        Arg(name="root_id", description="Id of org root", required=True)
    ],
    mermaid_diagram=""
)

tag_new_sandbox_account = AWSCliTool(
    name="tag_new_sandbox_account",
    description="Tag newly created sandbox account",
    content="aws organizations tag-resource --resource-id $account_id --tags Key=lease-expires,Value=1970-01-01T00:00:00Z Key=owner,Value=$KUBIYA_USER_EMAIL Key=name,Value=$account_name",
    args=[
        Arg(name="account_id", description="Id of account to tag from check account status step", required=True),
        Arg(name="account_name", description="Name of account to use as name tag from create_account step", required=True)
    ],
    mermaid_diagram=""
)

get_account_tags = AWSCliTool(
    name="get_account_tags",
    description="Get tags for the given account. Metadata for sandboxes is stored in tags",
    content="aws organizations list-tags-for-resource --resource-id $account_id",
    args=[
        Arg(name="account_id", description="Id of AWS account to get tags from", required=True)
    ],
    mermaid_diagram=""
)

tool_registry.register(list_sandboxes)
tool_registry.register(create_account)
tool_registry.register(check_account_status)
tool_registry.register(get_org_root_id)
tool_registry.register(move_account_to_sandbox_ou)
tool_registry.register(tag_new_sandbox_account)
tool_registry.register(get_account_tags)