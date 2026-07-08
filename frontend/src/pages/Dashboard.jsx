import { useState, useEffect } from "react";
import API from "../services/api";

function Dashboard() {
    const [image, setImage] = useState(null);
    const [textiles, setTextiles] = useState([]);

    const handleImage = (e) => {
        setImage(URL.createObjectURL(e.target.files[0]));
    };

    useEffect(() => {
        API.get("textiles/")
            .then((response) => {
                setTextiles(response.data);
            })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }, []);

    return (
        <div className="dashboard">

            <h1>Textile Waste Classification</h1>

            <p>Select a textile waste image for AI analysis.</p>

            <input
                type="file"
                accept="image/*"
                onChange={handleImage}
            />

            <br /><br />

            {image && (
                <img
                    src={image}
                    alt="Preview"
                    className="preview"
                />
            )}

            <br /><br />

            <button>Predict</button>

            <hr />

            <h2>Textile Inventory</h2>

            <ul>
                {textiles.map((item) => (
                    <li key={item.id}>
                        <strong>{item.material_type}</strong> -
                        {item.quantity} kg -
                        {item.color} -
                        {item.source}
                    </li>
                ))}
            </ul>

        </div>
    );
}

export default Dashboard;