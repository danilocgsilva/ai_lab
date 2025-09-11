# Available models

I needed to ask to Gemini chat, as there's anything convenient to got to know the available models.

## Question:

I am trying to use locally ChatGoogleGenerativeAI from langchain_google_genai. I am having an issue when setting the model. I need to know what put in the model parameter, but don't know what are available models. How does I got to know this?

## Answer

To find the available models for `ChatGoogleGenerativeAI` from `langchain_google_genai`, you should refer to the **Gemini API documentation**.

The `model` parameter in `ChatGoogleGenerativeAI` accepts the model ID string. Here are some of the popular Gemini models and their corresponding model ID strings:

  * **`gemini-2.5-pro`**: This is an advanced reasoning model for complex tasks.
  * **`gemini-2.5-flash`**: A faster and more cost-effective model with well-rounded capabilities.
  * **`gemini-2.5-flash-lite`**: The most cost-efficient model designed for high-throughput tasks.
  * **`gemini-2.0-flash`**: A multimodal model with improved speed and a 1M token context window.
  * **`gemini-1.5-pro`**: A powerful model for complex reasoning tasks.
  * **`gemini-1.5-flash`**: A versatile model with a large context window, optimized for speed.

You can also use models that are in preview or experimental stages. These are often named with a suffix like `-preview` or `-exp`. For example, a model for image generation might be `gemini-2.0-flash-preview-image-generation`.

To use one of these models, you'd initialize `ChatGoogleGenerativeAI` like this:

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
```
