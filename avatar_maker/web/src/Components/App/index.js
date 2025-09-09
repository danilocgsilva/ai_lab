import Line from '../Line';
import { useState, useEffect } from 'react';
import { provideModels } from '../../functions';

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
