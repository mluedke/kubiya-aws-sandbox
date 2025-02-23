from kubiya_sdk.tools import Arg
from .base import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

list_accounts = AWSCliTool(
    name="list_accounts",
    description="List accounts",
    content="aws organizations list-accounts --child-type ORGANIZATIONAL_UNIT --parent-id ou-4yit-ixuehhs9",
    args=[
    ],
    mermaid_diagram=""
)

tool_registry.register(list_accounts)