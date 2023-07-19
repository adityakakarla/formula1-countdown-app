import React, { useState, useEffect } from 'react';

function Standings() {
  const [data, setData] = useState();

  useEffect(() => {
    fetch('/standings')
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      {!data ? (
        <p>Loading...</p>
      ) : (
        <div class="text-center">
            <h2 class="mt-5 mb-3">Current Standings:</h2>
          {data.map((data, i) => (
            <p key={i}>{data.driver}: {data.points}</p>
          ))}
        </div>
      )}
    </div>
  );
}

export default Standings;
