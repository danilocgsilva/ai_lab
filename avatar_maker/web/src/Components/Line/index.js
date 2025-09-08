const Line = (props) => {
    let tagClasses = "";
    switch (props.tagType) {
        case "green":
            tagClasses = "px-3 py-1 text-sm bg-green-100 text-green-600 rounded-full";
            break;
        case "yellow":
            tagClasses = "px-3 py-1 text-sm bg-yellow-100 text-yellow-600 rounded-full";
            break;
        case "red":
            tagClasses = "px-3 py-1 text-sm bg-red-100 text-red-600 rounded-full";
            break;
    }

    return (
        <li className="bg-white shadow-md rounded-2xl p-4 flex items-center justify-between hover:shadow-lg transition">
            <div>
                <h3 className="text-lg font-semibold text-gray-700">{props.label}</h3>
                
                {
                    props.thinLine && (
                        <p className="text-sm text-gray-500">{ props.thinLine }</p>
                    )
                }
                
            </div>

            {
                props.tagMessage && props.tagType && (
                    <span className={tagClasses}>{props.tagMessage}</span>
                )
            }
        </li>
    );
};

export default Line;