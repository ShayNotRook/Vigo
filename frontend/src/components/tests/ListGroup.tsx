import React, { useState } from "react"
// import { MouseEvent } from "react"
import './styles.css'

interface Props {
  items: string[];
  header: string;
  onSelectedItem: (item: string) => void;
}

function ListGroup({ items, header, onSelectedItem }: Props) {
    const [selectedIndex, setSelectedIndex] = useState(-1);
    // Event Handler (Click)
    return (
      <>
        <h1>{header}</h1>
        <ul className="list-group">
          {items.map((item, index) => (
            <li
              className={
                selectedIndex === index
                  ? "list-group-item active"
                  : "list-group-item"
              }
              key={item}
              onClick={() => {
                setSelectedIndex(index);
                onSelectedItem(item);
              }}
            >
              {item}
            </li>
          ))}
        </ul>
      </>
    );
}

export default ListGroup