from kubiya_sdk.tools import Arg
from . import AWSCliTool
from kubiya_sdk.tools.registry import tool_registry

list_accounts = AWSCliTool(
    name="list_accounts",
    description="List accounts",
    content="aws organizations list-accounts",
    args=[],
    mermaid_diagram=""
)