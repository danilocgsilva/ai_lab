const getData = async () => {
  try {
    const response = await fetch("http://0.0.0.0:5001/");
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.statusText);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Fetch error:", error);
  }
}

const provideModels = async () => {
    const models_names = await getData();
    console.log(models_names);
    return models_names;
}

export { provideModels, getData };
