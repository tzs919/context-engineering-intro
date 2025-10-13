# Template Generation Request

## TECHNOLOGY/FRAMEWORK:

**Example:** LangGraph AI agents  

**Your technology:** LangGraph,LangChain,LangSmith

---

## TEMPLATE PURPOSE:
- Building intelligent AI agents with tool integration, conversation handling, and structured data validation using LangGraph AI framework
---

## CORE FEATURES:
- Agent creation with different model providers (OpenAI, Anthropic, Gemini)
- Tool integration patterns (web search, file operations, API calls)
- Conversation memory and context management
- Structured output validation with Pydantic models
- Error handling and retry mechanisms
- Testing patterns for AI agent behavior

---

## EXAMPLES TO INCLUDE:
- Basic chat agent with memory
- Tool-enabled agent (web search + calculator)
- Multi-step workflow agent
- Agent with custom Pydantic models for structured outputs
- Testing examples for agent responses and tool usage

---

## DOCUMENTATION TO RESEARCH:

- https://langchain-ai.github.io/langgraph/ - Official langgraph AI documentation
- https://langchain-ai.github.io/langgraph/examples/ - langgraph examples
- https://langchain-ai.github.io/langgraph/guides/ - langgraph guides
- https://langchain-ai.github.io/langgraph/reference/
- https://langchain-ai.github.io/langgraph/additional-resources/
- Model provider APIs (OpenAI, Anthropic) for integration patterns
- Tool integration best practices and examples
- Testing frameworks for AI applications



---

## DEVELOPMENT PATTERNS:
- How to structure agent modules and tool definitions
- Configuration management for different model providers
- Environment setup for development vs production
- Logging and monitoring patterns for AI agents
- Version control patterns for prompts and agent configurations

---

## SECURITY & BEST PRACTICES:
- API key management and rotation
- Input validation and sanitization for agent inputs
- Rate limiting and usage monitoring
- Prompt injection prevention
- Cost control and monitoring for model usage

---

## COMMON GOTCHAS:
- Model context length limitations and management
- Handling model provider rate limits and errors
- Token counting and cost optimization
- Managing conversation state across requests
- Tool execution error handling and retries

---

## VALIDATION REQUIREMENTS:
- Agent response quality testing
- Tool integration testing
- Model provider fallback testing
- Cost and performance benchmarking
- Conversation flow validation
---

## INTEGRATION FOCUS:
- Integration with vector databases (Pinecone, Weaviate)
- Web scraping tools and APIs
- External API integrations for tools
- Monitoring services (Weights & Biases, LangSmith)
- Deployment platforms (Modal, Replicate)

---

## ADDITIONAL NOTES:
- Focus on TypeScript patterns and include comprehensive type definitions
- 使用uv而不是pip

---

## TEMPLATE COMPLEXITY LEVEL:

**What level of complexity should this template target?**

- [ ] **Beginner-friendly** - Simple getting started patterns
- [ ] **Intermediate** - Production-ready patterns with common features  
- [ ] **Advanced** - Comprehensive patterns including complex scenarios
- [ ] **Enterprise** - Full enterprise patterns with monitoring, scaling, security

**Your choice:** Beginner-friendly

---
