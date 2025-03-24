import React, { useState, useMemo, useCallback } from "react";
import "./ListOptimizer.css";
const ListOptimizer = () => {
  const [numbers] = useState([45, 12, 78, 23, 56, 89, 34, 67, 10]);
  const [threshold, setThreshold] = useState(20);
  const [sortOrder, setSortOrder] = useState("asc"); // 'asc' or 'desc'

  // Memoized Filtered List
  const filteredNumbers = useMemo(() => {
    return numbers.filter((num) => num >= threshold);
  }, [numbers, threshold]);

  // Memoized Sorting Function
  const sortedNumbers = useCallback(() => {
    return [...filteredNumbers].sort((a, b) => 
      sortOrder === "asc" ? a - b : b - a
    );
  }, [filteredNumbers, sortOrder]);

  return (
    <div className="container">
      <h2>Optimized List Sorting & Filtering</h2>
      
      {/* Threshold Input */}
      <label>Filter Threshold:</label>
      <input 
        type="number" 
        value={threshold} 
        onChange={(e) => setThreshold(Number(e.target.value))}
      />

      {/* Sorting Buttons */}
      <button onClick={() => setSortOrder("asc")}>Sort Ascending</button>
      <button onClick={() => setSortOrder("desc")}>Sort Descending</button>

      {/* Display Sorted & Filtered Numbers */}
      <h3>Filtered & Sorted List:</h3>
      <ul>
        {sortedNumbers().map((num, index) => (
          <li key={index}>{num}</li>
        ))}
      </ul>
    </div>
  );
};

export default ListOptimizer;
