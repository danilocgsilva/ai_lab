import { useState } from 'react';

const App = () => {

    const [ isReadOnly, setReadOnly ] = useState(false);

    const onSubmit = (e) => {
        e.preventDefault();
        setReadOnly(true);
    }

    let textAreaClasses = "pl-10 w-full rounded-lg border-gray-300 border focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 py-3 px-4 transition duration-300";
    if (isReadOnly) {
        textAreaClasses += " bg-gray-100 text-gray-500 cursor-not-allowed opacity-75";
    }

    return (
        <div className="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center p-4">
            <div className="w-full max-w-2xl">
                <div className="bg-white rounded-xl shadow-2xl p-6 md:p-8 transition-all duration-300 hover:shadow-xl">
                    <div className="text-center mb-8">
                        <h1 className="text-3xl font-bold text-gray-800 mb-2">Ask</h1>
                    </div>

                    <form className="space-y-6" onSubmit={onSubmit}>

                        <div>
                            <label for="message" className="block text-sm font-medium text-gray-700 mb-1">Question</label>
                            <div className="relative">
                                <div className="absolute top-3 left-3 pointer-events-none">
                                    <i className="fas fa-comment text-gray-400"></i>
                                </div>
                                <textarea id="message" rows="4" readOnly={isReadOnly}
                                    className={textAreaClasses}
                                    placeholder="Your question here..."></textarea>
                            </div>
                        </div>


                        <div className="pt-4">
                            <button type="submit"
                                className="w-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-medium py-3 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-300 transform hover:-translate-y-0.5 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                                <span className="flex items-center justify-center">
                                    <i className="fas fa-paper-plane mr-2"></i>
                                    Ask
                                </span>
                            </button>
                        </div>
                    </form>

                </div>
            </div>
        </div>
    );
}

export default App;
