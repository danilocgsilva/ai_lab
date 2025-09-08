import Line from './Components/Line';

function App() {

    const models_names = [
        { 
            name: "Finish project report", 
        },
        {
            name: "Prepare presentation slides",
        },
        {
            name: "The model name",
        },
        {
            name: "One more",
        }
    ]

    return (
        <div className="bg-gray-100 min-h-screen flex items-center justify-center p-6">

            <div className="w-full max-w-3xl">
                <h2 className="text-3xl font-bold text-gray-800 mb-6">List of models</h2>

                <ul className="space-y-4">
                    {
                        models_names.map((model, index) => (
                            <Line 
                                key={index}
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
