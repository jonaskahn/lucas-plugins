# Lucas Plugins

This directory contains the plugin system for the Lucas Multi-Agent System. Plugins extend Lucas's capabilities by providing specialized agents with domain-specific tools and functionality.

## Plugin Architecture

Lucas uses a modular plugin architecture where each plugin is a self-contained agent with its own:
- **Agent Implementation**: Core logic and behavior
- **Tools**: Specific functions the agent can execute
- **Metadata**: Configuration and capability definitions
- **Dependencies**: Required packages and models

## Available Plugins

### Math Agent (`examples/math_agent/`)
A mathematical computation agent that handles basic arithmetic operations.

**Capabilities:**
- Addition, subtraction, multiplication, division
- Power and modulo operations
- Mathematical problem solving

**LLM Requirements:**
- Provider: OpenAI
- Model: GPT-4o
- Temperature: 0.8

### Search Agent (`examples/search_agent/`)
A web search and information retrieval agent for finding and gathering information.

**Capabilities:**
- Web search
- News search
- Academic search
- Image search
- Information lookup

**LLM Requirements:**
- Provider: OpenAI
- Model: GPT-4o
- Temperature: 0.8

## Plugin Structure

Each plugin follows this standard structure:

```
plugin_name/
├── agent.py          # Agent implementation
├── plugin.py         # Plugin entry point and metadata
├── tools.py          # Tool functions
└── requirements.txt  # Dependencies
```

### Core Files

- **`plugin.py`**: Entry point that defines metadata and creates agent instances
- **`agent.py`**: Main agent class implementing `BasePluginAgent`
- **`tools.py`**: Tool functions that the agent can use
- **`requirements.txt`**: Python dependencies specific to this plugin

## Creating a New Plugin

1. **Create Plugin Directory**
   ```bash
   mkdir plugins/examples/your_plugin_name
   ```

2. **Implement Plugin Entry Point** (`plugin.py`)
   ```python
   from lucas.plugins.base import BasePlugin, PluginMetadata
   
   class YourPlugin(BasePlugin):
       @staticmethod
       def get_metadata() -> PluginMetadata:
           return PluginMetadata(
               name="your_plugin_name",
               version="1.0.0",
               description="Your plugin description",
               capabilities=["capability1", "capability2"],
               llm_requirements={
                   "provider": "openai",
                   "model": "gpt-4o",
                   "temperature": 0.8,
                   "max_tokens": 1024,
               },
           )
   ```

3. **Implement Agent** (`agent.py`)
   ```python
   from lucas.plugins.base import BasePluginAgent
   
   class YourAgent(BasePluginAgent):
       def __init__(self, metadata):
           super().__init__(metadata)
           # Initialize your agent
   ```

4. **Define Tools** (`tools.py`)
   ```python
   def your_tool_function(param1: str) -> str:
       """Tool function docstring."""
       # Implement your tool logic
       return result
   ```

5. **Specify Dependencies** (`requirements.txt`)
   ```
   package-name>=1.0.0
   another-package>=2.0.0
   ```

## Plugin Discovery

Lucas automatically discovers plugins by:
1. Scanning the `plugins/examples/` directory
2. Loading plugin metadata from `plugin.py` files
3. Validating plugin security and structure
4. Registering available tools and capabilities

## Core Plugin System

The `core/` directory contains the foundational plugin system components:
- Base classes and interfaces
- Plugin loader and manager
- Security validation
- Tool binding utilities

## Best Practices

1. **Security**: Follow security guidelines and avoid dangerous operations
2. **Documentation**: Provide clear docstrings for all tools and methods
3. **Error Handling**: Implement proper error handling and logging
4. **Testing**: Include tests for your plugin functionality
5. **Dependencies**: Minimize external dependencies and specify versions

## Plugin Validation

All plugins undergo security validation to ensure:
- No dangerous imports or operations
- Proper structure and required files
- Valid metadata and configuration
- Compatible LLM requirements

For more information about the Lucas Multi-Agent System, see the main project README.