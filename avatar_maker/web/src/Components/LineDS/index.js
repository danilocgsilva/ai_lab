const selectMainLineClasses = (borderColor) => {
    let lineMainClasses = 'bg-white rounded-lg shadow-md p-6 border-l-4 entry ';

    switch (borderColor) {
        case 'on':
            lineMainClasses += 'border-blue-500';
            break;
        case 'off':
            lineMainClasses += 'border-gray-300';
            break;
        default:
            lineMainClasses += 'border-gray-300';
    }

    return lineMainClasses;
};

const selectWrapLableClasses = (thinLine, footerLine) => {
    let wrapLabelClasses = 'flex items-start justify-between ';

    if (thinLine === "" && footerLine === "") {
        wrapLabelClasses += 'mb-3';
    }
    return wrapLabelClasses;
};

const LineDS = ({borderColor, label, thinLine, footerLine}) => {

    let lineMainClasses = selectMainLineClasses(borderColor);
    let wrapLabelClasses = selectWrapLableClasses(thinLine, footerLine);

    return (
        <div className={lineMainClasses} data-active="true" data-important="true">
            <div className={wrapLabelClasses}>
                <h3 className="text-lg font-semibold text-gray-800">{label}</h3>
                <div className="flex items-center space-x-2">
                    <span className="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">Active</span>
                    <span className="px-2 py-1 bg-yellow-100 text-yellow-800 text-xs rounded-full">Important</span>
                </div>
            </div>

            {thinLine && (
                <p className="text-gray-600 mb-4">{thinLine}</p>
            )}
            {
                footerLine && (
                    <div className="text-sm text-gray-500">{footerLine}</div>
                )
            }
        </div>
    );
};

export default LineDS;
