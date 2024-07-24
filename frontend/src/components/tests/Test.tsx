import React from "react"


function Test() {
    let items = ['Chicago', 'New York', 'Cairo', 'Toronto']
    return (
        <>
            <h1>Test Items</h1>
            <ul className="list-group">
                {items.map((item) => (
                    <li className="list-group-item" key={item} onClick={() => console.log('Clicked')}>{item}</li>
                ))}
            </ul>
        </>
    )
}

export default Test