// app.js
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const input = document.querySelector("#city");
    const weatherInfo = document.querySelector(".weather-info");

    form.addEventListener("submit", function(e) {
        e.preventDefault();
        weatherInfo.innerHTML = "<p>Loading...</p>";
        fetchWeather(input.value);
    });

    function fetchWeather(city) {
        fetch(`/weather?city=${city}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    weatherInfo.innerHTML = `<p class="error">${data.error}</p>`;
                } else {
                    const { city, temperature, pressure, humidity, description, icon } = data;
                    weatherInfo.innerHTML = `
                        <h2>Weather in ${city}</h2>
                        <p>Temperature: ${temperature}°C</p>
                        <p>Pressure: ${pressure} hPa</p>
                        <p>Humidity: ${humidity}%</p>
                        <p>Description: ${description}</p>
                        <img src="http://openweathermap.org/img/wn/${icon}@2x.png" alt="Weather Icon">
                    `;
                }
            })
            .catch(err => {
                weatherInfo.innerHTML = `<p class="error">Error fetching data. Please try again later.</p>`;
            });
    }
});
