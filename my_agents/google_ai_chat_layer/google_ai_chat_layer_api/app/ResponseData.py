class ResponseData:
    def __init__(self, data: dict):
        self.content = data.get("content")
        self.additional_kwargs = data.get("additional_kwargs", {})
        self.response_metadata = data.get("response_metadata", {})
        self.type = data.get("type")
        self.name = data.get("name")
        self.id = data.get("id")
        self.example = data.get("example")
        self.tool_calls = data.get("tool_calls", [])
        self.invalid_tool_calls = data.get("invalid_tool_calls", [])
        self.usage_metadata = data.get("usage_metadata", {})

    def __repr__(self):
        return f"<ResponseData id={self.id} type={self.type}>"
