import { useState, useEffect } from 'react';
import { provideModels } from '../../functions';
import LineDS from '../LineDS';

const AppDS = (props) => {
    const [models, setModels] = useState([]);

    useEffect(() => {
        async function fetchModels() {
            const modelsData = await provideModels();
            setModels(modelsData || []);
        }
        fetchModels();
    }, []);

    return (
        <div className="bg-gray-50 min-h-screen">
            <div className="container mx-auto px-4 py-8 max-w-4xl">
                <div className="text-center mb-8">
                    <h1 className="text-3xl font-bold text-gray-800 mb-2">Text Entries</h1>
                    <p className="text-gray-600">Manage and filter your text entries</p>
                </div>

                <div className="bg-white rounded-lg shadow-md p-6 mb-6">
                    <h2 className="text-lg font-semibold text-gray-700 mb-4">Filter Options</h2>
                    <div className="flex flex-wrap gap-6">
                        <label className="flex items-center space-x-2 cursor-pointer">
                            <input type="checkbox" id="filter-active" className="w-4 h-4 text-blue-600 rounded focus:ring-blue-500" />
                            <span className="text-gray-700">Active Entries</span>
                        </label>

                        <label className="flex items-center space-x-2 cursor-pointer">
                            <input type="checkbox" id="filter-important" className="w-4 h-4 text-blue-600 rounded focus:ring-blue-500" />
                            <span className="text-gray-700">Important Entries</span>
                        </label>

                        <button id="clear-filters" className="ml-auto text-sm text-blue-600 hover:text-blue-800 transition-colors">
                            Clear Filters
                        </button>
                    </div>
                </div>

                <div className="space-y-4" id="entries-list">



                    <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500 entry" data-active="true" data-important="true">
                        <div className="flex items-start justify-between mb-3">
                            <h3 className="text-lg font-semibold text-gray-800">Project Update</h3>
                            <div className="flex items-center space-x-2">
                                <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
                                <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">Important</span>
                            </div>
                        </div>
                        <p className="text-gray-600 mb-4">Completed the initial design phase and started development. The team is making good progress on the frontend components.</p>
                        <div className="text-sm text-gray-500">Created: September 9, 2024</div>
                    </div>

                    <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-gray-300 entry" data-active="false" data-important="true">
                        <div className="flex items-start justify-between mb-3">
                            <h3 className="text-lg font-semibold text-gray-800">Meeting Notes</h3>
                            <div className="flex items-center space-x-2">
                                <span className="px-2 py-1 bg-red-100 text-red-800 text-xs rounded-full">Inactive</span>
                                <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">Important</span>
                            </div>
                        </div>
                        <p className="text-gray-600 mb-4">Discussed upcoming deadlines and resource allocation. Need to follow up with the design team about the mockups.</p>
                        <div className="text-sm text-gray-500">Created: September 8, 2024</div>
                    </div>

                    <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500 entry" data-active="true" data-important="false">
                        <div className="flex items-start justify-between mb-3">
                            <h3 className="text-lg font-semibold text-gray-800">Daily Tasks</h3>
                            <div className="flex items-center space-x-2">
                                <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
                            </div>
                        </div>
                        <p className="text-gray-600 mb-4">Review pull requests, write documentation, and prepare for tomorrow's standup meeting.</p>
                        <div className="text-sm text-gray-500">Created: September 9, 2024</div>
                    </div>

                    <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-gray-300 entry" data-active="false" data-important="false">
                        <div className="flex items-start justify-between mb-3">
                            <h3 className="text-lg font-semibold text-gray-800">Old Reference</h3>
                            <div className="flex items-center space-x-2">
                                <span className="px-2 py-1 bg-red-100 text-red-800 text-xs rounded-full">Inactive</span>
                            </div>
                        </div>
                        <p className="text-gray-600 mb-4">This entry is no longer relevant but kept for historical reference purposes.</p>
                        <div className="text-sm text-gray-500">Created: August 15, 2024</div>
                    </div>

                    <LineDS />

                </div>

                <div id="no-results" className="hidden text-center py-12">
                    <div className="text-gray-400 mb-4">
                        <svg className="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                    </div>
                    <h3 className="text-lg font-semibold text-gray-600 mb-2">No entries found</h3>
                    <p className="text-gray-500">Try adjusting your filter criteria</p>
                </div>
            </div>
        </div>
    );
}

export default AppDS;