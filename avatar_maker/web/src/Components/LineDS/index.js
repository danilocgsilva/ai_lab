const LineDS = (props) => {
    return (
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
    );
};

export default LineDS;
