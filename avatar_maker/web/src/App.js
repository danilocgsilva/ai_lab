import Line from './Components/Line';
import { useState, useEffect } from 'react';

async function getData() {
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

async function provideModels() {
    const models_names = await getData();
    console.log(models_names);
    return models_names;
}

const App = () => {
    const [models, setModels] = useState([]);

    useEffect(() => {
        async function fetchModels() {
            const modelsData = await provideModels();
            setModels(modelsData || []);
        }
        fetchModels();
    }, []);

    return (
        <div className="bg-gray-100 min-h-screen flex items-center justify-center p-6">

            <div className="w-full max-w-3xl">
                <h2 className="text-3xl font-bold text-gray-800 mb-6">List of models</h2>

                <ul className="space-y-4">
                    {
                        models.map((model) => (
                            <Line
                                key={model.name}
                                label={model.name}
                                thinLine={model.thinLine}
                                tagMessage={model.tag?.tagMessage}
                                tagType={model.tag?.tagType}
                            />
                        ))
                    }
                </ul>
            </div>

        </div>
    );
}

export default App;
