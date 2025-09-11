import google.generativeai as genai
import os

def format_module_info(index, m):
  """Formats module information into a single string.

  Args:
    index: The index of the module (for numbering).
    m: The module object containing the data to be formatted.

  Returns:
    A single string containing the formatted module information.
  """
  return (
      f"{index}.\n" +
      f"Name: {m.name}\n" +
      f"displayName: {m.display_name}\n" +
      f"description: {m.description}\n" +
      f"supportedMethods: {m.supported_generation_methods}\n" +
      f"version: {m.version}\n" +
      f"display_name: {m.display_name}"  # Added the duplicate line as requested
  )

def format2(index, m):
    return (
        f"{index}. displayName: {m.display_name}, description: {m.description}, "
    )

def configure_genai():
    GOOGLE_API_KEY = os.environ.get("GEMINI_KEY")

    if not GOOGLE_API_KEY:
        raise RuntimeError("Please export GEMINI_KEY before running")

    genai.configure(api_key=GOOGLE_API_KEY)
