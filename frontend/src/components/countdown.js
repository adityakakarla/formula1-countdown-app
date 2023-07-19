import React, { useState, useEffect } from 'react';
import { Row, Col } from 'react-bootstrap';

function Countdown() {
  const [data, setData] = useState();

  useEffect(() => {
    fetch('/next_race')
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      {!data ? (
        <p>Loading...</p>
      ) : (
        <div>
          <h1 class="text-center mt-3">Next Up: The {data.name}</h1>
            <div class="mt-5 mx-4">
            <Row>
              <Col>
                <h1 class="text-center">{data.days}</h1>
                <p class="text-center">Days</p>
              </Col>
              <Col>
                <h1 class="text-center">{data.hours}</h1>
                <p class="text-center">Hours</p>
              </Col>
              <Col>
                <h1 class="text-center">{data.minutes}</h1>
                <p class="text-center">Minutes</p>
              </Col>
              <Col>
                <h1 class="text-center">{data.seconds}</h1>
                <p class="text-center">Seconds</p>
              </Col>
            </Row>
            </div>
        </div>
      )}
    </div>
  );
}

export default Countdown;
