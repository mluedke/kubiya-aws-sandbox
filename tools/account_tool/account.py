from kubiya_sdk.tools import Arg
from .base import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

list_accounts = AWSCliTool(
    name="list_accounts",
    description="List accounts",
    content="aws organizations list-accounts --child-type ORGANIZATIONAL-UNIT --parent-id $sandbox-ou",
    args=[
        Arg(name="sandbox-ou", type="str", description="Id of OU containing sandbox accounts", reqquired=True),
    ],
    mermaid_diagram=""
)

tool_registry.register(list_accounts)