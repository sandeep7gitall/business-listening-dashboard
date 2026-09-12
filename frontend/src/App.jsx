import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [cityData, setCityData] = useState([]);
  const [categoryData, setCategoryData] = useState([]);
  const [sourceData, setSourceData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/dashboard/city")
      .then((res) => res.json())
      .then((data) => setCityData(data));

    fetch("http://127.0.0.1:8000/api/dashboard/category")
      .then((res) => res.json())
      .then((data) => setCategoryData(data));

    fetch("http://127.0.0.1:8000/api/dashboard/source")
      .then((res) => res.json())
      .then((data) => setSourceData(data));
  }, []);

  const totalListings = cityData.reduce(
    (total, item) => total + Number(item.count),
    0
  );

  return (
    <div className="app">
      <header className="navbar">
        <h2>Business Listening Dashboard</h2>
        <p classname="author">created by sandeep rana</p>

        <nav>
          <a href="#dashboard">Dashboard</a>
          <a href="#city">City</a>
          <a href="#category">Category</a>
          <a href="#source">Source</a>
        </nav>
      </header>

      <main>
        <section className="hero" id="dashboard">
          <h1>Business Listening Dashboard</h1>
          <p>
            Monitor business listings, categories, cities and sources from one
            place.
          </p>
        </section>

        <section className="cards">
          <div className="card">
            <h3>Total Listings</h3>
            <p className="number">{totalListings}</p>
            <span>From database</span>
          </div>

          <div className="card">
            <h3>Total Cities</h3>
            <p className="number">{cityData.length}</p>
            <span>Unique cities</span>
          </div>

          <div className="card">
            <h3>Total Categories</h3>
            <p className="number">{categoryData.length}</p>
            <span>Business categories</span>
          </div>

          <div className="card">
            <h3>Total Sources</h3>
            <p className="number">{sourceData.length}</p>
            <span>Listing sources</span>
          </div>
        </section>

        <section className="content-section" id="city">
          <h2>City Wise Listings</h2>

          <table>
            <thead>
              <tr>
                <th>City</th>
                <th>Listings</th>
              </tr>
            </thead>

            <tbody>
              {cityData.map((item, index) => (
                <tr key={index}>
                  <td>{item.city}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <section className="content-section" id="category">
          <h2>Category Wise Listings</h2>

          <table>
            <thead>
              <tr>
                <th>Category</th>
                <th>Listings</th>
              </tr>
            </thead>

            <tbody>
              {categoryData.map((item, index) => (
                <tr key={index}>
                  <td>{item.category}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <section className="content-section" id="source">
          <h2>Source Wise Listings</h2>

          <table>
            <thead>
              <tr>
                <th>Source</th>
                <th>Listings</th>
              </tr>
            </thead>

            <tbody>
              {sourceData.map((item, index) => (
                <tr key={index}>
                  <td>{item.source}</td>
                  <td>{item.count}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  );
}

export default App;