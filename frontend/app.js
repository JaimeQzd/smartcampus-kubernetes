const loadRoomsButton = document.getElementById("load-rooms");
const roomsContainer = document.getElementById("rooms");
const statusElement = document.getElementById("status");


async function loadRooms() {
    statusElement.textContent = "Cargando aulas...";
    roomsContainer.innerHTML = "";

    try {
        // El frontend llama a /api.
        // Nginx reenviará esta petición al backend.
        const response = await fetch("/api/rooms");

        if (!response.ok) {
            throw new Error(
                `Error HTTP: ${response.status}`
            );
        }

        const rooms = await response.json();

        if (rooms.length === 0) {
            statusElement.textContent =
                "No hay aulas registradas.";

            return;
        }

        statusElement.textContent =
            `${rooms.length} aula(s) encontrada(s).`;

        rooms.forEach((room) => {
            const roomElement =
                document.createElement("article");

            roomElement.className = "room";

            const equipment =
                room.equipamiento.length > 0
                    ? room.equipamiento.join(", ")
                    : "Sin equipamiento";

            roomElement.innerHTML = `
                <h3>${room.nombre}</h3>
                <p><strong>Edificio:</strong> ${room.edificio}</p>
                <p><strong>Capacidad:</strong> ${room.capacidad}</p>
                <p><strong>Equipamiento:</strong> ${equipment}</p>
            `;

            roomsContainer.appendChild(roomElement);
        });
    } catch (error) {
        statusElement.textContent =
            "No se ha podido conectar con el backend.";

        console.error(error);
    }
}


loadRoomsButton.addEventListener(
    "click",
    loadRooms
);